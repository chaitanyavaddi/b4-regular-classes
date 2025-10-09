# ---------------------------------------------------------------
# 1. Reverse Words in a Sentence (keep case & punctuation same)
# ---------------------------------------------------------------
# Given a string, reverse the words’ order — 
# but remove extra spaces and make sure there is only one space between words.
# Example: "  Python   is  fun!  " → "fun! is Python"

def reverse_words_clean(sentence: str) -> str:
    # TODO: your code here
    pass

# Example
# print(reverse_words_clean("  Python   is  fun!  "))  # Output: fun! is Python


# ---------------------------------------------------------------
# 2. Find the Third Most Frequent Character
# ---------------------------------------------------------------
# Return the character that appears third most frequently in a string.
# Ignore spaces and punctuation. If fewer than 3 unique letters exist, return None.
# Example: "aaabbccddddee" → 'c'

def third_most_frequent_char(s: str) -> str:
    # TODO: your code here
    pass

# Example
# print(third_most_frequent_char("aaabbccddddee"))  # Output: c


# ---------------------------------------------------------------
# 5. Check if Two Phrases Are “Loose Anagrams”
# ---------------------------------------------------------------
# Two strings are “loose anagrams” if they contain the same letters,
# but you can ignore up to 1 character difference.
# Ignore case, spaces, and punctuation.
# Example: "Listen" and "Silentt" → True  (1 extra 't' allowed)

def is_loose_anagram(s1: str, s2: str) -> bool:
    # TODO: your code here
    pass

# Example
# print(is_loose_anagram("Listen", "Silentt"))  # Output: True


# ---------------------------------------------------------------
# 6. Move Negative Numbers to the Start (in-place)
# ---------------------------------------------------------------
# Similar to the “move zeros” problem.
# Move all negative numbers to the front, preserving the order of non-negatives.
# Example: [3, -1, 4, -2, 0] → [-1, -2, 3, 4, 0]

def move_negatives(nums: list[int]) -> None:
    # TODO: your code here
    pass

# Example
# arr = [3, -1, 4, -2, 0]
# move_negatives(arr)
# print(arr)  # Output: [-1, -2, 3, 4, 0]


# ---------------------------------------------------------------
# 7. Check Balanced Brackets in Math Expression
# ---------------------------------------------------------------
# Given a string representing a math expression, check if all brackets () {} [] are balanced.
# Ignore numbers, operators, and spaces.
# Example: "3 * (2 + [5 - {1}])" → True

def is_balanced_expression(expr: str) -> bool:
    # TODO: your code here
    pass

# Example
# print(is_balanced_expression("3 * (2 + [5 - {1}])"))  # Output: True
# print(is_balanced_expression("(3 + 2]"))              # Output: False
