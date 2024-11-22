class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}")


class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}\nPages: {self.pages}")


class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        super().display_info()
        print(f"Journal: {self.journal}\nDOI: {self.doi}")


# File Handling
def save_info(filename, info):
    with open(filename, 'w') as file:
        for item in info:
            file.write(f"{item}\n")


def read_info(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


# Example Usage
book1 = Book("Python Programming", "John Doe", "Programming", 300)
article1 = Article("Data Analysis Techniques", "Jane Smith", "Data Journal", "doi:12345")

books_info = [f"Book: {book1.title}, {book1.author}, {book1.genre}, {book1.pages}"]
articles_info = [f"Article: {article1.title}, {article1.author}, {article1.journal}, {article1.doi}"]

save_info("library_info.txt", books_info + articles_info)
read_info("library_info.txt")
import csv

def save_book_to_csv(book, filename='books.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book.title, book.author, book.genre, book.pages])

def save_article_to_csv(article, filename='articles.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([article.title, article.author, article.journal, article.doi])

def read_books_from_csv(filename='books.csv'):
    books = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            title, author, genre, pages = row
            books.append(Book(title, author, genre, int(pages) if pages.isdigit() else None))
    return books
def read_articles_from_csv(filename='articles.csv'):
    articles = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            title, author, journal, doi = row
            articles.append(Article(title, author, journal, doi))
    return articles

