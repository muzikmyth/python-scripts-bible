# Filename      : check_internet_con.py
# Author		: Abhijit Kumar
# Created		: 29 Dec 2017

# Description   : Just checks internet connection is works or not.

#!/usr/bin/python3
import urllib2


def checkInternetConnectivity():
    try:
        urllib2.urlopen("http://google.com", timeout=2)
        print("Working connection")

    except urllib2.URLError as E:
        print("Connection error:%s" % E.reason)


checkInternetConnectivity()
