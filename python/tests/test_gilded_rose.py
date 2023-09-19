# -*- coding: utf-8 -*-
import unittest

import pytest

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


class BackstagePassesTest(unittest.TestCase):

    def test_backstage_passes_increase_in_quality_by_one_more_than_10_days_before_concert(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=33)
        gilded_rose = GildedRose([backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(34, backstage_passes.quality)

    @unittest.skip(reason='Test list')
    def test_backstage_passes_increase_in_quality_by_two_exactly_10_days_before_concert(self):
        pass

    @unittest.skip(reason='Test list')
    def test_backstage_passes_increase_in_quality_by_two_less_than_10_days_but_more_than_5_days_before_concert(self):
        pass


if __name__ == "__main__":
    unittest.main()
