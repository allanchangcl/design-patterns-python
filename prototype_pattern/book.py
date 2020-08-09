from collections import OrderedDict


class Book:
    def __init__(self, name, authors, price, **rest):
        """Examples of rest: publisher, length, tags, publication date"""
        self.name = name
        self.authors = authors
        self.price = price
        # in US dollars
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append("{}: {}".format(i, ordered[i]))
            if i == "price":
                mylist.append("$")
            mylist.append("\n")
        return "".join(mylist)


def test_book():
    book = Book("48 Laws", "Book", 120)
    # assert type(builder) is object
    # print(str(book))
    assert isinstance(book, Book)
