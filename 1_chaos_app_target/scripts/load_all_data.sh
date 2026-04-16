#!/bin/bash

set -e  # 有错误就停止

DB_NAME="chaosapp"

echo "🚀 Loading category..."
psql -d $DB_NAME -f scripts/load_data/load_category.sql

echo "🚀 Loading product..."
psql -d $DB_NAME -f scripts/load_data/load_products.sql

echo "🚀 Loading geolocation..."
psql -d $DB_NAME -f scripts/load_data/load_location.sql

echo "✅ All data loaded successfully!"