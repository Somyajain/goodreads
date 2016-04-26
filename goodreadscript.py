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
        soup=bs(url.content,'lxml')
	ten_books=soup.find_all('a',{'class':'bookTitle'})
	list_of_tenbooks=[]
	for e in ten_books:
		list_of_tenbooks.append(e.get_text().encode('utf-8'))
	print list_of_tenbooks

	print 'Top 10 books :'
	for m in list_of_tenbooks:
		print m
		print '\n'

    def all_books(self):
        #function for top 10
        url=requests.get('https://www.goodreads.com/author/list/'+self.author_id+'?page=1&per_page=1000')
        soup=bs(url.content,'lxml')
        all_books=soup.find_all('a',{'class':'bookTitle'})
        list_of_books=[]

        for e in all_books:


		list_of_books.append((e.get_text()).encode('utf-8'))

	print list_of_books[0]
	print len(list_of_books)

    def quotes(self):
        url=requests.get('http://www.goodreads.com/author/quotes/'+ self.author_id+'?page=1&per_page=1000')
        soup=bs(url.content,'lxml')
        all_quotes=soup.find_all('div',{'class':'quoteText'})
	self.list_of_quotes=[]
	for e in all_quotes:
		self.list_of_quotes.append(e.get_text().encode('utf-8'))
	print self.list_of_quotes[1]
	print len(self.list_of_quotes)
    
    def write_quotes(self,n):
	self.quotes()
	print n	
	string=''
	print self.author
	count=0
	while count<n:
		string=string+self.list_of_quotes[count]+'\n'
		print 'here', n
		count+=1
	fo=open('quotes'+ str(self.author)+'.txt','wb+')
	fo.write(string)
	fo.close()
        
