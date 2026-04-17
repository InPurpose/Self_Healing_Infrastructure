CREATE TABLE IF NOT EXISTS staging_seller (
    seller_id TEXT,
    seller_zip_code_prefix TEXT,
    seller_city TEXT,
    seller_state TEXT
);

TRUNCATE staging_seller;

\copy staging_seller FROM 'data/olist/olist_sellers_dataset.csv' CSV HEADER

INSERT INTO geolocation(
    zipcode,
    city,
    state
)
SELECT DISTINCT On(seller_zip_code_prefix)
    LPAD(seller_zip_code_prefix, 5, '0'),
    seller_city,
    seller_state
FROM staging_seller
WHERE LPAD(seller_zip_code_prefix, 5, '0') NOT IN (
    SELECT zipcode FROM geolocation
);

INSERT INTO seller (
    seller_id,
    seller_zipcode,
    seller_city,
    seller_state
)
SELECT
    seller_id,
    LPAD(seller_zip_code_prefix, 5, '0'),
    seller_city,
    seller_state
FROM staging_seller;

DROP TABLE IF EXISTS staging_seller;
