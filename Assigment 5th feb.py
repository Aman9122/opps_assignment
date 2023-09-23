#!/usr/bin/env python
# coding: utf-8

# In[13]:


#1 Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.
"""solution -Class is blueprint for creating object , 
When I create a any project then I used lot of modulo, like
frented modulo , bancked modulo , many more , in this prosess 
create a unstructe modulo and the advantage of class is stuctred a module 
for helping for reuseablity , also also for develoers



obejct is a instance of a class  """
'Example for a class'

class Home:
    # Define a home
    def __init__(self, owner_name, apartment_no, colour_of_house):
        self.owner_name = owner_name
        self.apartment_no = apartment_no
        self.colour_of_house = colour_of_house

    def return_define_a_home(self):
        return self.owner_name, self.apartment_no, self.colour_of_house

            
         




# In[19]:


aman = Home("aman", 5, "yellow")


# In[17]:


aman.return_define_a_home


# In[18]:


#2 - Name the four pillars of OOPs.

''' Encapsulation: Imagine putting your data and the code that works on that data inside a box. This box protects the data from being accessed or modified directly from outside. It's like a safe container for your information.

Abstraction: Think of abstraction as simplifying something complex. When you use a TV remote, you don't need to know how the TV works internally. You just press a button, and it does what you expect. Abstraction hides the complicated details and provides a simpler interface.

Inheritance: Inheritance is like inheriting traits from your parents. It allows you to create new classes based on existing ones, inheriting their properties and behaviors. It's like saying, "I want a new thing that's similar to this old thing, but with some differences."

Polymorphism: Polymorphism means that different objects can respond to the same message or method in their unique ways. It's like having a universal remote that works with different TVs. Each TV may respond differently to the same buttons, but they all understand and react to them.'''


# In[20]:


# 3 - Explain why the __init__() function is used. Give a suitable example.

'''
   __init__ fuctions is used in Python to initalize the attributs of an object when it is created. 
    The primery perpose of __init__ is to set up the intial state or properties of the object. 
    '''

# here is my first example 
class Home:
    # Define a home
    def __init__(self, owner_name, apartment_no, colour_of_house):
        self.owner_name = owner_name
        self.apartment_no = apartment_no
        self.colour_of_house = colour_of_house

    def return_define_a_home(self):
        return self.owner_name, self.apartment_no, self.colour_of_house

            


# In[21]:


aman = Home("aman", 5, "yellow")


# In[23]:


aman.return_define_a_home


# In[24]:


# 4 Why self is used in OOPs?

""" 
   In OOP function , ' self  is used to refer to the 
   instance of the class within the class's methods,
   it serves as a way to access and manipulate teh instance's 
   attributes and methods from within the class itself"""


# In[29]:


# What is inheritance? Give an example for each type of inheritance
"""
   it allows yout to create new classes based on exising ones
   it;s like saying,  I want  a new thing thet's similar to this 
   old thing, but with some differeces."""

'there is serverl types of inheritance and few of this '

'''
1 Single Inheritance in single inhertance a subclsas inehrits 
from a single superclass.
Example'''


class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return"Meow!"
    
'''
2 Multiple Inheritance: In multiple inhertance, a subclass can inherit from multiple supercalsees

'''

class Flyable:
    def fly(self):
        pass

class Swimmable:
    def swim(self):
        pass

class Bird(Flyable, Swimmable):
    pass

# Bird inherits from both Flyable and Swimmable classes.


# In[ ]:




