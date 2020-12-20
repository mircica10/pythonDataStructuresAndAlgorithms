#%% 
import random
import numpy as np
import pandas as pd
import matplotlib 

MAX = 100

df = pd.DataFrame(
        {'name': [ ['dp1', 'dp2', 'dp3', 'dp4'][random.randint(0,3)] for _ in range(0,MAX)],
         'category': [ ['cat1', 'cat2', 'cat3'][random.randint(0,2)] for _ in range(0,MAX)],
         'val1': [random.randint(60, 99) for _ in range(0,MAX)],
         'val2': [random.randint(200, 500) for _ in range(0,MAX)]         
        })
            
print(df)

df.plot(kind = 'bar')

# we do the group by name and category
df_groupby = df.groupby(['name','category'])['val1','val2'].sum()

print(df_groupby)

df_groupby.plot(kind = 'bar')

# we unstack here the category
df_groupby_unstacked = df_groupby.unstack()

print(df_groupby_unstacked)

df_groupby_unstacked.plot(kind = 'bar')

# this will flatten the group by columns
#df_groupby = df_groupby.reset_index()

# create new column from the group by combination to represent the x axis
#df_groupby['xlabel'] = df_groupby['name'] + '-' + df_groupby['category']

# plot the report
#df_groupby.plot(y = ['val1','val2'], x = 'xlabel' ,kind='bar')

#df_groupby.plot(x = 'name', y = 'category', kind='bar')

#df.plot(kind = 'bar')


#df_gb.plot(x = 'name', y=['category', 'val1', 'val2'],kind = 'bar')

# %%


# %%

