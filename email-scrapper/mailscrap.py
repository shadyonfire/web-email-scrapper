import requests as r
import re
class email_scrap:
     keywords=[]
     search_urls=[]
     trimmed_url=set()
     mails=set()
     def __init__(self,keywords):
          self.keywords=keywords

     #searching keyword with bing
     def search_keywords(self):
          link_pattern=r'href=[\'"]?([http][^\'" >]+)'
          print("searching")
          for key in self.keywords:
               search=r.get("https://www.bing.com/search?q="+key+"&&oq="+key)
               if search.status_code==200:
                    searched_links = re.findall(link_pattern, search.text)
                    for url in searched_links:
                         self.search_urls.append(url)
               else:
                    print("some error happened and http response is "+status.code)
          self.print_list("searched url",self.search_urls)
          
     #trimming the url
     def trim_url(self):
          trimming_pattern=r'(http[s]?://[0-9A-Za-z./-_%=&;]+)'
          print("trimming")
          for url in self.search_urls:
               print("\t",url)
               self.trimmed_url.update(re.findall(trimming_pattern, url))


     #scrapping
     def scrap(self):
          mail_pattern=r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
          print("scraping")
          for link in self.trimmed_urls:
               print("\t"+link)
               try:
                    search=r.get(link)
                    if search.status_code==200:
                              self.mails.update(re.findall(mail_pattern, search.text))
                    else:     
                              print("\t hell",search.status_code)
               except:
                    print("\t wrong url pattern or some error happend")

                    
     #printing mail
     def print_mails(self):
          self.print_list("\temails",self.mails)


     #printing list
     def print_list(self,name,data):
          print("printing",name)
          for i in data:
               print("\t",i)
               

print("HELLO WELCOME TO EMAIL SCRAPPER")
print("please enter the keywords and hit enter. and to search enter SCRAP")
keys=[]
while True:
     x=input()
     if x=="SCRAP" or x=="scrap" or x=="Scrap":
          break
     else:
          keys.append(x)
     
mail=email_scrap(keys)
mail.search_keywords()
mail.trim_url()
mail.scrap()
mail.print_mails()














               
