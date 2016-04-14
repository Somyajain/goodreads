import requests
from bs4 import BeautifulSoup as bs
class Goodreads():
    def __init__(self,author):
        self.author=""
        for i in author.split(" "):
            self.author=self.author+"+"+i
#getting the author url here
        search_url =requests.get("https://www.goodreads.com/search?q="+self.author+"&search[source]=goodreads&search_type=books&tab=books")
        search_soup=bs(search_url.content,"lxml")
        search_class=search_soup.find("a",class_="authorName")
        self.author_page=search_class.get("href")
        self.author_id=""
        count=0
        for i in self.author_page:
            if i == "/" or i == "?":
                count=count+1
            if count==5:
                self.author_id+=i
        self.author_id=self.author_id[1:len(self.author_id)]
    def books(self):
        #function for top 10
        url=requests.get('https://www.goodreads.com/author/list/'+self.author_id+'?page=1&per_page=10')
        soup=bs(url.content)
        ten_books=soup.find_all('div',{'class':'bookTitle'})
        list_of_tenbooks=[]
        for e in ten_books:
            pos=e.find('-')
            list_of_tenbooks.append(e[:pos])
        print 'Top 10 books :',list_of_tenbooks

    def all_books(self):
        #function for top 10
        url=requests.get('https://www.goodreads.com/author/list/'+self.author_id+'?page=1&per_page=1000')
        soup=bs(url.content)
        all_books=soup.find_all('div',{'class':'bookTitle'})
        list_of_books=[]
        for e in all_books:
            pos=e.find('-')
            list_of_books.append(e[:pos])
        print 'All books:',list_of_books

    def quotes(self):
        url=requests.get('http://www.goodreads.com/author/quotes/'+ self.author_id+'?page=1&per_page=1000')
        soup=bs(url.content)
        all_quotes=soup.find_all('div',{'class':'quoteText'})
        list_of_quotes=[]
        for e in all_quotes:
            pos=e.find('-')
            list_of_quotes.append(e[:pos])
        print 'All quotes',list_of_quotes

    def read_quotes(self,n):
        fo=open('quotes.txt','wb+')
