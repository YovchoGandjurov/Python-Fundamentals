import re
class Book:
    def __init__(self, title, author, chapter, price):
        self.title = title
        self.author = author
        self.chapter = chapter
        self.price = float(price)

data = input()
book_storage = []

while data != "on work":
    data = data.split(" -> ")
    book_info = data[0].split()
    chapter = data[1].split(", ")

    if len(book_info) == 3:
        price = book_info[2]
        if price.replace(".", "").isdigit():
            
            if float(book_info[2]) > 0:
                price = float(book_info[2])
            

        if type(book_info[0]) == str and type(book_info[1]) == str and type(price) == float and type(chapter) == list:
            valid_book = Book(book_info[0], book_info[1], chapter, book_info[2])
            book_storage.append(valid_book)
    
    data = input()


book = input()
sold_books = []
not_found_books = 0

while book != "end work":
    flag = 0
    for i in book_storage:
        if i.title == book:
            sold_books.append(i)
            #book_storage.remove(i)
            flag = 1
    if flag == 0:
        not_found_books += 1 
    book = input()


for x in range(not_found_books):
    print("No such book here")

if len(sold_books) == 0:
    print("Bad day :(")
else:
    for item in sold_books:
        print(f"SOLD: {item.title} with author {item.author}. Chapters in the book {len(item.chapter)}")
    print(f"Money: {sum([x.price for x in sold_books]):.2f}")