import sys
import unittest
sys.path.append('..')
from gilded_rose_refactored import *


# Unit test class for GildedRose application
class TestGildedRose(unittest.TestCase):

    # Set up the GildedRose instance before each test
    def setUp(self):
        self.gilded_rose = GildedRose([])

    # Test case for normal items decreasing in quality and sell_in
    def test_normal_item(self):
        items = [Item(name="Normal Item", sell_in=10, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that sell_in is decreased by 1 and quality by 1
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

    # Test case for normal items after sell date, quality decreases twice as fast
    def test_normal_item_after_sell_date(self):
        items = [Item(name="Normal Item", sell_in=0, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that sell_in is decreased by 1 and quality by 2 after sell date
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 18)

    # Test case for Aged Brie increasing in quality as it ages
    def test_aged_brie_increases_in_quality(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that sell_in is decreased by 1 and quality is increased by 1
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)

    # Test case to ensure Aged Brie quality never exceeds 50
    def test_aged_brie_quality_does_not_exceed_50(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=50)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality does not exceed the maximum of 50
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 50)

    # Test case to ensure Sulfuras item does not change in quality or sell_in
    def test_sulfuras_does_not_change(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that both sell_in and quality remain unchanged
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 80)

    # Test case for Backstage passes increasing in quality as sell_in decreases
    def test_backstage_passes_increase_in_quality(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that sell_in is decreased by 1 and quality is increased by 1
        self.assertEqual(items[0].sell_in, 14)
        self.assertEqual(items[0].quality, 21)

    # Test case for Backstage passes increasing in quality by 2 when sell_in is 10 days or less
    def test_backstage_passes_increase_in_quality_by_2_when_10_days_or_less(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality is increased by 2 as sell_in is 10 or less
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 22)

    # Test case for Backstage passes increasing in quality by 3 when sell_in is 5 days or less
    def test_backstage_passes_increase_in_quality_by_3_when_5_days_or_less(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality is increased by 3 as sell_in is 5 or less
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 23)

    # Test case for Backstage passes dropping to 0 quality after concert date
    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality drops to 0 after sell_in reaches 0
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)

    # Test case for Conjured items decreasing in quality twice as fast
    def test_conjured_item_decreases_in_quality_twice_as_fast(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality decreases by 2 for Conjured items
        self.assertEqual(items[0].sell_in, 2)
        self.assertEqual(items[0].quality, 4)

    # Test case for Conjured items decreasing in quality twice as fast after sell date
    def test_conjured_item_decreases_in_quality_twice_as_fast_after_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=6)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality decreases by 4 for Conjured items after sell date
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 2)

    # Test case to ensure quality never goes negative
    def test_quality_never_negative(self):
        items = [Item(name="Normal Item", sell_in=10, quality=0)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality does not drop below 0
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 0)

    # Test case for Aged Brie increasing in quality after sell date
    def test_aged_brie_increases_in_quality_after_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=20)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that quality increases by 2 after sell date
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 22)

    # Test case for Backstage passes quality at various sell_in values
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

        # Assert quality based on different sell_in values
        self.assertEqual(items[0].quality, 21)  # Increment by 1 for sell_in > 10
        self.assertEqual(items[1].quality, 22)  # Increment by 2 for 5 < sell_in <= 10
        self.assertEqual(items[2].quality, 22)  # Increment by 2 for 5 < sell_in <= 10
        self.assertEqual(items[3].quality, 23)  # Increment by 3 for 0 < sell_in <= 5
        self.assertEqual(items[4].quality, 23)  # Increment by 3 for sell_in == 0

    # Test case to ensure Sulfuras does not change even with negative sell_in
    def test_sulfuras_negative_sell_in(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that Sulfuras quality and sell_in remain unchanged even with negative sell_in
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 80)

    # Test case to check normal item quality decreases over time
    def test_normal_item_quality_decreases_over_time(self):
        items = [Item(name="Normal Item", sell_in=5, quality=10)]
        self.gilded_rose.items = items
        for _ in range(5):
            self.gilded_rose.update_quality()

        # Assert that quality decreases by 1 each day until sell_in reaches 0
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 5)

    # Test case for Conjured items with high initial quality
    def test_conjured_item_with_high_initial_quality(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=50)]
        self.gilded_rose.items = items
        for _ in range(2):
            self.gilded_rose.update_quality()

        # Assert that quality decreases twice as fast, with a decrease of 4 over 2 days
        self.assertEqual(items[0].quality, 46)

    # Test case to check items with an initial quality of zero
    def test_items_with_quality_of_zero(self):
        items = [
            Item(name="Normal Item", sell_in=5, quality=0),
            Item(name="Conjured Mana Cake", sell_in=5, quality=0),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=0)
        ]
        self.gilded_rose.items = items
        self.gilded_rose.update_quality()

        # Assert that normal and conjured items maintain a quality of 0, while Backstage Pass increases in quality
        self.assertEqual(items[0].quality, 0)
        self.assertEqual(items[1].quality, 0)
        self.assertEqual(items[2].quality, 3)  # Backstage pass increases in quality


if __name__ == '__main__':
    unittest.main()
