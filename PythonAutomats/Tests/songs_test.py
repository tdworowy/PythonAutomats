import unittest

from Songs.last_fm_parser import clear_titles


class TestSongs(unittest.TestCase):
    """Unit tests for 'songs' functions"""

    def test_clear_titles(self):
        """Test clear_titles - correct data."""
        titles = [
            'title="King Diamond — Give Me Your Soul"',
            "title='King Diamond — Give Me Your Soul'",
        ]
        clean_titles = [
            "King Diamond - Give Me Your Soul\n",
            "King Diamond - Give Me Your Soul\n",
        ]

        self.assertEquals(clear_titles(titles), clean_titles)


if __name__ == "__main__":
    unittest.main()
