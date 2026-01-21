class Library:
    def __init__(self):
        # Dictionary to store book details
        self.books = {}

    # -------- Sprint 1 --------
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Duplicate Book ID")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "status": "Available"
        }

    # -------- Sprint 2 --------
    def borrow_book(self, book_id):
        if self.books[book_id]["status"] == "Borrowed":
            raise ValueError("Book already borrowed")
        self.books[book_id]["status"] = "Borrowed"

    def return_book(self, book_id):
        self.books[book_id]["status"] = "Available"

    # -------- Sprint 3 --------
    def generate_report(self):
        report = "BookID | Title | Author | Status\n"
        for book_id, data in self.books.items():
            report += (
                f"{book_id} | "
                f"{data['title']} | "
                f"{data['author']} | "
                f"{data['status']}\n"
            )
        return report
