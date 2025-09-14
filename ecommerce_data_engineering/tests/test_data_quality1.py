#!/usr/bin/env python
# coding: utf-8

# <div style="background-color:#4EA72E;  padding:5px; border-radius:20px;">
#     
#   <p style="color:#DC2512; text-align:center; font-size:40px;"> Test_data_quality  </p>
#  
# </div>

# <div style="background-color:#17DCD7;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#D67218; text-align:center; font-size:20px;"> Import Library  </p>
#  
# </div>

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# <div style="background-color:#17DCD7;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#D67218; text-align:center; font-size:20px;"> Insert Data  </p>
#  
# </div>

# In[2]:


customers=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_customers_dataset.csv')

geo=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_geolocation_dataset.csv')
order_items=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_order_items_dataset.csv')
order_payments=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_order_payments_dataset.csv')
order_reviews=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_order_reviews_dataset.csv')
order_dataset=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_orders_dataset.csv')
products=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_products_dataset.csv')
sellers=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/olist_sellers_dataset.csv')
category_translation=pd.read_csv('/Users/Ahmad/ecommerce_data_engineering/Raw_data/product_category_name_translation.csv')


# <div style="background-color:#17DCD7;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#D67218; text-align:center; font-size:20px;"> order_items </p>
#  
# </div>

# In[3]:


Q99 = order_items['freight_value'].quantile(.99)
outliers = order_items[(order_items['freight_value'] >= Q99)]
print(outliers['freight_value'])
print("Q99:",  Q99)
print("outlier_freight_value99:",outliers['freight_value'].value_counts().sum())
order_items=order_items[order_items['freight_value']<Q99]
print(order_items['freight_value'])


# In[4]:


order_items[order_items['freight_value']<0].value_counts().sum()


# <div style="background-color:#92D050;  padding:10px; border-radius:5px;">
#     
#   <p style="color:#EB2213; text-align:center; font-size:15px;"> Cleaning </p>
#  
# </div>

# In[5]:


filtered_df = order_items[order_items['freight_value']>=Q99]
order_items = order_items.drop(index=filtered_df.index)
order_items['shipping_limit_date']=pd.to_datetime(order_items['shipping_limit_date'])


# <div style="background-color:#17DCD7;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#D67218; text-align:center; font-size:20px;"> order_reviews</p>
#  
# </div>

# <div style="background-color:#92D050;  padding:10px; border-radius:5px;">
#     
#   <p style="color:#EB2213; text-align:center; font-size:15px;"> Cleaning </p>
#  
# </div>

# In[6]:


order_reviews['review_comment_title']=order_reviews['review_comment_title'].fillna('NoTitle')
order_reviews['review_comment_message']=order_reviews['review_comment_message'].fillna('Nomessage')


# <div style="background-color:#17DCD7;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#D67218; text-align:center; font-size:20px;"> order_dataset</p>
#  
# </div>

# In[7]:


order_dataset['order_purchase_timestamp']=pd.to_datetime(order_dataset['order_purchase_timestamp'])
order_dataset['order_approved_at']=pd.to_datetime(order_dataset['order_approved_at'])
order_dataset['order_delivered_carrier_date']=pd.to_datetime(order_dataset['order_delivered_carrier_date'])
order_dataset['order_delivered_customer_date']=pd.to_datetime(order_dataset['order_delivered_customer_date'])
order_dataset['order_estimated_delivery_date']=pd.to_datetime(order_dataset['order_estimated_delivery_date'])


# In[8]:


order_dataset['start_end']=order_dataset['order_delivered_carrier_date']>order_dataset['order_delivered_customer_date']


# In[9]:


print("Outlier:", order_dataset['start_end'])


# In[10]:


True_Raws=order_dataset[order_dataset['start_end']==True]
print("True_Raws:", True_Raws[['order_delivered_carrier_date','order_delivered_customer_date' ]])
print("True_Raws_number:",True_Raws.value_counts().sum())


# In[11]:


print("outlier_date:", (order_dataset['order_delivered_carrier_date']>order_dataset['order_delivered_customer_date']).value_counts().sum)


# <div style="background-color:#92D050;  padding:10px; border-radius:5px;">
#     
#   <p style="color:#EB2213; text-align:center; font-size:15px;"> Cleaning </p>
#  
# </div>

# In[12]:


