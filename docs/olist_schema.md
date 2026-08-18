# Olist Dataset Schema

## 1. customers

| Column | Data Type | Description |
|---|---|---|
| customer_id | string | Unique customer identifier |
| customer_unique_id | string | Unique customer identifier across orders |
| customer_zip_code_prefix | integer | Customer ZIP code prefix |
| customer_city | string | Customer city |
| customer_state | string | Customer state |

## 2. orders

| Column | Data Type | Description |
|---|---|---|
| order_id | string | Unique order identifier |
| customer_id | string | Customer identifier |
| order_status | string | Order status |
| order_purchase_timestamp | datetime | Purchase timestamp |
| order_approved_at | datetime | Approval timestamp |
| order_delivered_carrier_date | datetime | Carrier delivery date |
| order_delivered_customer_date | datetime | Customer delivery date |
| order_estimated_delivery_date | datetime | Estimated delivery date |