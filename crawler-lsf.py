import urllib
import urllib2
import cookielib
import re

class uslsf:
    def __init__(self):
        self.loginUrl = 'https://lsf.uni-stuttgart.de/qisserver/rds?state=user&type' \
                        '=1&category=auth.login&startpage=portal.vm'

        # note! I have replaced info with xxxxxxx in the following link
        self.examUrl = 'https://lsf.uni-stuttgart.de/qisserver/rds?state=verpublish&' \
                       'status=init&publishid=xxxxxxx&moduleCall=pruefungenStudenten&' \
                       'publishConfFile=pruefungen&publishSubDir=listen'
        self.coikies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'asdf':'stxxxxx',
            'fdsa':'mypassword',
            'submit':'Ok'
        })
        self.opner = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.coikies))

    def getPage(self):
        request = urllib2.Request(
            url= self.loginUrl,
            data=self.postdata
        )
        result = self.opner.open(request)
        content = self.opner.open(self.examUrl).read()

        #print content

        pattern = re.compile('mod_.*?td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
        items = re.findall(pattern,content)
        print "I have following exams to go"
        for item in items:
            print item[0]
            print item[1]

stuu = uslsf()
stuu.getPage()