# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from konlpy.tag import Hannanum
from collections import Counter
import urllib.request
import re

class GetPage:
    def __init__(self, target):
        request = urllib.request.urlopen(target)
        self.rawDoc = request.read()
        self.soup = BeautifulSoup(request, 'html.parser')
        self.writerList_ = list()
        # self.title = str()
        # self.date = str()
        self.paragraphList_ = list()
        # self.articleDict_ = dict()

    @property
    def Article(self):
        # doc = self.soup.findAll(class_="smartOutput body_font")
        # startPos = doc[0].find('>')
        # endPos = doc[0].find('</')
        # doc = doc[0][startPos:endPos]
        return self.soup.findAll(class_="smartOutput body_font")

    @property
    def WriterList(self):
        # Get ResultSet
        corpus = self.soup.findAll(class_ = "head_writer_fullname")
        result = corpus[0]

        # Prefare substract name
        pattern = re.compile('\S*\S')

        # Append writers to list
        for i in result:
            t = pattern.findall(i.getText())[0]
            self.writerList_.append(t)

        return self.writerList_

    @property
    def title(self):
        return 0

    @property
    def ParagraphList(self):
        # Get ResultSet
        page = self.soup.find(class_="smartOutput body_font")

        # change to str
        # Split with \n
        # Remove \r
        self.paragraphList_ = page.getText().split(sep='\n')
        self.paragraphList_ = [x for x in self.paragraphList_ if x != '\r']
        self.paragraphList_ = [x.strip() for x in self.paragraphList_]

        return self.paragraphList_

def WordCount(corpus):
    h = Hannanum()
    nouns = h.nouns(corpus)
    frequency = Counter(nouns)
    return frequency



if __name__ == '__main__':

    target = "http://m.pressian.com/m/m_article.html?no=138940"
    # target = "test.html"

    k = GetPage(target)

    print(k.WriterList)
    # k.ParagraphList
    print(k.Article)
    print(type(k.Article))

    # print(WordCount(k.soup.find(class_ = "smartOutput body_font")))

    #for corpus in k.ParagraphList[0:3]:
    #    print(WordCount(corpus))
