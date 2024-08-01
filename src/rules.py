import logging
from utils import ActionEnum, ActionUnit, UpdateRule, UpdateRuleSet
# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def load_rules():
    logging.info("Loading rules for items")
    rules = {
        "Aged Brie": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.INC, 1),
            update_rules=[
                UpdateRule("item.sell_in < 0", ActionUnit(ActionEnum.INC, 2))
            ],
            min_quality=0,
            max_quality=50
        ),
        "Sulfuras, Hand of Ragnaros": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.DEC, 0),
            update_rules=[],
            min_quality=80,
            max_quality=80
        ),
        "Backstage passes to a TAFKAL80ETC concert": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.INC, 1),
            update_rules=[
                UpdateRule("item.sell_in <= 10 and item.sell_in > 5", ActionUnit(ActionEnum.INC, 2)),
                UpdateRule("item.sell_in <= 5 and item.sell_in > 0", ActionUnit(ActionEnum.INC, 3)),
                UpdateRule("item.sell_in <= 0", ActionUnit(ActionEnum.DEC, float('inf')))
            ],
            min_quality=0,
            max_quality=50
        ),
        "Conjured Mana Cake": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.DEC, 2),
            update_rules=[
                UpdateRule("item.sell_in < 0", ActionUnit(ActionEnum.DEC, 2))
            ],
            min_quality=0,
            max_quality=50
        ),
        "Normal Item": UpdateRuleSet(
            base_action=ActionUnit(ActionEnum.DEC, 1),
            update_rules=[
                UpdateRule("item.sell_in < 0", ActionUnit(ActionEnum.DEC, 1))
            ],
            min_quality=0,
            max_quality=50
        ),
    }
    logging.info("Rules loaded successfully")
    return rules
