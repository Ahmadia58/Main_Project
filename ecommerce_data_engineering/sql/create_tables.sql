--------------------------------------------------CREATE SCHEMA--------------------------------------------------
postgres=# CREATE SCHEMA datawarehouse;
--------------------------------------------------CREATE TABLE-----------------------------------------------------

postgres=# CREATE TABLE datawarehouse.order_fact(order_id  TEXT PRIMARY KEY, order_item_id INT, customer_id  TEXT, product_id TEXT, seller_id TEXT, shipping_limit_date TIMESTAMPTZ, price DECIMAL, freight_value  DECIMAL, payment_value DECIMAL,review_score DECIMAL);


postgres-# CREATE TABLE datawarehouse.customer_dim( order_id TEXT,customer_id TEXT PRIMARY KEY, order_status TEXT, order_purchase_timestamp TIMESTAMPTZ, order_approved_at TIMESTAMPTZ, order_delivered_carrier_date TIMESTAMPTZ, order_delivered_customer_date TIMESTAMPTZ, order_estimated_delivery_date TIMESTAMPTZ, customer_unique_id  TEXT,customer_zip_code_prefix INT, customer_city TEXT, customer_state TEXT);

postgres=# CREATE TABLE datawarehouse.product_dim( product_id TEXT PRIMARY KEY,product_category_name TEXT, product_name_lenght DECIMAL, product_description_lenght DECIMAL, product_photos_qty DECIMAL, product_length_cm DECIMAL, product_height_cm DECIMAL, product_width_cm DECIMAL,product_category_name_english TEXT);


postgres=# CREATE TABLE datawarehouse.seller_dim(seller_id TEXT PRIMARY KEY,seller_zip_code_prefix INT,seller_city TEXT,seller_state TEXT);


postgres=# CREATE TABLE datawarehouse.date_dim( date_key INT 
   ,date TIMESTAMPTZ PRIMARY KEY, day  INT, month INT, year  INT, is_weekend  bool);


---------------------------------------------------ALTER TABLE-----------------------------------------------------------

postgres-# ALTER TABLE datawarehouse.customer_dim ADD CONSTRAINT customer_dim_unique_customer_id UNIQUE (customer_id);

postgres=# ALTER TABLE datawarehouse.orders_fact ADD CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES datawarehouse.customer_dim(customer_id);


postgres=# ALTER TABLE datawarehouse.seller_dim ADD CONSTRAINT seller_dim_unique_seller_id UNIQUE (seller_id);

postgres=# ALTER TABLE datawarehouse.orders_fact ADD CONSTRAINT fk_seller FOREIGN KEY (seller_id) REFERENCES datawarehouse.seller_dim(seller_id);


postgres=# ALTER TABLE datawarehouse.product_dim ADD CONSTRAINT product_dim_unique_product_id UNIQUE (product_id);

postgres=# ALTER TABLE datawarehouse.orders_fact ADD CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES datawarehouse.product_dim(product_id);

postgres=# ALTER TABLE datawarehouse.date_dim ADD CONSTRAINT date_dim_unique_date UNIQUE (date);
ALTER TABLE datawarehouse.orders_fact ADD CONSTRAINT fk_date FOREIGN KEY (shipping_limit_date) REFERENCES datawarehouse.date_dim(date);





------------------------------------------QUERY FOR NULL DATA---------------------------

SELECT COUNT(*) FROM datawarehouse.orders_fact
WHERE order_id IS NULL OR shipping_limit_date IS NULL OR price IS NULL OR freight_value IS NULL OR payment_value IS NULL;

SELECT COUNT(*) FROM datawarehouse.product_dim
WHERE product_id IS NULL OR product_category_name_english IS NULL OR product_photos_qty IS NULL;

SELECT COUNT(*) FROM datawarehouse.seller_dim
WHERE seller_id IS NULL OR seller_city IS NULL OR seller_state IS NULL;


SELECT COUNT(*) FROM datawarehouse.customer_dim
WHERE customer_id IS NULL OR order_approved_at IS NULL OR order_delivered_customer_date IS NULL OR customer_city IS NULL OR customer_state IS NULL;


SELECT COUNT(*) FROM datawarehouse.date_dim
WHERE date IS NULL;

--------------------------------------------------- DUPLICATE DATAS-------------------------------------------------- 
SELECT product_id, COUNT(*) 
FROM datawarehouse.product_dim
GROUP BY product_id
HAVING COUNT(*) > 1;

SELECT customer_id, COUNT(*) 
FROM datawarehouse.customer_dim
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT order_id, COUNT(*) 
FROM datawarehouse.orders_fact
GROUP BY order_id
HAVING COUNT(*) > 1;

SELECT date, COUNT(*) 
FROM datawarehouse.date_dim
GROUP BY date_id
HAVING COUNT(*) > 1;

SELECT seller_id, COUNT(*) 
FROM datawarehouse.seller_dim
GROUP BY seller_id
HAVING COUNT(*) > 1;

------------------------------------------------RELATIONS------------------------------------------------------------
SELECT o.customer_id 
FROM datawarehouse.orders_fact o
LEFT JOIN datawarehouse.customer_dim c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

SELECT o.seller_id 
FROM datawarehouse.orders_fact o
LEFT JOIN datawarehouse.seller_dim c ON o.seller_id = c.seller_id
WHERE c.seller_id IS NULL;

SELECT o.product_id 
FROM datawarehouse.orders_fact o
LEFT JOIN datawarehouse.product_dim c ON o.product_id = c.product_id
WHERE c.product_id IS NULL;

SELECT shipping_limit_date
FROM datawarehouse.orders_fact o
LEFT JOIN datawarehouse.date_dim c ON o.shipping_limit_date = c.date
WHERE  c.date  IS NULL;