order_dataset['order_purchase_timestamp']=pd.to_datetime(order_dataset['order_purchase_timestamp'])
order_dataset['order_approved_at']=pd.to_datetime(order_dataset['order_approved_at'])
order_dataset['order_delivered_carrier_date']=pd.to_datetime(order_dataset['order_delivered_carrier_date'])
order_dataset['order_delivered_customer_date']=pd.to_datetime(order_dataset['order_delivered_customer_date'])
order_dataset['order_estimated_delivery_date']=pd.to_datetime(order_dataset['order_estimated_delivery_date'])


# In[13]:


filtered_order_dataset = order_dataset[order_dataset['order_delivered_carrier_date']>order_dataset['order_delivered_customer_date']]
order_dataset = order_dataset.drop(index=filtered_order_dataset.index)


# In[14]:


order_dataset=order_dataset.dropna(subset=['order_approved_at','order_delivered_carrier_date','order_delivered_customer_date'])


# <div style="background-color:#17DCD7;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#D67218; text-align:center; font-size:20px;"> products</p>
#  
# </div>

# <div style="background-color:#92D050;  padding:10px; border-radius:5px;">
#     
#   <p style="color:#EB2213; text-align:center; font-size:15px;"> Cleaning </p>
#  
# </div>

# In[15]:


products=products.dropna(subset=['product_category_name', 'product_name_lenght','product_description_lenght','product_photos_qty','product_weight_g'])


# <div style="background-color:#37B3B3;  padding:10px; border-radius:5px;">
#     
#   <p style="color:#D67218; text-align:center; font-size:15px;"> Save File </p>
#  
# </div>

# In[16]:


geo.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Geo_clean.csv", index=False)


# In[17]:


customers.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Customers_clean.csv", index=False)


# In[18]:


order_items.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Order_items_clean.csv", index=False)


# In[19]:


order_payments.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Order_payments_clean.csv", index=False)


# In[20]:


order_reviews.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Order_reviews_clean.csv", index=False)


# In[21]:


order_dataset.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Order_dataset_clean.csv", index=False)


# In[22]:


products.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Products_clean.csv", index=False)


# In[23]:


sellers.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Sellers_clean.csv", index=False)


# In[24]:


category_translation.to_csv("/Users/Ahmad/ecommerce_data_engineering/Clean_data/Category_translation_clean.csv", index=False)


# <div style="background-color:#D96211;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#0CE307; text-align:center; font-size:20px;"> Model Data </p>
#  
# </div>

# In[25]:


order1=pd.merge(order_items,order_payments[['order_id', 'payment_value']], on='order_id', how='left')


# In[26]:


order_fact=pd.merge(order1,order_reviews[['order_id','review_score']], on='order_id', how='left')


# In[27]:


customer_dim=pd.merge(order_dataset, customers, on='customer_id', how='right')


# In[28]:


seller_dim=sellers


# In[29]:


product_dim=pd.merge(products,category_translation,on='product_category_name', how='inner')


# <div style="background-color:#647CD6;  padding:10px; border-radius:10px;">
#     
#   <p style="color:#0CE307; text-align:center; font-size:20px;"> Validation </p>
#  
# </div>

# In[30]:


assert order_fact["order_id"].isin(order_items["order_id"]).all()
print("relation between order_fact and order item holds.")



# In[31]:


missing_products = order_fact[~order_fact["product_id"].isin(product_dim["product_id"])]
#print(f"Products missing from product_dim: {missing_products['product_id'].unique()}")

order_fact_filtered = order_fact[order_fact["product_id"].isin(product_dim["product_id"])]

order_fact=order_fact_filtered


# In[32]:


assert order_fact["product_id"].isin(product_dim["product_id"]).all()

print("relation between order_fact and product_dim holds.")
# In[33]:


assert order_fact["seller_id"].isin(seller_dim["seller_id"]).all()
print("relation between order_fact and seller_dim holds.")

# In[34]:


missing_customers = order_fact[~order_fact["order_id"].isin(customer_dim["order_id"])]
#print(f"Products missing from product_dim: {missing_products['product_id'].unique()}")

order_fact_filtered = order_fact[order_fact["order_id"].isin(customer_dim["order_id"])]

order_fact=order_fact_filtered


# In[35]:


assert order_fact["order_id"].isin(customer_dim["order_id"]).all()
print("relation between order_fact customer_dim holds.")

