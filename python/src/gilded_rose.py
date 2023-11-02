# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            match item.name:
                case 'Sulfuras, Hand of Ragnaros':
                    pass
                case 'Aged Brie':
                    change = self.__aged_brie_change_in_quality__(item)
                    item.quality = min(50, max(0, item.quality + change))
                    item.sell_in = item.sell_in - 1
                case 'Backstage passes to a TAFKAL80ETC concert':
                    change = self.__back_stage_passes_change_in_quality__(item)
                    item.quality = min(50, max(0, item.quality + change))
                    item.sell_in = item.sell_in - 1
                case _:
                    change = self.__normal_item_change_in_quality__(item)
                    item.quality = min(50, max(0, item.quality + change))
                    item.sell_in = item.sell_in - 1

    def __normal_item_change_in_quality__(self, item):
        if item.sell_in > 0:
            return -1
        else:
            return -2

    def __back_stage_passes_change_in_quality__(self, item):
        if item.sell_in > 10:
            return 1
        elif item.sell_in in range(6, 11):
            return 2
        elif item.sell_in in range(1, 6):
            return 3
        if item.sell_in <= 0:
            return -item.quality

    def __aged_brie_change_in_quality__(self, item):
        if item.sell_in > 0:
            return 1
        else:
            return 2


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
