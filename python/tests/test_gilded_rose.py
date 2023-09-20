# -*- coding: utf-8 -*-
import unittest


from src.gilded_rose import Item, GildedRose


class BackstagePassesTest(unittest.TestCase):
    def test_backstage_passes_increase_in_quality_by_one_more_than_10_days_before_concert(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=33)
        gilded_rose = GildedRose([backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(34, backstage_passes.quality)

    def test_backstage_passes_increase_in_quality_by_two_exactly_10_days_before_concert(self):
        backstage_passes = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=21)
        gilded_rose = GildedRose([backstage_passes])

        gilded_rose.update_quality()

        self.assertEqual(23, backstage_passes.quality)

    @unittest.skip(reason="Test list")
    def test_backstage_passes_increase_in_quality_by_two_less_than_10_days_but_more_than_5_days_before_concert(self):
        pass


if __name__ == "__main__":
    unittest.main()
