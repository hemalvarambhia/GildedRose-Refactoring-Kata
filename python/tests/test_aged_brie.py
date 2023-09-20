# -*- coding: utf-8 -*-
import unittest


from src.gilded_rose import Item, GildedRose


class AgedBrieTest(unittest.TestCase):
    def test_aged_brie_before_expiry_date_increases_in_quality_by_1(self):
        aged_brie = Item("Aged Brie", sell_in=5, quality=10)
        gilded_rose = GildedRose([aged_brie])

        gilded_rose.update_quality()

        self.assertEqual(11, aged_brie.quality)

    def test_aged_brie_that_has_reached_expiry_date_increases_in_quality_by_2(self):
        aged_brie = Item("Aged Brie", sell_in=0, quality=11)
        gilded_rose = GildedRose([aged_brie])

        gilded_rose.update_quality()

        self.assertEqual(13, aged_brie.quality)

    def test_aged_brie_that_past_its_sell_by_date_increases_in_quality_by_2(self):
        aged_brie = Item("Aged Brie", sell_in=-1, quality=11)
        gilded_rose = GildedRose([aged_brie])

        gilded_rose.update_quality()

        self.assertEqual(13, aged_brie.quality)

    def test_aged_bries_quality_does_not_exceed_50(self):
        aged_brie = Item("Aged Brie", sell_in=-1, quality=49)
        gilded_rose = GildedRose([aged_brie])

        gilded_rose.update_quality()

        self.assertEqual(50, aged_brie.quality)


if __name__ == '__main__':
    unittest.main()
