# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_before_expiry_date(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(11, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
