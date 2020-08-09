import copy


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError("Incorrect object identifier:{}".format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def test_prototype():
    from prototype_pattern import book

    b1 = book.Book(
        "The C Programming Language",
        ("Brian W. Kernighan", "Dennis M.Ritchie"),
        price=118,
        publisher="Prentice Hall",
        length=228,
        publication_date="1978-02-22",
        tags=("C", "programming", "algorithms", "data structures"),
    )

    prototype = Prototype()
    cid = "k&r-first"
    prototype.register(cid, b1)
    b2 = prototype.clone(
        cid,
        name="The C Programming Language(ANSI)",
        price=48.99,
        length=274,
        publication_date="1988-04-01",
        edition=2,
    )
    for i in (b1, b2):
        print(i)
        print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))
