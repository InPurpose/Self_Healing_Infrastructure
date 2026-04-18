-- 1. staging
CREATE TABLE IF NOT EXISTS staging_review (
    review_id TEXT,
    order_id TEXT,
    review_score INT,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMPTZ,
    review_answer_timestamp TIMESTAMPTZ
);

-- 2. 清空
TRUNCATE staging_review;

-- 3. 导入
\copy staging_review FROM 'data/olist/olist_order_reviews_dataset.csv' CSV HEADER

-- 4. 插入
INSERT INTO orderreview (
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message,
    review_creation_date,
    review_answer_timestamp
)
SELECT
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message,
    review_creation_date,
    review_answer_timestamp
FROM staging_review
WHERE review_id IS NOT NULL
ON CONFLICT (review_id) DO NOTHING;

-- 5. 清理
DROP TABLE IF EXISTS staging_review;