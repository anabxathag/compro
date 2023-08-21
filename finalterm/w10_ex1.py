"""Week10 Example1"""
class bookstore:
    """sell online books"""
    def detail(self, title, asin, language, page):
        """attribute & method"""
        self.title = title
        self.asin = asin
        self.language = language
        self.page = page
        print("{}".format(self.title))
        print("ASIN = {}".format(self.asin))
        print("language = {}".format(self.language))
        print("Print length = {} pages".format(self.page))
obj_1 = bookstore()
obj_1.detail("E-book", "B098W8NP8", "Thai", 225)
print()
obj_2 = bookstore()
obj_2.detail("Audio_book", "B09BBK79VB", "English", 720)
print()
obj_3 = bookstore()
obj_3.detail("Paperback", "0981821332", "Malaysia", 550)
        