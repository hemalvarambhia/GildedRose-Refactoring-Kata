# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            match item.name:
                case 'Sulfuras, Hand of Ragnaros':
                    self.__update_sulfuras__(item)
                case 'Aged Brie':
                    self.__update_aged_brie__(item)
                case 'Backstage passes to a TAFKAL80ETC concert':
                    self.__update_backstage_passes__(item)
                case _:
                    self.__update_normal_items__(item)

    def __update_sulfuras__(self, item):
        change = 0
        item.quality = min(80, max(0, item.quality + change))

    def __update_normal_items__(self, item):
        item.sell_in = item.sell_in - 1
        change = self.__normal_item_change_in_quality__(item)

        item.quality = min(50, max(0, item.quality + change))

    def __normal_item_change_in_quality__(self, item):
        if item.sell_in > 0:
            return -1
        else:
            return -2

    def __update_backstage_passes__(self, item):
        change = self.__back_stage_passes_change_in_quality__(item)
        item.sell_in = item.sell_in - 1
        item.quality = min(50, max(0, item.quality + change))

    def __back_stage_passes_change_in_quality__(self, item):
        if item.sell_in > 10:
            return 1
        elif item.sell_in in range(6, 11):
            return 2
        elif item.sell_in in range(1, 6):
            return 3
        if item.sell_in <= 0:
            return -item.quality

    def __update_aged_brie__(self, item):
        change = 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            change = 2

        item.quality = min(50, max(0, item.quality + change))


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
