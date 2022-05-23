#!/usr/bin/env python
# coding: utf-8

# In[11]:


A=["Name : Kunal Salunkhe","Age:20","DOB:31 March 2001","Address: Amalner,Jalgaon ,Maharashtra"]
print(A)
B=["College Name: S.P. College,Pune","Class: T.Y.BSc","Specialisation: STATISTICS","Roll No. : 9128"]
print(B)


# In[13]:


type(A)
type(B)


# In[8]:


print(A[0]),print(A[1]),print(A[2]),print(A[3])


# In[14]:


print(B[0]),print(B[1]),print(B[2]),print(B[3])


# In[15]:


print(A[2:]) #access items above 2
print(A[:-1])   # Negative index


# In[16]:


print(B[0:2]) #access items above 2
print(A[-3:-1])   # Negative index


# In[19]:


print(A)
A[1]="Age:19"
print(A)            # Change item in a list


# In[20]:


# looping through list
for i in A:
   print(i)


# In[23]:


for j in B:
    print(j)


# In[11]:


#nested list
mylist=["Name : Kunal Salunkhe",["Class: T.Y.BSc","Specialisation: STATISTICS",
                                 ["College Name: S.P. College,Pune",
                                  ["Roll No. : 9128"]]]]
print(mylist)


# In[14]:


#### Tuples ####

t1=("Name : Kunal Salunkhe","Age:20","DOB:31 March 2001","Address: Amalner,Jalgaon ,Maharashtra")
t2=("College Name: S.P. College,Pune","Class: T.Y.BSc","Specialisation: STATISTICS","Roll No. : 9128")
print(t1,"\n")
print(t2)


# In[23]:


#Access elements  (As +ve)
print(t1[0])
print(t2[3:])
print(t1[:4])
print(t2[2:2]) ##Hahahaha 
print(t1[1:2])


# In[31]:


#Negative Index (As -ve)
print(t2[-4])
print(t1[:-3])
print(t1[-2:-3])
print(t2[-7:])   # Note here
print(t2[-3:])
print(t1[0:3])


# In[35]:


#looping through tuple
for d in t1:
    print(d)


# In[37]:


# check if 'Class: T.Y.BSc' inn t2
if "Class: T.Y.BSc" in t2:
    print("Class: T.Y.BSc is listed in t2")
print("Class: T.Y.BSc" in t2)


# In[38]:


# check if 'Class: T.Y.BSc' inn t1   ## note here  
if "Class: T.Y.BSc" in t1:
    print("Class: T.Y.BSc is listed in t1")
print("Class: T.Y.BSc" in t1)


# In[ ]:




