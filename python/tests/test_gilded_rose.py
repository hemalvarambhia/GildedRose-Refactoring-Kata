# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import Item, GildedRose


class NormalItemsTest(unittest.TestCase):

    @unittest.skip(reason='Test list')
    def test_normal_item_quality_that_has_not_reached_its_sell_by_date_decreases_by_1(self):
        pass

    @unittest.skip(reason='Test list')
    def test_normal_item_quality_that_has_reached_its_sell_by_date_decreases_twice_as_fast(self):
        pass

    @unittest.skip(reason='Test list')
    def test_normal_item_quality_that_is_passed_its_sell_by_date_decreases_twice_as_fast(self):
        pass


if __name__ == "__main__":
    unittest.main()
