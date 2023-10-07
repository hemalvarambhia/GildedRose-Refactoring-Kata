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
                    item.quality = self.__increase_quality_of__(item, 1)
                    item.sell_in = item.sell_in - 1
                    if item.sell_in < 0:
                        item.quality = self.__increase_quality_of__(item, 1)
                case 'Backstage passes to a TAFKAL80ETC concert':
                    item.quality = self.__increase_quality_of__(item, 1)
                    if item.sell_in < 11:
                        item.quality = self.__increase_quality_of__(item, 1)
                    if item.sell_in < 6:
                        item.quality = self.__increase_quality_of__(item, 1)
                    item.sell_in = item.sell_in - 1
                    if item.sell_in < 0:
                        item.quality = 0
                case _:
                    item.quality = self.__reduce_quality_of(item)
                    item.sell_in = item.sell_in - 1
                    if item.sell_in < 0:
                        item.quality = self.__reduce_quality_of(item)

    def __reduce_quality_of(self, item, by=1):
        if item.quality > 0:
            return item.quality - by
        else:
            return item.quality

    def __increase_quality_of__(self, item, by):
        if item.quality < 50:
            return item.quality + by
        else:
            return item.quality


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
