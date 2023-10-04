# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == 'Sulfuras, Hand of Ragnaros':
                continue

            if item.name == "Aged Brie":
                item.quality = self.__increase_quality_of__(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = self.__increase_quality_of__(item)
                if item.sell_in < 11:
                    item.quality = self.__increase_quality_of__(item)
                if item.sell_in < 6:
                    item.quality = self.__increase_quality_of__(item)
            else:
                item.quality = self.__reduce_quality_of(item)
            item.sell_in = item.sell_in - 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 0:
                    item.quality = 0
            elif item.name == "Aged Brie":
                if item.sell_in < 0:
                    item.quality = self.__increase_quality_of__(item)
            else:
                if item.sell_in < 0:
                    item.quality = self.__reduce_quality_of(item)

    def __reduce_quality_of(self, item):
        if item.quality > 0:
            return item.quality - 1
        else:
            return item.quality

    def __increase_quality_of__(self, item):
        if item.quality < 50:
            return item.quality + 1
        else:
            return item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
