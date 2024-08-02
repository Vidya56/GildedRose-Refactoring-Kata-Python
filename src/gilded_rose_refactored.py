import sys
import logging
from rules import load_rules

# Set up logging configuration to display debug and info level messages
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Item:
    '''
    Define the Item class representing items in the shop
    '''
    def __init__(self, name, sell_in, quality):
        self.name = name  # Name of the item
        self.sell_in = sell_in  # Number of days to sell the item
        self.quality = quality  # Quality of the item

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

class GildedRose:
    '''
    Define the GildedRose class to manage the collection of items
    '''
    def __init__(self, items):
        self.items = items  # List of items in the shop
        self.rules = load_rules()  # Load rules for item updates from external function
        logging.debug(f"GildedRose initialized with {len(items)} items.") 

    # Method to update the quality of all items based on rules
    def update_quality(self):
        logging.info("Updating quality for all items.") 
        for item in self.items:
            item_name = item.name
            if item_name in self.rules:
                # Apply specific rules if the item has defined rules
                logging.debug(f"Applying rules for {item_name}. Current state: {item}")
                self.rules[item_name].apply_rules(item)
            else:
                # Apply generic rules for normal items
                logging.debug(f"Applying normal item rules for {item_name}. Current state: {item}")
                self.rules["Normal Item"].apply_rules(item)
            logging.debug(f"Updated state: {item}") 
