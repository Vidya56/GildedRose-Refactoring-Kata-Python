import sys
import unittest
sys.path.append('..')
from gilded_rose_refactored import *


class TestGildedRose(unittest.TestCase):

    def setUp(self):
        self.gilded_rose = GildedRose([])

    def test_normal_item(self):
        items = [Item(name="Normal Item", sell_in=10, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_after_sell_date(self):
        items = [Item(name="Normal Item", sell_in=0, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 18)

    def test_aged_brie_increases_in_quality(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)

    def test_aged_brie_quality_does_not_exceed_50(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=50)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_does_not_change(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 80)

    def test_backstage_passes_increase_in_quality(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 14)
        self.assertEqual(items[0].quality, 21)

    def test_backstage_passes_increase_in_quality_by_2_when_10_days_or_less(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 22)

    def test_backstage_passes_increase_in_quality_by_3_when_5_days_or_less(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 23)

    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item_decreases_in_quality_twice_as_fast(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 2)
        self.assertEqual(items[0].quality, 4)

    def test_conjured_item_decreases_in_quality_twice_as_fast_after_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 2)

    def test_quality_never_negative(self):
        items = [Item(name="Normal Item", sell_in=10, quality=0)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_increases_in_quality_after_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 22)

    def test_backstage_passes_quality_at_various_sell_in_values(self):
        items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=20),
        ]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 21)  # Increment by 1 for sell_in > 10
        self.assertEqual(items[1].quality, 22)  # Increment by 2 for 5 < sell_in <= 10
        self.assertEqual(items[2].quality, 22)  # Increment by 2 for 5 < sell_in <= 10
        self.assertEqual(items[3].quality, 23)  # Increment by 3 for 0 < sell_in <= 5
        self.assertEqual(items[4].quality, 23)  # Increment by 3 for sell_in == 0

    def test_sulfuras_negative_sell_in(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 80)

    def test_normal_item_quality_decreases_over_time(self):
        items = [Item(name="Normal Item", sell_in=5, quality=10)]
        self.gilded_rose.items = items
        for _ in range(5):
            self.gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 5)

    def test_conjured_item_with_high_initial_quality(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=50)]
        self.gilded_rose.items = items
        for _ in range(2):
            self.gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 46)

    def test_items_with_quality_of_zero(self):
        items = [
            Item(name="Normal Item", sell_in=5, quality=0),
            Item(name="Conjured Mana Cake", sell_in=5, quality=0),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=0)
        ]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 0)
        self.assertEqual(items[2].quality, 3)  # Backstage pass increases in quality


if __name__ == '__main__':
    unittest.main()
