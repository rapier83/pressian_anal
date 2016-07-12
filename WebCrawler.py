# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import re

target = "http://m.pressian.com/m/m_article.html?no=138940"


class GetPage:
    def __init__(self, target):
        self.target = target
        htmlDocument = urllib.request.urlopen(target)
        self.soup = BeautifulSoup(htmlDocument, 'html.parser')
        self.writerList_ = list()

    def GetWriter(self):
        # Get ResultSet
        writer = self.soup.find_all(class_="head_writer_fullname")

        # Prefare substract name
        pattern = re.compile('\S*\S')

        for i in writer:
            t = pattern.findall(i.getText())[0]
            self.writerList_.append(t)
        return self.writerList_


k = GetPage(target)
print(k.GetWriter())
