import requests as r
import re
class web_scrap:
    seed=""
    result=""
    tag_attr=[]
    
    def __init__(self,seed,tag,attr):
          self.seed=seed
          self.set_tag(tag)
          self.set_attr(attr)
          self.fetch_web()
          self.extract_tags()
          self.print_result()            


    def fetch_web(self):
        self.result=r.get(self.seed)
        
    def set_tag(self,tag):
        self.re_tag=r"(<"+tag+r" [^>]+>)"

    def set_attr(self,attr):
        self.re_attr_parser=r"("+attr+r")\=\"([^\"]+)\""

    def extract_tags(self):
            tags=re.findall(self.re_tag,self.result.text)
            for i in tags:
                self.attr_parser(i)

    def attr_parser(self,tag):
        attributes=re.findall(self.re_attr_parser,tag)
        for data in attributes:
            temp={}
            temp["attr_name"]=data[0];
            temp["attr_value"]=data[1];
            self.tag_attr.append(temp)
            
    def print_result(self):
            for i in self.tag_attr:
                print(i["attr_name"] ,"-->",i["attr_value"])
        
        
    
     
print("\t HELLO WELCOME TO EMAIL SCRAPPER")

scrap=web_scrap(input("enter the link \t"),input("enter the tag to scrap \t"),input("enter the attribute to scrap \t"))
