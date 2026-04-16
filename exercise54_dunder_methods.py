# Magic methods - dunder(double underscore) __init__, __str__, __eq__ ,etc
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behaviour of objects

class Book:
    def __init__(self, title,author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    # equals
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    #less than
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    # greater than
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):
        if(key=='title'): return self.title
        elif(key=='author'): return self.author
        elif(key=='num_pages'): return self.num_pages
        else: return f"'{key}' was not found"


book1 = Book("The Hobbit", "JRR Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "JK Rowling", 223)
book3 = Book("Dune", "Frank Herbert", 398)
book4 = Book("The Hobbit", "JRR Tolkien", 301)


# priting book1 directly gives memory addreses (like in java, priting an object without defining toString)
print(book1)

print(book1==book4)

print(book1>book3) #returns False as book1 does not have more pages than book3
print(book2<book1) #returns True as book2 has less pages than book1

print(book1+ book2)

print("rowling" in book2)

print(book3["author"])
print(book2['num_pages'])
print(book1['audio'])