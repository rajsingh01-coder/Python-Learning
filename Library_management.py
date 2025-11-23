
books = []
for i in range(5):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    year = int(input("Enter year of publication: "))
    books.append({"Title": title, "Author": author, "Genre": genre, "Year": year})

genres = set(book["Genre"] for book in books)
print("Unique Genres:", genres)

authors = tuple(book["Author"] for book in books)
print("Authors:", authors)

print("Books published after 2010:")
for book in books:
    if book["Year"] > 2010:
        print(book)

remove_title = input("Enter the title of the book to remove: ")
books = [book for book in books if book["Title"] != remove_title]

print("Updated book list:")
for book in books:
    print(book) 

