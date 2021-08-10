#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Python Workshop 1: Variables

# Key 
# + Concept 
# @ Code Explanation 
# & Interaction with Students 
# ! Run the Code 


# In[14]:


# @/+ We're gonna be working with the Pythagorean Theorem today, which can help us figure out any missing side given 2
# sides of a right triangle.

a = 3
b = 4
c = None
# @ How can we figure out C? (Assuming that these 3 sides are a part of a right triangle.)

# + a, b, and c above are what we call variables! Variables are much like the variables we see in our 
# math classes. They can store a number value or a word value, otheriwse known as a string!


# In[15]:


# ! - Show the students what happens when we print each of these values. (The idea is for them to see that whatever the variable is equal to, will appear when we print it out.)
print(a)
print(b)
print(c)

# & Encourage students to write their own variables with different number values inside of them and print them using a print statement.


# In[17]:


import math # + This is called a library! You can think of a library as a door . To access certain functions, you need to have a key.
# In our case, the function we want to access (and what we need our key for) is math.sqrt() which will be explained later.


# In[19]:


# @ Now, we are going to write a program to figure out what c is!

# @ Pythagorean Theorem: (a)**2 + (b)**2 = (c)**2, given this information, how we can find c?
# @ Well, lets see if we can arrange the formula in a way that will isolate c by itself (run through math for this.)
# @ What we would find is that when we isolate c, we get a formula like this: c = sqrt((a)**2 + (b)**2)
# @ ** = squaring a value, math.sqrt() = square rooting a value, + = addition. Now, lets convert this idea to code!

c = math.sqrt((a)**2 + (b)**2)
print(c)

# & Great! Now we can find our missing value. Now, try to see if you can find a missing value from a triangle given the other two values using what we learned!

