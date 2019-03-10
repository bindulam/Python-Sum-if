
# coding: utf-8

# In[1]:


import queue

import sys
N = int(input())
K = int(input())


# In[2]:


Ar = []
# for i in range(0,5):
#     a = int(input())
i = sys.stdin.readline()
A = i.split()


# In[4]:


print(A)


# In[6]:


Q = queue.Queue(maxsize = N)
St = queue.LifoQueue(maxsize=N)


# In[7]:


def subarraylen(arr , n ,x):
    length = n +1
    for i in range(0,n): 
        arr_sum = arr[i] 
        if (arr_sum > x): 
            return 1
   
        for j in range(i+1,n): 
            arr_sum += arr[j] 
            if arr_sum >= x and (j - i +1 ) < length: 
                length = (j - i + 1 ) 
          
    return length;


# In[8]:


import sys
L = []
i = 1
while(i == 1):
    print(i)
    for i in range(0,len(A)):
        Q.put(int(A[i]))
    for  i in range(0,len(A)):
        L.append(Q.get())
    for i in range(0,len(A)):
        St.put(int(A[i]))
    for i in range(0,len(A)):
        L.append(St.get())
    if(sys.getsizeof(L) >= 50):
	print("hi")
        i = 0


# In[19]:

le = subarraylen(L,3*N,K)
print(le)

