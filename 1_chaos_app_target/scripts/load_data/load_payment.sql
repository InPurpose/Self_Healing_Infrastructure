-- 1. staging
CREATE TABLE IF NOT EXISTS staging_payment (
    order_id TEXT,
    payment_sequential INT,
    payment_type TEXT,
    payment_installments INT,
    payment_value FLOAT
);

-- 2. 清空
TRUNCATE staging_payment;

-- 3. 导入
\copy staging_payment FROM 'data/olist/olist_order_payments_dataset.csv' CSV HEADER

-- 4. 插入
INSERT INTO orderpayment (
    order_id,
    payment_sequential,
    payment_type,
    payment_installment,
    payment_value
)
SELECT
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
FROM staging_payment
WHERE order_id IS NOT NULL
ON CONFLICT (order_id, payment_sequential) DO NOTHING;

-- 5. 清理
DROP TABLE IF EXISTS staging_payment;