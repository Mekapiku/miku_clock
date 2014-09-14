# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'miku_clock/version'

Gem::Specification.new do |spec|
  spec.name          = "miku_clock"
  spec.version       = MikuClock::VERSION
  spec.authors       = ["mekapiku"]
  spec.email         = ["mekapiku@gmail.com"]
  spec.summary       = %q{TODO: Write a short summary. Required.}
  spec.description   = %q{TODO: Write a longer description. Optional.}
  spec.homepage      = ""
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0")
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.6"
  spec.add_development_dependency "rake"
  spec.add_development_dependency "foreman"

  spec.add_dependency "faye-websocket"
  spec.add_dependency "puma"
  spec.add_dependency "sinatra"
  spec.add_dependency "haml"

  spec.add_dependency "omniauth"
  spec.add_dependency "omniauth-twitter"

  spec.add_dependency "pusher"

  spec.required_ruby_version = ">= 2.0.0"
end
