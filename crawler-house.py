import urllib2
import re

page = 1
url = 'http://stu-cn.de/forumdisplay.php?fid=14&page='+str(page)
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    #print response.read()
    content = response.read()
    pattern = re.compile('a href="viewthread.*?page%3D1">(.*?)</a></span>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code