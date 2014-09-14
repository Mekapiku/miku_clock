#!/usr/bin/env python
# coding: utf-8

import sys

import urllib
import urllib2

from datetime import datetime as dt
from datetime import datetime as dt

url = 'http://mikuclock.herokuapp.com/set'
#url = 'http://0.0.0.0:5000/set'

if __name__ == '__main__':
    if len(sys.argv) != 3:
    	print "please input time. %%Y/%%m/%%d %%H:%%M:%%S"
        sys.exit(1)

    arg_date = sys.argv[1]
    arg_time = sys.argv[2]

    tstr = "%s %s" % (arg_date, arg_time)
    tdatetime = dt.strptime(tstr, '%Y/%m/%d %H:%M:%S')

    params = {'time' : tdatetime}
    params = urllib.urlencode(params)

    req = urllib2.Request(url)
    req.add_data(params)

    res = urllib2.urlopen(req)
    body = res.read()