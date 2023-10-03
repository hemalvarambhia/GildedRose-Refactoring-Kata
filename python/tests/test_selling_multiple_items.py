# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import GildedRose, Item


class SellingMultipleItemsTest(unittest.TestCase):

    def test_selling_more_than_one_item(self):
        aged_brie = Item(name='Aged Brie', quality=11, sell_in=25)
        sulfuras = Item(name='Sulfuras, Hand of Ragnaros', quality=32, sell_in=11)
        normal_item = Item(name='Normal Item', quality=2, sell_in=5)
        gilded_rose = GildedRose([aged_brie, sulfuras, normal_item])

        gilded_rose.update_quality()

        self.assertEqual(32, sulfuras.quality)
        self.assertEqual(12, aged_brie.quality)
        self.assertEqual(1, normal_item.quality)

    @unittest.skip(reason='Test list')
    def test_selling_no_items(self):
        pass