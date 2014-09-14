#!/usr/bin/env python
# coding: utf-8

import urllib
import urllib2

from datetime import datetime as dt
from datetime import datetime as dt

url = 'http://mikuclock.herokuapp.com/stop'
#url = 'http://0.0.0.0:5000/stop'

if __name__ == '__main__':

    tdatetime = dt.now().strftime('%Y/%m/%d %H:%M:%S')

    params = {'time' : tdatetime}
    params = urllib.urlencode(params)

    req = urllib2.Request(url)
    req.add_data(params)

    res = urllib2.urlopen(req)
    body = res.read()