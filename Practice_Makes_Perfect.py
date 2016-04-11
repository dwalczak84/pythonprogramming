###############################################################################
# Practice Makes Perfect
###############################################################################
# Practice! Practice Practice!
# The best way to get good at anything is a lot of practice. This lesson is 
# full of practice problems for you to work on. This section will contain 
# minimal instructions to help you solve these problems; instead, this section 
# will help you work on taking your programming skills and applying them to 
# real life problems.

# The more challenging programs will contain some helpful hints to nudge you 
# in the right direction. If you feel as if you are completely lost, feel free 
# to check out the Q&A section for help (the link is on the very bottom left 
# of your screen).
###############################################################################
# is_even
###############################################################################
# Instructions
# 1) Define a function is_even that will take a number x as input.
# 2) If x is even, then return True.
# 3) Otherwise, return False.

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
###############################################################################
# is_int
###############################################################################
# Instructions
# 1) Define a function is_int that takes a number x as an input.
# 2) Have it return True if the number is an integer (as defined above) and 
# False otherwise.

def is_int(x):
    if x % 1 == 0:
        return True
    else:
        return False
###############################################################################
# digit_sum
###############################################################################
# Instructions
# Write a function called digit_sum that takes a positive integer n as input 
# and returns the sum of all that number's digits.
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
# (Assume that the number you are given will always be positive.)

def digit_sum(n):
    digits = list(str(n))
    sum = 0    
    for i in range(len(digits)):
        sum += int(digits[i])
    return sum
###############################################################################
# factorial
###############################################################################
# Instructions
# Define a function factorial that takes an integer x as input.
# Calculate and return the factorial of that number.

def factorial(x):
    i = 1
    result = 1
    while i < x + 1:
        result *= i
        i += 1
    return result
###############################################################################
# is_prime
###############################################################################
# Instructions
# 1) Define a function called is_prime that takes a number x as input.
# 2) For each number n from 2 to x - 1, test if x is evenly divisible by n.
# 3) If it is, return False.
# 4) If none of them are, then return True.

def is_prime(x):
    if x < 2:
        return False
    else:
        y = []    
        for n in range(2, x - 1):
            y.append(x % n != 0)
        return all(y)
###############################################################################
# reverse
###############################################################################
# Instructions
# Define a function called reverse that takes a string textand returns that 
# string in reverse.
# For example: reverse("abcd") should return "dcba".
# 1) You may not use reversed or [::-1] to help you with this.
# 2) You may get a string containing special characters - for example, !, @, or 
# #.
        
def reverse(string):
    a = list(string)
    i = len(a)
    b = []
    while i != 0:
        b.append(a[i-1])
        i -= 1
    return ''.join(b)
###############################################################################
# anti_vowel
###############################################################################
# Instructions
# Define a function called anti_vowel that takes one string, text, as input 
# and returns the text with all of the vowels removed.
# For example: anti_vowel("Hey You!") should return "Hy Y!".
# - Don't count Y as a vowel.
# - Make sure to remove lowercase and uppercase vowels.

def anti_vowel(text):
    return ''.join(char for char in text if char not in 'AaEeUuIiOo')
###############################################################################
# scrabble_score
###############################################################################
# Instructions
# Define a function scrabble_score that takes a string word as input and 
# returns the equivalent scrabble score for that word.
# 1) Assume your input is only one word containing no spaces or punctuation.
# 2) As mentioned, no need to worry about score multipliers!
# 3) Your function should work even if the letters you get are uppercase, 
# lowercase, or a mix.
# 4) Assume that you're only given non-empty strings.

def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
             "x": 8, "z": 10}
    word = list(word.lower())
    total= 0    
    for letter in word:
        total += score[letter]
    return total
###############################################################################
# censor
###############################################################################
# Instructions
# Write a function called censor that takes two strings, text and word, as 
# input. It should return the text with the word you chose replaced with 
# asterisks.

# For example:

# censor("this hack is wack hack", "hack") 
# should return

# "this **** is wack ****"
# 1) Assume your input strings won't contain punctuation or upper case letters.
# 2) The number of asterisks you put should correspond to the number of 
# letters in the censored word.

def censor(text, word):
    a = text.split()
    for i in range(0, len(a)):
        if a[i] == word:
            a[i] = '*' * len(list(word))
    return ' '.join(a)
###############################################################################
# count
###############################################################################
# Instructions
# 1) Define a function called count that has two arguments called sequence and 
# item.
# 2) Return the number of times the item occurs in the list.
# For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times 
# in the list).
# 3) There is a list method in Python that you can use for this, but you 
# should do it the long way for practice.
# 4) Your function should return an integer.
# 5) The item you input may be an integer, string, float, or even another list!
# 6) Be careful not to use list as a variable name in your code—it's a 
# reserved word in Python!
    
def count(sequence, item):
    total = 0
    for i in sequence:
        if i == item:
            total += 1
    return total
###############################################################################
# purify
###############################################################################
# Instructions
# Define a function called purify that takes in a list of numbers, removes all 
# odd numbers in the list, and returns the result.
# For example, purify([1,2,3]) should return [2].
# Do not directly modify the list you are given as input; instead, return a 
# new list with only the even numbers.
    
def purify(numbers):
    non_odds = []
    for number in numbers:
        if number % 2 == 0:
            non_odds.append(number)
    return non_odds
###############################################################################
# product
###############################################################################
# Instructions
# Define a function called product that takes a list of integers as input and 
# returns the product of all of the elements in the list.
# For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
# 1) Don't worry about the list being empty.
# 2) Your function should return an integer.
    
def product(integers):
    result = 1
    for number in integers:
        result *= number
    return result
###############################################################################
# remove_duplicates
###############################################################################
# Instructions
# Write a function remove_duplicates that takes in a list and removes elements 
# of the list that are the same.
# For example: remove_duplicates([1,1,2,2]) should return [1,2].
# 1) Don't remove every occurrence, since you need to keep a single occurrence 
# of a number.
# 2) The order in which you present your output does not matter. So returning 
# [1,2,3] is the same as returning [3,1,2].
# 3) Do not modify the list you take as input! Instead, return a new list.

def remove_duplicates(numbers):
    uniques = []
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
    return uniques
###############################################################################
# median
###############################################################################
# Instructions
# Write a function called median that takes a list as an input and returns the 
# median value of the list.
# For example: median([1,1,2]) should return 1.
# 1) The list can be of any size and the numbers are not guaranteed to be in 
# any particular order.
# 2) If the list contains an even number of elements, your function should 
# return the average of the middle two.

def median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return sum(numbers[len(numbers) / 2 - 1:len(numbers) / 2 + 1]) / 2.0
    else:
        return numbers[len(numbers) / 2]
###############################################################################
