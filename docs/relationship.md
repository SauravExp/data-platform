# Relationships

- customers.customer_id → orders.customer_id
- orders.order_id → order_items.order_id
- orders.order_id → order_payments.order_id
- orders.order_id → order_reviews.order_id
- order_items.product_id → products.product_id
- order_items.seller_id → sellers.seller_id
- products.product_category_name → product_category_name_translation.product_category_name