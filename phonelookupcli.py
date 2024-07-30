#AUTHOR:        Ru1722
#PROGRAM NAME:  phonelookupcli
#DESCRIPTION:   A CLI tool that shows spam risks of a phone number using python3
#VERSION:       1.0
#DEV NOTES:     I got it to sucessfully find some info from spamcalls.net. Figuring out how to display what city the number is from

from html.parser import HTMLParser  #Used to parse  
import requests                     #Used to 

w = int(input("Phone number: "))    #Using integers so a letter can't be used to search a phone number
n = str(w)                          #Converts to string so phone number can be searched

r = requests.get('https://spamcalls.net/en/search?q=%2B=' + n)

class MyHTMLParser(HTMLParser):
    #Code below looks for the lines Spam-Risk, Low and High
    def handle_data(self, data):
        spamRisk = data.find("Spam-Risk")
        lowRisk = data.find("Low")
        highRisk = data.find("High")

        if spamRisk == 0:
            print ("Found phone number")
        if lowRisk == 0:
            print ("Low risk")
        if highRisk == 0:
            print ("High risk")
                    
parser = MyHTMLParser()
parser.feed(r.text)
