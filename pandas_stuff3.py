#%% 
import random
import numpy as np
import pandas as pd
import matplotlib 

MAX_OBSERVATIONS = 100
MAX_PRODUCTS = 5
MAX_ORDERS = 30

products = ['product ' + str(i) for i in range(MAX_PRODUCTS)]
orders = ['order ' + str(i) for i in range(MAX_ORDERS)]


df = pd.DataFrame({
         'products': [products[random.randint(0,len(products) - 1)] for _ in range(MAX_OBSERVATIONS)],
         'orders': [orders[random.randint(0,len(orders) - 1)] for _ in range(MAX_OBSERVATIONS)],
         'quantity': [random.randint(54,189) for _ in range(MAX_OBSERVATIONS)]
        })

# add rank
df['percentage'] = (df['quantity'] / df['quantity'].sum() ) * 100

df_cat_prod = df.groupby(['products', 'orders']).agg({'quantity': 'sum'})
df_cat_prod["quantity_perc"] = df_cat_prod.groupby(level = 'products')['quantity'].apply( lambda x: 100 * x / float(x.sum()))
df_cat_prod["rank_in_product"] = df_cat_prod.groupby(level = 'products')['quantity_perc'].rank()
df_cat_prod["rank"] = df_cat_prod['quantity_perc'].rank()
print(df_cat_prod)

"""
df_cat_percs = df_cat_prod.groupby(level = 'products').apply( lambda x: 100 * x / float(x.sum()))
# reset_index reseteaza indexul si asa avem toate coloanele
df_cat_percs = df_cat_percs.reset_index().rename( columns = {'quantity':'perc'})

# where condition
df_prod0 = df_cat_percs[df_cat_percs["products"] == 'product 0']

print(df_cat_percs)
"""