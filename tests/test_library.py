import unittest
from src.library import Library


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


if __name__ == "__main__":
    unittest.main()
