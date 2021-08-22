#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


l = [1,2,3,4,5,6]
for i in l:
    print(i+1)


# In[4]:


# [] - list
# () - tupe
# {} - dictionary



['123',2,4,5] #this describes list



'''
this describes list
dsas
fdgsfgafeqtheah
gaggafeerba
gegwe

'''
khkdekjhj


# In[19]:


#pranay = 'pranay is my friend'
a = int(123.3)
a
b = a+3
b
#pranay  = 123


# In[27]:


print(1!=2) #  not equal to
print(1==2) # equal 

#print(pranay)


# In[30]:


1 <= 0


# In[36]:


123<123.1


# In[40]:


a =1
b = 2
c = 3

a,b,c = 1,2,3


# In[41]:


print(a,b,c)


# In[42]:


a = b = c = 1
print(a,b,c)


# In[47]:


l = [1,2,3]
a,b,c = l #[1,2,3]
print(a,b,c)


# In[48]:


a = 'pranay is'
b = 'my friend'

a+b


# In[51]:


a+' '+b+' '+'.I am not lying'


# In[54]:


a = 122
b = 125
str(a) + str(b) + 'is my favourite number'


# In[56]:


def pranaysfunction(a):# input value should be written in braces
    
    value = str(a)
    string = 'Is my favourite number'
    output = value + ' ' +string
    
    return output # output value that this function should return 


# In[59]:


myoutput = pranaysfunction(5)
print(myoutput)


# In[60]:


def concatenatedoutput(a,b):# input value should be written in braces
    
    
    output = a + ' ' + b
    
    return output # output value that this function should return 


# In[62]:


concatenatedoutput('pubg','is my favourite game')


# In[69]:


def evenorodd(a):
    
    
    if a%2 == 0:
        b = 'even'
    else:
        b = 'odd'
    
    
    return b


# In[71]:


evenorodd(2)


# In[72]:


def number(a):

    if a==0:
        output = 'this is 0'
    elif a>0:
        output = 'this is greater than zero'
    elif a<0 : 
        output = 'this is less than zero'
    
    
    return output 
        


# In[75]:


number(6)


# In[78]:


6>0


# In[ ]:




