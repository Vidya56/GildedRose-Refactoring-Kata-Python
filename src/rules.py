import logging
from utils import ActionEnum, ActionUnit, UpdateRule, UpdateRuleSet

# Set up logging configuration to display debug information
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to load rules for different items
def load_rules():
    logging.info("Loading rules for items")
    rules = {
        # Rules for "Aged Brie"
        "Aged Brie": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.INC, 1),  # Increase quality by 1 each day
            update_rules=[
                UpdateRule("item.sell_in < 0", ActionUnit(ActionEnum.INC, 2))  # Increase quality by 2 if sell_in < 0
            ],
            sell_in_action=ActionUnit(ActionEnum.DEC, 1),  # Decrease sell_in by 1 each day
            min_quality=0,  # Minimum quality constraint
            max_quality=50  # Maximum quality constraint
        ),
        # Rules for "Sulfuras, Hand of Ragnaros"
        "Sulfuras, Hand of Ragnaros": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.DEC, 0),  # No change in quality
            update_rules=[],  # No additional rules
            sell_in_action=ActionUnit(ActionEnum.DEC, 0),  # No change in sell_in
            min_quality=80,  # Fixed quality constraint
            max_quality=80  # Fixed quality constraint
        ),
        # Rules for "Backstage passes to a TAFKAL80ETC concert"
        "Backstage passes to a TAFKAL80ETC concert": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.INC, 1),  # Increase quality by 1 each day
            update_rules=[
                # Increase quality by 2 if sell_in is between 6 and 10
                UpdateRule("item.sell_in <= 10 and item.sell_in > 5", ActionUnit(ActionEnum.INC, 2)),
                # Increase quality by 3 if sell_in is between 1 and 5
                UpdateRule("item.sell_in <= 5 and item.sell_in > 0", ActionUnit(ActionEnum.INC, 3)),
                # Set quality to 0 if sell_in is 0 or less (concert date passed)
                UpdateRule("item.sell_in <= 0", ActionUnit(ActionEnum.DEC, float('inf')))
            ],
            sell_in_action=ActionUnit(ActionEnum.DEC, 1),  # Decrease sell_in by 1 each day
            min_quality=0,  # Minimum quality constraint
            max_quality=50  # Maximum quality constraint
        ),
        # Rules for "Conjured Mana Cake"
        "Conjured Mana Cake": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.DEC, 2),  # Decrease quality by 2 each day
            update_rules=[
                UpdateRule("item.sell_in < 0", ActionUnit(ActionEnum.DEC, 2))  # Decrease quality by 2 more if sell_in < 0
            ],
            sell_in_action=ActionUnit(ActionEnum.DEC, 1),  # Decrease sell_in by 1 each day
            min_quality=0,  # Minimum quality constraint
            max_quality=50  # Maximum quality constraint
        ),
        # Rules for a Normal Item
        "Normal Item": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.DEC, 1),  # Decrease quality by 1 each day
            update_rules=[
                UpdateRule("item.sell_in < 0", ActionUnit(ActionEnum.DEC, 1))  # Decrease quality by 1 more if sell_in < 0
            ],
            sell_in_action=ActionUnit(ActionEnum.DEC, 1),  # Decrease sell_in by 1 each day
            min_quality=0,  # Minimum quality constraint
            max_quality=50  # Maximum quality constraint
        ),
    }
    logging.info("Rules loaded successfully")
    return rules
