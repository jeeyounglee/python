
# coding: utf-8

# In[3]:

# Review numpy library using the 
import numpy as np 


# In[1]:

# Review what the data looks like 

# 1::1193::5::978300760
# 1::661::3::978302109
# 1::914::3::978301968
# 1::3408::4::978300275
# 1::2355::5::978824291
# 1::1197::3::978302268
# ... 

# The MovieLens 1M dataset uses a double colon :: as separator.
# the 1st column (index 0) = user ID
# the 3rd column (index 2) = ratings


# In[19]:

data = np.loadtxt("data/ml-1m/ratings.dat", 
                  delimiter = "::", dtype=np.int64)


# In[18]:

data[:7, :]  # check the first 7 rows 


# In[20]:

data.shape 


# In[34]:

######################################################################
######## <<1>> Calculate total mean (mean of index 2 column) #########
totalmean_rate = data[:, 2].mean()


# In[35]:

totalmean_rate


# In[36]:

######################################################################
########  <<2>> Calculate mean rating of the each user ID  ###########

# Firstly, need to extract the unique user IDs from the data
ids = np.unique(data[:,0]) # use unique command, at the index 0


# In[37]:

ids 


# In[40]:

mean_rating_user = [] 

# Secondly, make an empty list, 
# user id and its mean rating will be added

for user_id in ids: 
    data_for_user = data[data[:, 0] == user_id, :] #(1) 
    mean_rating_id = data_for_user[:, 2].mean()  #(2) 
    mean_rating_user.append([user_id, mean_rating_id]) #(3)

# (1) ex) create data_for_user when the user_id == 1
# (2) Calculate the mean of data_for user (as this data all users are 1)
# (3) Store the user_id, and its calculated mean in mean_rating_user 
# (3) Loop users from 1 to 6040


# In[41]:

mean_rating_user[:5]


# In[42]:

# change it the array format 
mean_rating_user_array = np.array(mean_rating_user, dtype=np.float32)


# In[43]:

mean_rating_user_array[:5]


# In[44]:

# Save this result as a csv file 
np.savetxt("mean_rating_user.csv", 
           mean_rating_user_array, fmt="%3f", delimiter=",")

