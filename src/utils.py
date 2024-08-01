import logging
from enum import Enum


# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ActionEnum(Enum):
    INC = 1
    DEC = 2

class ActionUnit:
    def __init__(self, action: ActionEnum, units: int):
        self.action = action
        self.units = units
        logging.debug(f"ActionUnit created: {self.action}, {self.units} units")

class UpdateRule:
    def __init__(self, bound: str, action: ActionUnit):
        self.bound = bound
        self.action = action
        logging.debug(f"UpdateRule created: Bound='{self.bound}', Action={self.action}")

class UpdateRuleSet:
    def __init__(self, base_action: ActionUnit, update_rules: list[UpdateRule], min_quality: int = 0, max_quality: int = 50):
        self.base_action = base_action
        self.update_rules = update_rules
        self.min_quality = min_quality
        self.max_quality = max_quality
        logging.debug(f"UpdateRuleSet created: BaseAction={self.base_action}, MinQuality={self.min_quality}, MaxQuality={self.max_quality}")

    def apply_rules(self, item):
        logging.info(f"Applying rules to item: {item.name} (Sell In: {item.sell_in}, Quality: {item.quality})")
        applied_rule = False
        for rule in self.update_rules:
            logging.debug(f"Checking rule: {rule.bound}")
            if eval(rule.bound, {"item": item}):
                logging.info(f"Rule matched for item '{item.name}': {rule.bound}. Applying action: {rule.action.action}")
                self.apply_action(item, rule.action)
                applied_rule = True

        if not applied_rule:
            logging.info(f"No specific rule matched for item '{item.name}'. Applying base action.")
            self.apply_action(item, self.base_action)

        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

        if item.sell_in < 0:
            for rule in self.update_rules:
                if "item.sell_in < 0" in rule.bound:
                    logging.info(f"Applying post sell_in rule for '{item.name}'")
                    self.apply_action(item, rule.action)

    def apply_action(self, item, action):
        logging.debug(f"Applying action '{action.action}' with units '{action.units}' to item '{item.name}'")
        if action.action == ActionEnum.INC:
            item.quality = min(self.max_quality, item.quality + action.units)
        elif action.action == ActionEnum.DEC:
            item.quality = max(self.min_quality, item.quality - action.units)
        logging.debug(f"Updated quality of '{item.name}': {item.quality}")
