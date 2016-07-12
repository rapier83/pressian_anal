# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from konlpy.tag import Hannanum
import urllib.request
import re

class GetPage:
    def __init__(self, target):
        self.target = target
        htmlDocument = urllib.request.urlopen(target)
        self.soup = BeautifulSoup(htmlDocument, 'html.parser')
        self.writerList_ = list()
        self.articleDict_ = dict()

    def GetWriter(self):
        # Get ResultSet
        writer = self.soup.findAll(class_ = "head_writer_fullname")

        # Prefare substract name
        pattern = re.compile('\S*\S')

        for i in writer:
            t = pattern.findall(i.getText())[0]
            self.writerList_.append(t)
        return self.writerList_

#    def GetArticle(self):
#        article = self.soup.findAll(class_ = "cnt_view news_body_area")

#        doc =


class WordCount:
    def __init__(self, corpus):
        self.corpus = corpus



# target = "http://m.pressian.com/m/m_article.html?no=138940"
# k = GetPage(target)
# print(k.GetWriter())
