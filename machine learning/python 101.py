#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = 5

b = True

c= 7.6

d = "how r u?"

print(type(d))
print(type(a))
print(type(b))
print(type(c))


# In[ ]:


list1 = [1,3,4,5]

dic = {1:2, 3:4, 5:6}

print(list(map(list, dic.items())))

print(list(dic.items()))

# print(lis2)


# In[3]:


a = [1,4,6,7,8,9]
# cal = 0
# sum =[]
# for i in a:
    
#     cal += i
    
# sum.append(cal)
# print(sum)

cal1 = 0

s1 = []

s = [cal1 := cal1 + i for i in a]
s1.append(s[-1])
print(s1)

a1 = []

a1.append(sum(a))


# In[4]:


eve = [i for i in range(1,51) if i %2 == 0]
sum(eve)


# In[5]:


arr = [-90, 34,9,100,-95,34,98,-101,38,-88]
neg = []
pos = []

for i in arr:
    
    if i < 0:
        
        neg.append(i)
    else:
        
        pos.append(i)

print(neg + pos)



