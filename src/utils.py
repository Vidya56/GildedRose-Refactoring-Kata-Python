import logging
from enum import Enum

# Set up logging to display debug information
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class ActionEnum(Enum):
    '''
    Enum to define possible actions
    '''
    INC = 1
    DEC = 2
 
class ActionUnit:
    '''
    Class representing an action with a specified number of units
    '''
    def __init__(self, action: ActionEnum, units: int):
        self.action = action
        self.units = units
        # Log creation of ActionUnit instance
        logging.debug(f"ActionUnit created: {self.action}, {self.units} units")

class UpdateRule:
    '''
    Class representing a rule that will be applied based on a specific condition (bound)
    and its associated action
    '''
    def __init__(self, bound: str, action: ActionUnit):
        self.bound = bound
        self.action = action
        # Log creation of UpdateRule instance
        logging.debug(f"UpdateRule created: Bound='{self.bound}', Action={self.action}")

class UpdateRuleSet:
    '''
    Class representing a set of rules for updating an item's quality and sell_in, 
    with optional minimum and maximum quality constraints
    '''
    def __init__(self, base_action: ActionUnit, update_rules: list[UpdateRule],
                 min_quality: int = 0, max_quality: int = 50, sell_in_action: ActionUnit = None):
        self.base_action = base_action  # Default action if no specific rule matches
        self.update_rules = update_rules  # List of specific rules to apply
        self.min_quality = min_quality  # Minimum allowed quality
        self.max_quality = max_quality  # Maximum allowed quality
        self.sell_in_action = sell_in_action  # Action to apply to sell_in
        logging.debug(f"UpdateRuleSet created: BaseAction={self.base_action}, MinQuality={self.min_quality}, MaxQuality={self.max_quality}, SellInAction={self.sell_in_action}")

    # Method to apply the set of rules to a given item
    def apply_rules(self, item):
        logging.info(f"Applying rules to item: {item.name} (Sell In: {item.sell_in}, Quality: {item.quality})")
        applied_rule = False  # Flag to track if a specific rule was applied

        # Iterate through each rule and apply the first matching one
        for rule in self.update_rules:
            logging.debug(f"Checking rule: {rule.bound}")
            if eval(rule.bound, {"item": item}):
                logging.info(f"Rule matched for item '{item.name}': {rule.bound}. Applying action: {rule.action.action}")
                self.apply_action(item, rule.action)
                applied_rule = True
                break 

        # If no specific rule matched, apply the base action
        if not applied_rule:
            logging.info(f"No specific rule matched for item '{item.name}'. Applying base action.")
            self.apply_action(item, self.base_action)

        # Apply the sell_in action if defined
        if self.sell_in_action:
            self.apply_sell_in_action(item)

        # Apply any post sell_in rules
        if item.sell_in < 0:
            for rule in self.update_rules:
                if "item.sell_in < 0" in rule.bound:
                    logging.info(f"Applying post sell_in rule for '{item.name}'")
                    self.apply_action(item, rule.action)

    # Method to apply the sell_in action to an item
    def apply_sell_in_action(self, item):
        item.sell_in += self.sell_in_action.units
        logging.debug(f"Updated sell_in of '{item.name}': {item.sell_in}")

    # Method to apply a quality action (increase or decrease) to an item
    def apply_action(self, item, action):
        logging.debug(f"Applying action '{action.action}' with units '{action.units}' to item '{item.name}'")
        if action.action == ActionEnum.INC:
            # Ensure quality does not exceed max limit
            item.quality = min(self.max_quality, item.quality + action.units)
        elif action.action == ActionEnum.DEC:
            # Ensure quality does not drop below min limit
            item.quality = max(self.min_quality, item.quality - action.units)
        logging.debug(f"Updated quality of '{item.name}': {item.quality}")
