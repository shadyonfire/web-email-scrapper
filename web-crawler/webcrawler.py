import requests as r
import re
class web_scrap:
    seed=""
    result=""
    tag_attr=[]
    
    def __init__(self,seed):
          self.seed=seed
          self.set_tag()
          self.set_attr()
          self.fetch_web(self.seed)
          self.crawl()            


    def fetch_web(self,link):
        self.result=r.get(link)
        self.extract_tags()
        
    def set_tag(self):
        self.re_tag=r"(<a [^>]+>)"

    def set_attr(self):
        self.re_attr_parser=r"href\=\"([^\"]+)\""

    def extract_tags(self):
            title=re.findall(r"<title>([^<]+)</title>",self.result.text)
            if len(title)!=0:
                print(title[0])
            else:
                print("No Title")
            tags=re.findall(self.re_tag,self.result.text)
            for i in tags:
                self.attr_parser(i)

    def attr_parser(self,tag):
        attributes=re.findall(self.re_attr_parser,tag)
        for data in attributes:
            if data[0]=="/":
                if data[1]=="/":
                    self.tag_attr.append({data[1:]:0})
                else:
                    self.tag_attr.append({data:0})
            
    def crawl(self):
            for i in self.tag_attr:
                    link=list(i.keys())[0]
                    if(not i[link]):
                        print(link)
                        self.fetch_web(self.seed+link)
            
    
     
print("\t HELLO WELCOME TO EMAIL SCRAPPER")

scrap=web_scrap(input("enter the link \t"))
