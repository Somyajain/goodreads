import requests
import bs4




class goodreads(author,num):
    def _init_(self,author):
        self.name=author
        

    def books():
        #function for top 10
        url=requests.get('https://www.goodreads.com/author/list/'+author+'?page=1&per_page=10')
	soup=bs4.BeautifulSoup(url.content)
        
        ten_books=soup.find_all('div',{'class':'bookTitle'})
	list_of_tenbooks=[]
	for e in ten_books:
		
		pos=e.find('-')
		list_of_tenbooks.append(e[:pos])

	print 'Top 10 books :',list_of_tenbooks
    def all_books(self,author):
        #function for top 10
        url=requests.get('https://www.goodreads.com/author/list/'+author+'?page=1&per_page=1000')
        soup=bs4.BeautifulSoup(url.content)
        
        all_books=soup.find_all('div',{'class':'bookTitle'})
	list_of_books=[]	
	for e in all_books:
		
		pos=e.find('-')
		list_of_books.append(e[:pos])
	print 'All books:',list_of_books
    
    def quotes(self,num):
        url=requests.get('http://www.goodreads.com/author/quotes/'+ author+'?page=1&per_page=1000')
        soup=bs4.BeautifulSoup(url.content)
        all_quotes=soup.find_all('div',{'class':'quoteText'})
	list_of_quotes=[]	
	for e in all_quotes:
		
		pos=e.find('-')
		list_of_quotes.append(e[:pos])
	print 'All quotes',list_of_quotes
    def read_quotes(n):
	fo=open('quotes.txt','wb+')
	
    

        
