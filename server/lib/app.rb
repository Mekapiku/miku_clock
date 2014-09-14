require 'sinatra/base'
require 'haml'
require 'omniauth-twitter'

require 'pusher'

Pusher.url="pusher_url"
PUSHER_KEY='pusher_key'
PUSHER_SECRET='pusher_secret'

ENV['CONSUMER_KEY']="consumer_key"
ENV['CONSUMER_SECRET']="consumer_secret"

module MikuClock
  class App < Sinatra::Base

    enable :sessions

    use OmniAuth::Builder do
      provider :twitter, ENV['CONSUMER_KEY'], ENV['CONSUMER_SECRET']
    end

    # トップページ
    get "/" do
      if session[:info].nil?
        redirect "/auth/twitter"
      end

      @twitter_screen_name = session[:info]['nickname']
      @twitter_name = session[:info]['name']

      haml :index
    end

    # Twitter認証
    get "/auth/:name/callback" do
      # @auth = request.env['omniauth.auth']
      session[:info] = env['omniauth.auth']['info']
      redirect to('/')
      # haml :callback
    end

    # 僕を起こすPush通知を量産させる
    post "/wakeup" do
      if @@wake_up
        return "wakeup"
      end

      Pusher['miku_clock_channel'].trigger('wakeup', {
        name: session[:info]['nickname'], message: params[:in]
      })
      return "send"
    end

    # 起きる時間をクライアント側にセットする
    post "/set" do
      begin
        @@set_time = Time.parse(params[:time])
        @@wake_up = false
      rescue
        return Exception
      end
    end

    # 起きた時にクライアント側から呼ぶ
    post "/stop" do
      begin
        @@stop_time = Time.parse(params[:time])
        @@wake_up = true
      rescue
        return Exception
      end
    end
  end
end
