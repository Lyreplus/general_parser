import feedparser
import time
from os import system
from bs4 import BeautifulSoup
rss = feedparser.parse("https://jobs.fbk.eu/Annunci/Feed.xml") #your newspaper's rss

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + 'Hello World !' + color.END)

print("Number of  RSS post: ", len(rss.entries))

for n in enumerate(rss.entries): #enumerate returns a tuple with the index and the value, example: (0, <entry 1>)

    print(n[0])
    print(color.BOLD + "Title: " + rss.entries[n[0]].title + color.END + "\n")
    print(n[1].link)
    print(n[1].published)
    htmlify = n[1].summary
    soup = BeautifulSoup(htmlify, 'html.parser')

    # remove the script and style elements
    for script in soup(["script", "style"]):
        script.extract()

    # extract the text
    text = soup.get_text()

    print(text)
    print("\n")

print("\n\n------------")