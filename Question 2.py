#!/usr/bin/env python
# coding: utf-8

# Question 1.Assume that you are a manager and there are m types of worker (numbered from 1 to m) and n
# types of task (numbered from 1 to n). There are a(i) workers of type #i and b(j) postitions for task
# #j. C(i, j) is the cost of hiring a worker of type #i to do the task of type #j. Your job is to minimize the
# cost of hiring workers to fill all the positions given that the total number of workers is equal to the
# total number of positions.
# 

# In[ ]:


def find(arr, pos, m, isRunning):


# In[ ]:


d = [0] * (m + 1)
    for i in range(m - 1, pos, -1):
         if isRunning[arr[i]]:
            d[arr[i]] = i


# In[ ]:


maxipos = 0
   for ele in d:
       maxipos = max(ele, maxipos)

   return maxipos
def mincost(n, m, arr):


# In[ ]:


freqarr = [[] for i in range(m)]


# In[ ]:


newvec = [0] * (m + 1)
    freqarr[m - 1] = newvec[:]
    for i in range(m - 2, -1, -1):
     
        nv = freqarr[i + 1][:]
        nv[arr[i + 1]] += 1
        freqarr[i] = nv[:]


# In[ ]:


isRunning = [False] * (m + 1)
    cost = 0


# In[ ]:


truecount = 0
   for i in range(0, m):
       ele = arr[i]
       if isRunning[ele] == True:
           continue
           else:
               if truecount < n:
               cost += 1
               truecount += 1
               isRunning[ele] = True
               else:
                   mini = 100000
                   miniind = 0
                   for j in range(1, m + 1):
                   if isRunning[j] and mini > freqarr[i][j]:
                       mini = freqarr[i][j]
                       miniind = j
                       if mini == 0:
                   isRunning[miniind] = False
                   isRunning[ele] = True
                   cost += 1
                    else:
                   farpos = find(arr, i, m, isRunning)
                   isRunning[arr[farpos]] = False
                   isRunning[ele] = True
                   cost += 1
                   return cost


# In[ ]:


if __name__ == "__main__":


# In[ ]:


# Test case 1
    n1, m1 = 3, 6
    arr1 = [1, 2, 1, 3, 4, 1]
    print(mincost(n1, m1, arr1))


# In[ ]:


# Test case 2
    n2, m2 = 2, 6
    arr2 = [1, 2, 1, 3, 2, 1]
    print(mincost(n2, m2, arr2))
 


# In[ ]:


# Test case 3
    n3, m3 = 3, 31
    arr3 = [7, 11, 17, 10, 7, 10, 2, 9,
            2, 18, 8, 10, 20, 10, 3, 20,
            17, 17, 17, 1, 15, 10, 8, 3,
            3, 18, 13, 2, 10, 10, 11]


# In[ ]:


print(mincost(n3, m3, arr3))


# In[ ]:




