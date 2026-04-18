CREATE TABLE IF NOT EXISTS staging_order_item (
    order_id TEXT,
    order_item_id INT,
    product_id TEXT,
    seller_id TEXT,
    shipping_limit_date TIMESTAMPTZ,
    price FLOAT,
    freight_value FLOAT
);

TRUNCATE staging_order_item;

\copy staging_order_item FROM 'data/olist/olist_order_items_dataset.csv' CSV HEADER

INSERT INTO orderitem(
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value
)
SELECT
    order_id,
    order_item_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value 
FROM staging_order_item
ON CONFLICT (order_id,order_item_id) DO NOTHING;

DROP TABLE IF EXISTS staging_order_item;
