from bs4 import BeautifulSoup  

class Book:
    def __init__(self, book_html):
        self.title = None
        self.md5 = None
        self.author = None
        self.language = None
        self.size = None
        self.filename = None
        self.display_title = None
        self.display_author = None
        self.filepath = None
        self.parse_html(book_html)
        
    def parse_html(self, book_html):
        title = book_html.find('h3').string
        self.title = title.replace(":", " -")
        link = book_html.find('a')["href"]
        self.md5 = link.split("/")[2]
        self.author = book_html.find("div", class_="max-lg:line-clamp-[2] lg:truncate leading-[1.2] lg:leading-[1.35] max-lg:text-sm italic").string
        metadata = book_html.find("div", class_="line-clamp-[2] leading-[1.2] text-[10px] lg:text-xs text-gray-500").string
        split_metadata = metadata.split(",")
        self.language = split_metadata[0]
        self.size = split_metadata[2].strip()
        self.genre = split_metadata[3].split("(")[1].split(")")[0]
    
    def print_metadata(self):
        return f"{self.display_title} / {self.display_author} / {self.size}"