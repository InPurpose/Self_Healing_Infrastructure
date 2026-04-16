import csv
import os

from sqlmodel import Session, select, create_engine
from sqlalchemy import Engine
from src.models.product import Product


from dotenv import load_dotenv

load_dotenv()

def to_int(val):
    try:
        return int(val)
    except:
        return 0

def load_products(csv_path: str, engine:Engine):

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # l = [row for row in reader if not row["product_category_name"]]
        # print(len(l))
        # return
        
        with Session(engine) as session:

            BATCH_SIZE = 1000
            batch = []
            
            for row in reader:
                try:
                    batch.append(
                        Product(
                            product_id=row["product_id"],
                            product_category_name=row["product_category_name"] or None,
                            product_name_length=int(row["product_name_lenght"] or 0),
                            product_description_length=int(row["product_description_lenght"] or 0),
                            product_photos_qty=int(row["product_photos_qty"] or 0),
                            product_weight_g=int(row["product_weight_g"] or 0),
                            product_length_cm=int(row["product_length_cm"] or 0),
                            product_height_cm=int(row["product_height_cm"] or 0),
                            product_width_cm=int(row["product_width_cm"] or 0),
                        )
                    )

                    if len(batch) >= BATCH_SIZE:
                        session.add_all(batch)
                        session.commit()
                        batch.clear()

                except Exception as e:
                    print(f"skip row: {row['product_id']} error={e}")

            
            if batch:
                session.add_all(batch)
                session.commit()


def main():

    DATABASE_URL: str | None = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set")

    engine = create_engine(DATABASE_URL, echo=True)

    load_products(csv_path="data/olist/olist_products_dataset.csv",engine=engine)


if __name__ == "__main__":
    main()

