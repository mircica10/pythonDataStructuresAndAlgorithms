#%% 
import random
import numpy as np
import pandas as pd
import matplotlib 

MAX_OBSERVATIONS = 20
MAX_PRODUCTS = 20
MAX_CATEGORY = 3

products = ['product ' + str(i) for i in range(MAX_PRODUCTS)]
categories = ['category ' + str(i) for i in range(MAX_CATEGORY)]
prices = [random.randint(54,189) for _ in range(MAX_PRODUCTS)]


df = pd.DataFrame({
         'products': products,
         'categories': [categories[random.randint(0,len(categories) - 1)] for _ in range(MAX_OBSERVATIONS)],
         'prices': prices
        })

# add a new column in data frame
df['comb'] = df['products'] + '-' + df['categories']
# add rank
df['rank'] = df.groupby('categories')['prices'].rank()
df['percentage'] = (df['prices'] / df['prices'].sum() ) * 100

df.sort_values(by = 'percentage', ascending=False, inplace=True)

df_cat_prod = df.groupby(['categories', 'products']).agg(avg_price = ('prices', np.mean))
df_cat = df_cat_prod.groupby(['categories']).agg(avg_price = ('avg_price', np.mean))
dt = df_cat_prod.div(df_cat, level = 'categories') * 100
dt = dt.reset_index()

print(dt.reset_index())

df.plot(x = 'products', y = 'prices', kind = 'bar')
df.plot(x = 'categories', y = 'prices', kind = 'bar')

df.plot(x = 'comb' , y = 'prices', kind = 'bar')
# grou by category
df_category_gb = df.groupby('categories', as_index = False).agg(
    min_price = ('prices', 'min'),
    max_price = ('prices', 'max'),
    avg_price = ('prices', np.mean)    
)


# print(df_category_gb)

df_category_gb.plot(x='categories' ,y = ['max_price', 'min_price', 'avg_price'], kind = 'bar')
