#!/usr/bin/python

import sys
import urllib2

def testFunc():
    req = urllib2.Request('http://google.com')
    res = urllib2.urlopen(req)
    html = res.read()
    print(html)
    return "This worked"

def main():
    print(testFunc())
    

if __name__ == '__main__':
    testFunc()