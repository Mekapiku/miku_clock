#!/usr/bin/env python
# coding: utf-8

import time
import pusherclient

import miku

global pusher

def channel_callback(data):
	miku.add_miku_queue(data)
	print "Channel Callback: %s" % data

def connect_handler(data):
    channel = pusher.subscribe("miku_clock_channel")
    channel.bind('wakeup', channel_callback)   

if __name__ == '__main__':
    appkey = 'app_key'
    secret = 'app_seret'
    userid = 'user_id'

    pusher = pusherclient.Pusher(appkey, secret=secret, user_data={'user_id': userid})

    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:
    	miku.process_miku()
        time.sleep(1)