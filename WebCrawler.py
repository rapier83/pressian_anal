# -*- coding: utf-8 -*-

import bs4
from konlpy.tag import Hannanum
from collections import Counter
import urllib.request
import re

class GetPage:
    def __init__(self, target):
        request = urllib.request.urlopen(target)
        self.rawDoc = urllib.request.urlopen(target).read()
        self.soup = bs4.BeautifulSoup(urllib.request.urlopen(target), 'html.parser')
        self.writerList_ = list()
        # self.title = str()
        # self.date = str()
        self.paragraphList_ = list()
        # self.articleDict_ = dict()

    @property
    def Article(self):
        doc = self.soup.find(class_="smartOutput body_font").getText()

        return self.soup.find(class_="smartOutput body_font").getText()

    @property
    def ParagraphList(self):
        # Get ResultSet
        page = self.soup.find(class_="smartOutput body_font")

        # change to str
        # Split with \n
        # Remove \r
        self.paragraphList_ = page.getText().split(sep='\xa0')
        self.paragraphList_ = [x for x in self.paragraphList_ if x != '\r' or x != '']
        self.paragraphList_ = [x.strip('\xa0') for x in self.paragraphList_]
        self.paragraphList_ = [x.replace('\n', '') for x in self.paragraphList_]
        self.paragraphList_ = list(filter(('').__ne__, self.paragraphList_))
        return self.paragraphList_

    @property
    def WriterList(self):
        # Get ResultSet

        corpus = list(self.soup.findChildren(attrs = "head_writer_fullname"))
        pattern = re.compile('\S*\S')
        for e in corpus:
            appendee = pattern.findall(e.getText())[0]
            # print(appendee)
            self.writerList_.append(appendee)
        return self.writerList_

    @property
    def title(self):
        return 0



def WordCount(corpus):
    h = Hannanum()
    nouns = h.nouns(corpus)
    frequency = Counter(nouns)
    return frequency

if __name__ == '__main__':

    target = "http://m.pressian.com/m/m_article.html?no=138940"
    target2 = "http://m.pressian.com/m/m_article.html?no=138936"
    target3 = "http://m.pressian.com/m/m_article.html?no=139075"
    targetFile = "test.html"

    k = GetPage(target2)

    # print(k.ParagraphList)
    print(k.Article)
    print(type(k.Article))
    print(WordCount(k.Article))

    # print(WordCount(k.soup.find(class_ = "smartOutput body_font")))

    #for corpus in k.ParagraphList:
    #    print(WordCount(corpus))