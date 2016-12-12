import urllib
import urllib2
import cookielib
import time

from bs4 import BeautifulSoup

import config


class Douban:

    def __init__(self):
        self.loginURL = "https://www.douban.com/accounts/login"
        self.myMovieURL = "https://movie.douban.com/mine?status=collect"
        self.frankMoviesURL = "https://movie.douban.com/people/Gawiel/collect"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
        self.headers = {'User-Agent': self.user_agent}
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'form_email': config.USERNAME,
            'form_password': config.PASSWORD,
        })
        self.myopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def login(self):
        request = urllib2.Request(
            self.loginURL,
            self.postdata,
            self.headers
        )
        self.myopener.open(request)
        time.sleep(config.SLEEP_TIME)

    def readMovies(self):
        movieRequest = urllib2.Request(
            self.frankMoviesURL,
            None,
            self.headers
        )
        content = self.myopener.open(movieRequest).read()
        soup = BeautifulSoup(content, 'html.parser')
        movies = soup.body.find_all(id="wrapper")
        print movies

    def load(self):
        url = 'http://www.douban.com/people/Gawiel/'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        content = response.read()
        print content

spider = Douban()
spider.readMovies()