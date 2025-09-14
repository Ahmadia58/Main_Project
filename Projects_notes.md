========================================🏬 E-commerce Data Warehouse Project============================================
									 
======================================== 📦 Customers (`olist_customers_dataset.csv`)===================================
                     File_Size            Column           Row:                  Null
                        8.6MB               5              99441                   0
Column_name:   customer_id    customer_unique_id   customer_zip_code_prefix  customer_city    customer_state
 Data_Type:      object             object                 int64                 object            object
Outliers:
 =====================================================================================================================    ======================================🌍 Geo(`olist_geolocation_dataset.csv`)========================================									
                     File_Size             Column           Row:                  Null
                       58.4 MB                5              1000163                0                  
Column_name:  geolocation_zip_code_prefix   geolocation_lat  geolocation_lng  geolocation_city  geolocation_state 
 Data_Type:             int64                   float64          float64           object            object
Outliers:
  =====================================================================================================================                                
====================================== 📦 Order_Items  (`olist_order_items_dataset.csv`)===============================
                     File_Size             Column           Row:                  Null
                        14.7MB               7             112650                   0
Column_name:  order_id   order_item_id   product_id   seller_id  shipping_limit_date  price  freight_value
 Data_Type:    object      int64            object       object         object        float64    float64
Outliers:
  =====================================================================================================================  
======================================💳Order_payments (`olist_order_payments.csv`)====================================
                     File_Size             Column           Row:                  Null
                        5.5MB                5              103886                  0
Column_name: order_id  payment_sequential  payment_type  payment_installments payment_value
 Data_Type:    object      int64                 object         int64             float64
Outliers:
   ===================================================================================================================== 
==================================== 📝 Order_Reviews (`olist_order_reviews_dataset.csv`)===============================
                     File_Size             Column           Row:                  
                       13.8MB                7               99224
Column_name: 
review_id order_id review_score review_comment_title review_comment_message review_creation_date  review_answer_timestamp                    
 Data_Type:
 object    object  int64                object              object                 object              object
Outliers:
Nullity:
0          0           0                87656                 58247                   0                     0
   ===================================================================================================================== ===================================== 📦 Orders_Dataset (`olist_orders_dataset.csv`)====================================
                     File_Size             Column           Row:                 
                        16.8MB               8               99441            
Column_name: 
order_id customer_id  order_status order_purchase_timestamp order_approved_at order_delivered_carrier_date order_delivered_customer_date  order_estimated_delivery_date
 Data_Type:
 object     object       object           object                object                 object
  object                              object
 Nullity: 
 0        0               0                 0                 160                  1783
 2965                              0
Outliers:
  =====================================================================================================================
=================================== 🛒 Products (`olist_products_dataset.csv`)========================================
                     File_Size             Column           Row:                 
                        2.3MB                  9             32951
Column_name:
product_id  product_category_name product_name_lenght product_description_lenght product_photos_qty product_weight_g product_length_cm   product_height_cm  product_width_cm 
 Data_Type:
 object        object                 float64               float64                   float64            float64             float64                float64           float64
 Nullity:
 0               610                       610               610                        610              2                     2                  2                   2
Outliers:
   ===================================================================================================================== 
===================================🏪 Sellers(`olist_sellers_dataset.csv`)==============================================
                     File_Size             Column           Row:                  Null
                         170KB               4              3095                    0
Column_name:  seller_id     seller_zip_code_prefix     seller_city         seller_state 
 Data_Type:    object                 int64               object               object
Outliers:     
  =====================================================================================================================  
===================================🔤 Category_Translation (`product_category_name_translation.csv`)==================
                      File_Size             Column           Row:                  Null
                          2.6KB                 2              71                    0
Column_name: product_category_name                product_category_name_english
 Data_Type:object                                          object
Outliers:
 =====================================================================================================================
======================================Issues for Data Cleaning========================================================

- Null values in `orders.order_delivered_customer_date`=2965
- Negative or zero prices in `order_items`=0
- Inconsistent date types: need to convert all to datetime=ok
- Some `freight_value` seem unusually high=1128
- Duplicate entries in `order_payments=0
 =====================================================================================================================
======================================= Cleaning Log==================================================================
 -- Removed 1128 rows with order_items['freight_value']>=Q99(Quntil(.99))
 -- Fill 87656 row of order_reviews['review_comment_title'] with ('NoTitle')
 -- Fill 58247 row of  order_reviews['review_comment_message'] with ('Nomessage')
 --Change data type order_dataset['order_purchase_timestamp'] to datetime
-- Change data type order_dataset['order_approved_at'] to datetime
-- Change data type order_dataset['order_delivered_carrier_date'] to datetime
-- Change data type order_dataset['order_delivered_customer_date'] to datetime
-- Change data type order_dataset['order_estimated_delivery_date'] to datetime
--  Deleting 23 orders with invalid delivery of order_dataset
--  Removed 3003 rows null values of order_dataset
--  Removed 3003 rows null values of products

- Renamed all columns to lowercase snake_case
 =====================================================================================================================-
======================================= Model Data===================================================================


        Customers                      order_items                       order_payments
  customer_id====> Primary Key       order_id===> Primary Key        order_id===> Primary Key
                                    product_id====>Foreign Key
                                     seller_id====> foreign Key
  
         order_reviews                 order_dataset                 products                    sellers
  review_id====>Primary Key       order_id===> Primary Key    product_id====>Primary Key  seller_id====> Primary Key	
  order_id=====>Foreign Key    customer_id====> Foreign Key
 =====================================================================================================================  
===================================    Quality checklist==============================================================
  1--Are the keys unique? YES
  2--Are there any missing data or outliers? Yes, Specified in the main file.
  3--Are the data types in the columns correct?Yes
  4--Are the relationships between tables valid?Yes
   =====================================================================================================================
  
  
  
  
          


           
   

             

 Data quality



 