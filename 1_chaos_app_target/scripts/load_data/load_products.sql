-- 1. staging 表
CREATE TABLE IF NOT EXISTS staging_products (
    product_id TEXT,
    product_category_name TEXT,
    product_name_lenght INT,
    product_description_lenght INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- 2. 清空
TRUNCATE staging_products;

-- 3. 导入 CSV
\copy staging_products FROM 'data/olist/olist_products_dataset.csv' CSV HEADER

-- 3.5 
INSERT INTO category (name)
SELECT DISTINCT product_category_name
FROM staging_products
WHERE product_category_name IS NOT NULL
ON CONFLICT (name) DO NOTHING;

-- 4. 插入 product（通过 name 映射到 category_id）
INSERT INTO product (
    product_id,
    product_category_id,
    product_name_length,
    product_description_length,
    product_photos_qty,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm
)
SELECT
    sp.product_id,
    c.category_id,                      -- ⭐ 关键：JOIN 拿 id
    sp.product_name_lenght,
    sp.product_description_lenght,
    sp.product_photos_qty,
    sp.product_weight_g,
    sp.product_length_cm,
    sp.product_height_cm,
    sp.product_width_cm
FROM staging_products sp
LEFT JOIN category c
    ON sp.product_category_name = c.name
WHERE sp.product_id IS NOT NULL
ON CONFLICT (product_id) DO NOTHING;