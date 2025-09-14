# 🏬 E-commerce Data Warehouse Project

## 📌 Overview
This project builds a comprehensive data warehouse using real-world e-commerce datasets from Olist. It includes customer data, orders, payments, reviews, products, sellers, and geolocation information. The goal is to clean, model, and prepare the data for advanced analytics and dashboarding.

## 📁 Datasets Included
- **Customers**: Unique customer identifiers and location info.
- **Geolocation**: Latitude and longitude data by zip code.
- **Order Items**: Product-level details per order.
- **Payments**: Payment type and value per order.
- **Reviews**: Customer feedback and scores.
- **Orders**: Full order lifecycle timestamps.
- **Products**: Product metadata and dimensions.
- **Sellers**: Seller location and identifiers.
- **Category Translation**: Mapping of product categories to English.

## 🧹 Data Cleaning Summary
- Removed outliers in `freight_value` and invalid delivery dates.
- Filled missing review titles/messages with placeholders.
- Converted all date columns to datetime format.
- Dropped rows with excessive null values.
- Renamed all columns to lowercase snake_case for consistency.

## 🧠 Data Modeling
Relational links between tables:
- `customer_id` → Orders
- `order_id` → Order Items, Payments, Reviews
- `product_id` → Order Items, Products
- `seller_id` → Order Items, Sellers

## ✅ Quality Checklist
- ✅ Unique keys confirmed
- ✅ Nulls and outliers handled
- ✅ Data types standardized
- ✅ Relationships validated

## 📊 Next Steps
- Build interactive dashboards (e.g., sales performance, customer segmentation)
- Apply machine learning models for prediction and recommendation
- Deploy the warehouse for BI tools like Power BI 


