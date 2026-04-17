CREATE TABLE IF NOT EXISTS staging_customer (
    customer_id TEXT,
    customer_unique_id TEXT,
    customer_zip_code_prefix TEXT,
    customer_city TEXT,
    customer_state TEXT
);

TRUNCATE staging_customer;

\copy staging_customer FROM 'data/olist/olist_customers_dataset.csv' CSV HEADER

INSERT INTO geolocation(
    zipcode,
    city,
    state
)
SELECT DISTINCT On(customer_zip_code_prefix)
    LPAD(customer_zip_code_prefix, 5, '0'),
    customer_city,
    customer_state
FROM staging_customer
WHERE LPAD(customer_zip_code_prefix, 5, '0') NOT IN (
    SELECT zipcode FROM geolocation
);

-- INSERT INTO geolocation (
--     zipcode,
--     city,
--     state
-- )
-- SELECT DISTINCT ON (customer_zip_code_prefix)
--     LPAD(TRIM(customer_zip_code_prefix), 5, '0'),
--     customer_city,
--     customer_state
-- FROM staging_customer
-- WHERE customer_zip_code_prefix IS NOT NULL
-- ON CONFLICT (zipcode)
-- DO UPDATE SET
--     city = COALESCE(EXCLUDED.city, geolocation.city),
--     state = COALESCE(EXCLUDED.state, geolocation.state);


INSERT INTO customer (
    customer_id,
    customer_unique_id,
    customer_zipcode,
    customer_city,
    customer_state
)
SELECT
    customer_id,
    customer_unique_id,
    LPAD(customer_zip_code_prefix, 5, '0'),
    customer_city,
    customer_state
FROM staging_customer
ON CONFLICT (customer_id) DO NOTHING;
DROP TABLE IF EXISTS staging_customer;
