# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import Item, GildedRose


class NormalItemsTest(unittest.TestCase):

    def test_normal_item_can_be_sold(self):
        normal_item = Item(name='Any normal item', sell_in=13, quality=5)
        gilded_rose = GildedRose([normal_item])

        gilded_rose.update_quality()

        self.assertEqual(12, normal_item.sell_in)

    def test_normal_item_quality_that_has_not_reached_its_sell_by_date_decreases_by_1(self):
        normal_item = Item(name='Any normal item', sell_in=13, quality=5)
        gilded_rose = GildedRose([normal_item])

        gilded_rose.update_quality()

        self.assertEqual(4, normal_item.quality)

    def test_normal_item_quality_that_has_reached_its_sell_by_date_decreases_twice_as_fast(self):
        normal_item = Item(name='Any normal item', sell_in=0, quality=9)
        gilded_rose = GildedRose([normal_item])

        gilded_rose.update_quality()

        self.assertEqual(7, normal_item.quality)

    def test_normal_item_quality_that_has_passed_its_sell_by_date_decreases_twice_as_fast(self):
        normal_item = Item(name='Any normal item', sell_in=-1, quality=14)
        gilded_rose = GildedRose([normal_item])

        gilded_rose.update_quality()

        self.assertEqual(12, normal_item.quality)


if __name__ == "__main__":
    unittest.main()
