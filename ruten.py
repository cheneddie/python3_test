from urllib import request, parse
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.a_flag=True
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs:
            print(attrs)
            self.a_flag = True
    # def handle_data(self, data):
    #     if self.a_flag:
    #         print(data)
    #         self.titles.append(data)
    # def handle_endtag(self, tag):
    #     if tag == 'a':
    #         self.a_flag = False

# keyword = input("Please enter a search term.\n")
keyword = "iphone"
url = "https://find.ruten.com.tw/s/?q=" + keyword

data = {'kw':keyword}
data = parse.urlencode(data).encode()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

req = request.Request(url, headers=headers)
response = request.urlopen(req)

if response.getcode() == 200:
    charset = response.headers.get_content_charset()
    charset = charset if charset else 'utf-8'

    content = response.read().decode(charset)
    
else :
    print("Error")

parser=MyHTMLParser()
parser.feed(content)

