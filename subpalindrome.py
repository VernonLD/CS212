#! /usr/bin/python2.7
# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

#My solution 
# def is_palindrome(string):
#     return True if string.lower() == string[::-1].lower() else False

# def grow(start, end, result, text):
# 	l = len(text)
# 	while is_palindrome(text[start:end]) and start >= 0 and end <= l:
# 		if result[1] - result[0] < end - start:
# 			# if end - start == len(text):
# 			# 	return result
# 			print start, end 
# 			result = (start, end)
# 		start -= 1
# 		end   += 1
# 	return result

# def longest_subpalindrome_slice(text):
#     "Return (i, j) such that text[i:j] is the longest palindrome in text."
#     result = (0,0)
#     if not text:
#     	return result

#     for i in range(1,len(text)):
#     	result = grow(i - 1, i + 2, result, text)
#     	if text[i] == text[i - 1]:
#     		result = grow(i - 1, i + 1, result, text)


#     return result

#Teachers solution
def is_palindrome(string):
    return True if string.lower() == string[::-1].lower() else False

def grow(start, end, text):
	while is_palindrome(text[start-1:end+1]) and start > 0 and end < len(text):
		start -= 1
		end   += 1
	return (start, end)

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if not text: return (0,0)
    def length(slice): a,b = slice; return b-a
    # 1. start from the middle of the string -> easliy to find the longgest palindrome which length equal to length of string
    # 2. control the condition that only when start = start + 1 we find the palindrome start from (start, start + 1)
    result = [grow(start, end, text) 
    			for start in range(len(text)) 
    			for end in (start, start+1)]
    return max(result, key=length)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()