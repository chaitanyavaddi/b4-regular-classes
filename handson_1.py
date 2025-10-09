
# ---------------------------------------------------------------
# 1. Reverse Words in a Sentence (but not characters)
# ---------------------------------------------------------------
# Given a string, reverse the order of words while keeping punctuation attached.
# Example: "Hello, world! How are you?" → "you? are How world! Hello,"

def reverse_words(sentence: str) -> str:
    words = sentence.split()             # Split into words (punctuation stays attached)
    reversed_words = words[::-1]         # Reverse the word order
    return " ".join(reversed_words)      # Join back into a single string

# Example
print("Q1:", reverse_words("Hello, world! How are you?"))
# Output: you? are How world! Hello,



# ---------------------------------------------------------------
# 2. Find the Second Most Frequent Character
# ---------------------------------------------------------------
# Return the character that appears second most frequently in a string.
# Ignore spaces and capitalization.
# Example: "Aabbcccddd" → 'c'

def second_most_frequent_char(s: str) -> str:
    s = s.replace(" ", "").lower()       # Normalize string
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1   # Count each character

    # Sort by frequency (highest first)
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    if len(sorted_chars) < 2:
        return None                      # No second-most frequency
    return sorted_chars[1][0]

# Example
print("Q2:", second_most_frequent_char("Aabbcccddd"))
# Output: c













# ---------------------------------------------------------------
# 5. Custom Anagram Check (Ignore digits/punctuation, case-insensitive)
# ---------------------------------------------------------------
# Check if two strings are anagrams, ignoring digits, punctuation, and case.
# Example: "Debit Card!" and "Bad Credit" → True

def is_anagram(s1: str, s2: str) -> bool:
    # Keep only alphabetic characters, make lowercase
    s1_clean = ''.join(ch.lower() for ch in s1 if ch.isalpha())
    s2_clean = ''.join(ch.lower() for ch in s2 if ch.isalpha())
    return sorted(s1_clean) == sorted(s2_clean)

# Example
print("Q5:", is_anagram("Debit Card!", "Bad Credit"))
# Output: True


# ---------------------------------------------------------------
# 6. Move Zeros to the End (in-place)
# ---------------------------------------------------------------
# Move all zeros to the end without creating a new list.
# Preserve the order of non-zero elements.
# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

def move_zeros(nums: list[int]) -> None:
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

# Example
arr = [0, 1, 0, 3, 12]
move_zeros(arr)
print("Q6:", arr)
# Output: [1, 3, 12, 0, 0]


# ---------------------------------------------------------------
# 7. Balanced Parentheses (with <> support)
# ---------------------------------------------------------------
# Check if a string containing (), {}, [], and <> is balanced.
# Example: "{[<>]}" → True, "{[<]>}" → False

def is_balanced(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '[', '>': '<'}
    
    for ch in s:
        if ch in pairs.values():     # Opening brackets
            stack.append(ch)
        elif ch in pairs.keys():     # Closing brackets
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

# Example
print("Q7:", is_balanced("{[<>]}"))
# Output: True
print("Q7:", is_balanced("{[<]>}"))
# Output: False
