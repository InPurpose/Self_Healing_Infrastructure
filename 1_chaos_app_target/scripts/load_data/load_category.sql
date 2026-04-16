-- 1. 创建 staging 表（如果不存在）
CREATE TABLE IF NOT EXISTS staging_category (
    product_category_name TEXT,
    product_category_name_english TEXT
);

-- 2. 清空 staging（防止重复跑）
TRUNCATE staging_category;

-- 3. 导入 CSV（psql 专用命令）
\copy staging_category FROM 'data/olist/product_category_name_translation.csv' CSV HEADER

-- 4. 插入到正式表（去重）
INSERT INTO category (name, name_english)
SELECT DISTINCT
    product_category_name,
    product_category_name_english
FROM staging_category
WHERE product_category_name IS NOT NULL
ON CONFLICT (name) DO NOTHING;