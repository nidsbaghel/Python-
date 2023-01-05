#!/usr/bin/env python
# coding: utf-8

# Question: - 3
# Inexperienced in the digital arts, the cows tried to build a calculating engine (yes, it's a cowmpouter)
# using binary numbers (base 2) but instead built one based on base negative 2! They were quite
# pleased since numbers expressed in base -2 do not have a sign bit.
# You know number bases have place values that start at 1 (base to the 0 power) and proceed rightto-left to base^1, base^2, and so on. In base -2, the place values are 1, -2, 4, -8, 16, -32, ... (reading
# from right to left). Thus, counting from 1 goes like this: 1, 110, 111, 100, 101, 11010, 11011, 11000,
# 11001, and so on.
# Eerily, negative numbers are also represented with 1's and 0's but no sign. Consider counting from
# -1 downward: 11, 10, 1101, 1100, 1111, and so on.
# Please help the cows convert ordinary decimal integers (range -2,000,000,000 .. 2,000,000,000) to
# their counterpart representation in base -2.

# In[ ]:


# Method to convert n to base negBase
def toNegativeBase(n, negBase):


# In[ ]:


# If n is zero then in any base it
    # will be 0 only
    if (n == 0):
        return "0"
 
    converted = "01"
    while (n != 0):
          # Get remainder by negative base,
        # it can be negative also
        remainder = n % (negBase)
        n = int(n/negBase)
 
        # if remainder is negative, add
        # abs(base) to it and add 1 to n
        if (remainder < 0):
            remainder += ((-1) * negBase)
            n += 1
 
        # convert remainder to string add
        # into the result
        converted = str(remainder) + converted
         
    return converted


# In[ ]:


# Driver Code
if __name__ == '__main__':
    n = 13
    negBase = -2
 
    print(toNegativeBase(n, negBase))


# In[ ]:





# In[ ]:




