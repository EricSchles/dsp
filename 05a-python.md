# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> List and tuples are similar in that they are both structured, ordered, and iterable sequence types. Each also can contain mixed data types. However, tuples are immutable while lists are mutable (changeable). Tuples can work as keys in dictionaries since a key for a dictionary HAS to be immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A python list and set are similar in that they are both iterable and mutable sequences of items. Both can also contained mixed data types. However, a set has no duplicates while a list can. Also, a list is ordered while a set is unordered.

An example of a list would be something like a list of political affiliations --> ['Rep','Rep','Rep','Green','Dem']. However, if we wanted just the unique values of political affiliations, we could just use the set method on the previous list to return ['Rep, 'Dem', Green']. If we were to try to find an element across a list, it would generally take a larger amount of time to find an element, since it has more to iterate/check through. However, since a set has only unique values, it would be a lot smaller to iterate through. In my list example, a loop through the set would return quicker than a loop through the list to find if 'Dem' existed.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' is primarily used to temporarily define a function for use by another function. To me, it's like quickly writing a function without actually declaring one through the normal declarative "def ______" structure.

Examples:

cubed = lambda x: x**3

list_of_states = ['Virginia','Washington','California','Georgia', 'South Carolina', 'Oregon']
sorted(list_of_states, key=lambda word: word[-2:])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a short hand way of being able to generate a list without having to write a for loop on multiple lines. Speaking in terms of python's 'map' and 'filter', list comprehension can incorporate both onto one line, applying 'filter' (returns a sequence containing the items from the original sequence for which the condition is True) first, then a 'map' (applies a function to every element of a sequence and returns a list). List comprehension mimics this map/filter functionality by using a for/if structure. Overall, list comprehension is favored for its simplicity/cleanliness.

Examples:

List Comprehension Example 1
store_item_prices = [89,62,83,46,31,108,99]
calculate_sale = [n - 5 for n in store_item_prices if n < 100]

Equivalent Map/Filter
calculate_sale = list(map(lambda n: n - 5, filter(lambda n: n < 100, store_item_prices)))

List Comprehension Example 2
numbers = [1,2,3,4,5,6,7,8,9,10]

double_evens = [w * 2 for w in numbers if w % 2 ==0]

Equivalent Map/Filter
double_evens = list(map(lambda w: w * 2, filter(lambda w: w % 2 == 0,numbers)))

Set Comprehension Example 1
list_of_names = ['John','Balboa','Johnny','Jon','Nicholas', 'Mark']
unique_name_lengths = {len(name) for name in list_of_names}

Set Comprehension Example 2
list_of_names = ['John','Balboa','Johnny','Jon','Nicholas','Mark','John']
unique_names= {name for name in list_of_names}

Dictionary Comprehension Example 1
list_of_heroes = {'Cyclops','Wolverine','Colossus','Beast','Gambit'}
length_of_hero_name = {hero:len(hero) for hero in list_of_heroes}

# Dictionary Comprehension Example 2
list_of_heroes = {'Cyclops','Wolverine','Colossus','Beast','Gambit'}
index_of_heroes = {hero:index for index, hero in enumerate(list_of_heroes)}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.
a.

```
date_start = '01-02-2013'
date_stop = '07-28-2015'
```

>> 937 days

b.
```
date_start = '12312013'
date_stop = '05282015'
```

>> 513 days

c.
```
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





