#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Dictionary
student = {"name": "Kapil", "Age": 25, "Courses": ["Data Engineer", "Cloud", "Big data"]}
print(student)


# In[7]:


print(student["Courses"])


# In[15]:


print(student.get("phone", "NoT FoUnD"))


# In[17]:


student["name"] = "Manmohan"


# In[18]:


print(student)


# In[22]:


student.update({"name" : "Kapil"})


# In[23]:


student


# In[24]:


del student["Age"]


# In[25]:


print(student)


# In[28]:


student.update({"Age": 25})
student


# In[30]:


student.keys()


# In[31]:


len(student)


# In[33]:


student.items()


# In[55]:


# string format in dictionary
for k,v in student.items():
    print("{k} is {v}")


# In[82]:


# Sets
set_1 = {1,3,5,7,9}
set_2 = {2,3,4,6,7,8,9}
set_4= set_2.symmetric_difference(set_1)
set_4


# In[84]:


# Removing duplicates in the list
list1 = [2,3,4,5,6,7,8,3,4,5]
list2 = list(set(list1))
print(list2)


# In[66]:


set_1.remove(1)


# In[69]:


set_1.discard(11)


# In[70]:


set_1


# In[73]:


set_4 = set_2.union(set_1)
set_4


# In[81]:





# In[90]:


# Problem 1
i = 1

while i < 11:
    print(i)
    i = i+1


# In[111]:


# Problem 2

row = 5

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("   ")


# In[117]:


# Problem 3 (Sum till the given input number)

inp = int(input("The input number is:"))
count = 0

for i in range(inp):
    count = count + i
    i +=1
    
print("The total sum of the given number is %d"%count)
    


# In[129]:


# Problem 4 Multiplication table of a given number 

inp = int(input("The input number is:"))

for i in range(1,inp):
    for j in range(1,11):
        mul = inp * j
        print(mul)
    print(" ")


# In[142]:


# Problem 5
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i <= 150 and i%5 == 0:
        print(i)
    elif i > 500 and i%5 == 0:
        break
                
    


# In[158]:


# Problem 6
# In Python 3.x, 5 / 2 will return 2.5 and 5 // 2 will return 2. 
# The former is floating point division, and the latter is floor division, sometimes also called integer division.


inp = 75869
out = 0

while inp != 0:
    inp = inp//10
    out += 1
print(out)


# In[169]:


# Problem 7   # Tricky but nice to code

row = 5
rows = 5

for i in range(0,row+1):                              # number of Rows
    for j in range(rows-i, 0, -1):                     # columns
        print(j, end=" ")
    print("")


# In[178]:


# Problem 8  Print list in reverse order using for loop
# Using reversed function

list1 = [10, 20, 30, 40, 50]
rev_list = []
rev = reversed(list1)

for i in rev:
    rev_list.append(i)
print(rev_list)


# In[189]:


# Using len fucntion 

size = len(list1)
rev_l = []

for i in range(size-1, -1, -1):
    rev_l.append(list1[i])

print(rev_l)


# In[200]:


# problem 9 Display the number for -10 to -1



for i in range(-10,0,1):
    print(i)


# In[205]:


# Problem 10

for i in range(0,6):
    if i < 5:
        print(i)
        i += 1
    else:
        print("Done")
        


# In[ ]:




