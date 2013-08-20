#coding:utf-8

import urllib2
from BeautifulSoup import BeautifulStoneSoup
import cookielib

class DoubanMovies:

    def __init__(self,url):
        self.url = url

    def openUrl(self):
        cj = cookielib.CookieJar()
        openUrl = urllib2.urlopen(self.url)
        cjHander = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cjHander)
        urllib2.install_opener(opener)

        return openUrl.readlines()

    def parseHtml(self):
        movieStr = ''
        movieResStr = ''
        for html in self.openUrl():
            movieStr += str(html)
        soup = BeautifulStoneSoup(movieStr)
        #print soup
        print soup.findAll('div',{'class':'mod-bd'})

if __name__ =="__main__":
    print DoubanMovies("http://movie.douban.com/nowplaying/shanghai").parseHtml()