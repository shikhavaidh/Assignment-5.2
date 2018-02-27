
# coding: utf-8

# In[24]:

#Assignment 5.2
# Hello World program in Python
subjects=["American","Indians"]
verbs=["Play","Watch"]
objects=["Basketball","Cricket"]
#Using for loop
for sub in subjects:
    #print sub
    for vb in verbs:
        #print sub + " " + vb
        for obj in objects:
             print (sub + " " + vb + " " + obj)
            
print ("-------------------------------------------------------") 
#using list comprehension

item = [x + " " + y + " " + z for x in subjects for y in verbs for z in objects]
#print item
for number in item:
    print(number)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



