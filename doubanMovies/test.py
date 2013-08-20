#coding:utf-8

import urllib2
from BeautifulSoup import BeautifulStoneSoup
import cookielib
from threading import Thread


HOST_URL = 'http://m.douban.com'

class DoubanMovies:
    def __init__(self):
        self.url = ''

    def openUrl(self):
        cj = cookielib.CookieJar()
        openUrl = urllib2.urlopen(self.url)
        cjHander = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cjHander)
        urllib2.install_opener(opener)

        return openUrl.readlines()

    #tag=p是正在热映的影片id
    #tag=h3是即将上映影片的id
    def getMovieId(self,tag):
        movieStr = ''
        movieId =[]
        for html in self.openUrl():
            movieStr += str(html).strip()
        soup = BeautifulStoneSoup(movieStr.strip(''))

        for con in soup.findAll(tag):
            res = BeautifulStoneSoup(str(con))
            movieId.append(str(res.a["href"]).split("/")[-2])

        return movieId


    #正在热映影片ID
    def nowPlaying(self):
        movie_id = []
        for i in range(1,3,1):
            url = HOST_URL + '/movie/recent/now?page=' + str(i)+'&session=833b8d4c'
            self.url = url
            for id in self.getMovieId('p'):
                movie_id.append(id)
        return movie_id

    #即将上映影片ID
    def soonPlaying(self):
        url = r'http://movie.douban.com/later/shanghai/'
        self.url = url
        self.openUrl()
        return self.getMovieId('h3')


#http://api.douban.com/v2/movie/subject/movieId(豆瓣接口)
if __name__ == "__main__":
    print DoubanMovies().nowPlaying()

