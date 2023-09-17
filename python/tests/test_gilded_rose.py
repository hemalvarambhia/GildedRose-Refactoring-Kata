# -*- coding: utf-8 -*-
import unittest

import pytest

from src.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_aged_brie_before_expiry_date_increases_in_quality_by_1(self):
        items = [Item("Aged Brie", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(11, items[0].quality)

    def test_aged_brie_that_has_reached_expiry_date_increases_in_quality_by_2(self):
        items = [Item("Aged Brie", sell_in=0, quality=11)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(13, items[0].quality)

    @pytest.mark.skip('Test list')
    def test_aged_brie_that_past_its_sell_by_date_increases_in_quality_by_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
