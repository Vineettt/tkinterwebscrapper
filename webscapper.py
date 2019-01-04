from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

class Webscrapper:
    def __init__(self, master):    
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        
        ttk.Label(self.frame_content, text = 'Enter A URL:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        self.entry_name = ttk.Entry(self.frame_content, width = 100)
        self.entry_name.grid(row = 2, column = 0, padx = 5)
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        url = self.entry_name.get();
        if not url:
            print('Please Enter A URL')
        else:
            agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
            try:
                raw_html = requests.get(url, headers=agent)
            except requests.exceptions.RequestException as e:
                print(e)
                sys.exit(1)
            html = BeautifulSoup(raw_html.text, 'html.parser')
            name = html.find_all("a", class_="ui large header left")
            rating = html.find_all("div", class_="rating-div")
            cost = html.find_all("div", class_="res-info-detail")
            href = html.find_all("a")
            if href:
                for x in href:
                    print('Href: {}'.format(x))
            else:
                print('Name: {}'.format(name[0].text))
                print('Rating: {}'.format(rating[0].text))
                print('Cost: {}'.format(cost[0].text))
            self.clear()
    
    def clear(self):
        self.entry_name.delete(0, 'end')

def main():            
    root = Tk()
    webscrapper = Webscrapper(root)
    root.mainloop()
    
if __name__ == "__main__": main()
