#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a python program to store all the programming languages known to you using
# Set.

s1 = {'C','C++','Java',"Python","Machine Learning","NLP","CV"}
print(type(s1),s1)


# In[73]:


# 2. Write a python program to store your own information {name, age, gender, so on..}


s1 = {'name',"age",}
print(s1)


# In[74]:


# 3. Write a python script to get the data type of a Set.

set1 = {"hello i am prayag soni and what is your name"}
print(type(set1),set1)


# In[26]:


# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
# "Python", "Django"}

set1 = {"java","Python","Django"}
if "Python" in set1:
    print("Python is present in set1 ")
    print("Tnx for check this program")
else:
    print("! Sorry Python is not present in set1")
    print(set1)


# In[33]:


# 5. Write a python program to add items from another set to the current set. thisset =
# {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}

thisset = {"Java","Python","Sql"}
secondset = {"C","Cpp","Sql"}
thisset.update(secondset)
print(thisset)
print(type(thisset))


# In[49]:


# 6. Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

thisset = {"Python","Django","Javascript"}
mylist = ["Java","c"]
thisset.update(mylist)
print(thisset)
print(type(thisset))


# In[44]:


myset = set((1,2,3,4))
mylist = list([1,2,3])

myset.add(tuple(mylist))
print(myset)


# In[54]:


# 7. Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}

thisset = {"python","django","javascript","sql"}
thisset.remove("sql")
print(thisset)


# In[55]:


# 8. Write a python program to delete the set completely.

thisset = {"python","django","javascript","sql"}
thisset.clear()
print(thisset)


# In[77]:


# 9. Write a python program to loop through the set and print values
# thisset = {"Python", "Django", "JavaScript", “SQL”}


thisset = {"Python", "Django", "JavaScript", "SQL"}
for value in thisset :
    print(thisset)
   



# In[67]:


# 10. Write a python program to find the maximum and minimum value in a set.

set2  = {10,20,30,40,60}
print("maximum valuse is ",max(set2))
print("Minimum set2 value is ",min(set2))
print(set2)


# In[ ]:




