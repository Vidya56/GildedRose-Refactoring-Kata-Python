# Gilded Rose Refactoring Kata - Python

The detailed exercise of Gilded Rose Refactoring Kata can be found here - https://github.com/NotMyself/GildedRose.


The Python code can be found here - https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/python

In the Gilded Rose store, there are 3 things to know - 
* All items have a SellIn value which denotes the number of days we have to sell the item
* All items have a Quality value which denotes how valuable the item is
* At the end of each day our system lowers both values for every item

The existing codebase provides support for three products, however, the addition of a new product Conjured breaks the existing business logic and hence needs remodeling. There are a few business rules and constraints that need to be taken care of while refactoring the code.

## Business Rules
1. All items will have the three attributes as follows:
    1. name – Name of the item.
    2. sell_in – The number of days within which the item should be sold off.
    3. quality – The quality of the item; denoted by an integer.
2. Every day, the method update_quality() is executed, which lowers the values for sell_in and quality each.
3. Once the sell_in date has passed, the value for quality degrades twice faster.
4. There are also rules for each of the items that are currently present which are as follows.
    1. AgedBrie increases its quality with a decrease in sell_in value.
    2. BackstagePasses has the following two rules:
        1. When sell_in value is more than 10, quality increases by 1.
        2. When sell_in value is less than 10, quality increases by 2.
        3. When sell_in value is less than 5, quality increases by 3.
        4. When sell_in value is less than 0, quality is set to 0.
    3. Sulfuras is legendary, so quality is always 80 and sell_in value never decreases.
    4. A new item – Conjured is to be added with the following rule:
        1. Conjured items degrade quality twice as fast as normal items.


## Constraints
There are a few constraints that we need to consider before refactoring.
1. We are not allowed to alter the Item class or the attributes of the Item class.
2. The minimum and maximum values for quality can only be 0 and 50 respectively.

## Run the python file 

```
python gilded_rose_refactored.py
```

## Run the unit tests from the Command-Line

```
python tests/my_tests.py
```

## Run the TextTest fixture from the Command-Line
The script for conjured items have been changed as well which fixes this test case from the origin repo.

For e.g. 10 days:

```
python tests/texttest_fixture.py 10
```