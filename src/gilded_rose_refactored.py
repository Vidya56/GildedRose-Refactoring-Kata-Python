import sys
import logging
from rules import load_rules


# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

class GildedRose:
    def __init__(self, items):
        self.items = items
        self.rules = load_rules()
        logging.debug(f"GildedRose initialized with {len(items)} items.")

    def update_quality(self):
        logging.info("Updating quality for all items.")
        for item in self.items:
            item_name = item.name
            if item_name in self.rules:
                logging.debug(f"Applying rules for {item_name}. Current state: {item}")
                self.rules[item_name].apply_rules(item)
            else:
                logging.debug(f"Applying normal item rules for {item_name}. Current state: {item}")
                self.rules["Normal Item"].apply_rules(item)
            logging.debug(f"Updated state: {item}")
