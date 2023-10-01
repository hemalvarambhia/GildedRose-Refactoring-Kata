# -*- coding: utf-8 -*-
import unittest

from src.gilded_rose import GildedRose, Item


class SulfurasItemsTest(unittest.TestCase):


    def test_sulfuras_cannot_be_sold(self):
        sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=23)
        gilded_rose = GildedRose([sulfuras])

        gilded_rose.update_quality()

        self.assertEqual(0, sulfuras.sell_in)


    def test_sulfuras_does_not_change_in_quality(self):
        sulfuras = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=1)
        gilded_rose = GildedRose([sulfuras])

        gilded_rose.update_quality()

        self.assertEqual(1, sulfuras.quality)