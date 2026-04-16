-- 1. 创建 staging 表（如果不存在）
CREATE TABLE IF NOT EXISTS staging_location (
    geolocation_zip_code_prefix TEXT,
    geolocation_lat FLOAT,
    geolocation_lng FLOAT,
    geolocation_city TEXT,
    geolocation_state TEXT
);

-- 2. 清空 staging（防止重复跑）
TRUNCATE staging_location;

-- 3. 导入 CSV（psql 专用命令）
\copy staging_location FROM 'data/olist/olist_geolocation_dataset.csv' CSV HEADER


-- 4. 插入到正式表（去重）
INSERT INTO geolocation (
    zipcode, 
    latitude,
    longitude,
    city,
    state
    )
SELECT DISTINCT
    geolocation_zip_code_prefix,
    geolocation_lat,
    geolocation_lng,
    geolocation_city,
    geolocation_state
FROM staging_location
-- WHERE product_category_name IS NOT NULL
ON CONFLICT (zipcode) DO NOTHING;


-- 5. drop table
DROP TABLE IF EXISTS staging_location;
