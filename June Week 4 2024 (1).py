#!/usr/bin/env python
# coding: utf-8

#     11. Container With Most Water
# 
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 

# In[ ]:


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        vmax = 0
        vol = 0
        first = 0
        last = len(height)-1
        for i in range(len(height)):
            if last == first:
                return vmax
            if height[last] >= height[first]:
                vol = height[first] * (last-first)
                first +=1
            else:
                vol = height[last] * (last-first)
                last -=1
            if vol > vmax:
                vmax = vol


# 
#     2490. Circular Sentence
# 
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# 
# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.
# 
# A sentence is circular if:
# 
# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.
# 
# Given a string sentence, return true if it is circular. Otherwise, return false

# In[ ]:


if sentence[0] != sentence[-1]:
            return False
        words = sentence.split()
        for i in range(len(words)-1):
            if words[i][-1] != words[i+1][0]:
                return False
        return True


#     58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# 
# A word is a maximal substring consisting of non-space characters only.

# In[ ]:


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])


#     Factorial and x^n using Recursion

# In[35]:


def fact(num):
    if num <= 1:
        return 1
    else:
        return  num * fact(num-1)

num = input("Enter number: ")

if  not isinstance(num, int):
    print("invalid input")
else:
    print (fact(int(num)))
    


# In[37]:


num = int(input("Enter number: "))
deg = int(input("Enter power: "))
def power(num,deg):
    if num == 1:
        return num
    elif deg == 1:
        return num
    else:
        return  num * power(num, deg-1)
print (power(num,deg))


#     Nth term of Fibonacci series - Recursive

# In[44]:


term = int(input("Enter term no.: "))
def fib(term):
    if term <= 2:
        return 1
    else:
        return fib(term-1) + fib(term-2)
    
print (fib(term))


# 

# In[ ]:




