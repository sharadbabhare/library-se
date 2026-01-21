import unittest
from src.library import Library


# ---------------- SPRINT 1 TESTS ----------------
class TestSprint1(unittest.TestCase):

    def test_add_book_success(self):
        library = Library()
        library.add_book("B1", "Python Programming", "Guido van Rossum")
        self.assertIn("B1", library.books)

    def test_duplicate_book_id(self):
        library = Library()
        library.add_book("B1", "Python Programming", "Guido van Rossum")
        with self.assertRaises(ValueError):
            library.add_book("B1", "Java Programming", "James Gosling")


# ---------------- SPRINT 2 TESTS ----------------
class TestSprint2(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book("B1", "Python Programming", "Guido van Rossum")

    def test_borrow_book(self):
        self.library.borrow_book("B1")
        self.assertEqual(self.library.books["B1"]["status"], "Borrowed")

    def test_borrow_already_borrowed_book(self):
        self.library.borrow_book("B1")
        with self.assertRaises(ValueError):
            self.library.borrow_book("B1")

    def test_return_book(self):
        self.library.borrow_book("B1")
        self.library.return_book("B1")
        self.assertEqual(self.library.books["B1"]["status"], "Available")


if __name__ == "__main__":
    unittest.main()
