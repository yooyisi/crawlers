import urllib2
import re

page = 1

class HScw:
    def __init__(self):
        self.pageIndex = 1

    def loadPage(self):
        self.url = 'http://stu-cn.de/forumdisplay.php?fid=14&page='+str(self.pageIndex)
        request = urllib2.Request(self.url)
        response = urllib2.urlopen(request)
        content = response.read()
        pattern = re.compile('a href="viewthread.*?page%3D.">(.*?)</a></span>',re.S)
        items = re.findall(pattern,content)
        for item in items:
            print item

    def start(self):
        for i in range(1,5):
            self.pageIndex = i
            self.loadPage()

spider = HScw()
spider.start()