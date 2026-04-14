import csv
import os

from dotenv import load_dotenv

from sqlmodel import Session, select, create_engine
from sqlalchemy import Engine

from src.models.category import Category


load_dotenv()


def load_category(csv_path: str, engine:Engine):

    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        # print([row for row in reader])
        # return
        with Session(engine) as session:

            categories = []

            for row in reader:
                try:
                    if row["product_category_name"]:
                        categories.append(
                            Category(
                                name = row["product_category_name"],
                                name_english=row["product_category_name_english"]
                            )
                        )
                except Exception as e:
                    print(f"skip category: {row.get('product_category_name')} error={e}")

            existing = session.exec(select(Category.name)).all()
            existing_set = set(existing)

            new_categories = [
                row
                for row in categories
                if row.name not in existing_set
            ]

            session.add_all(new_categories)
            session.commit()
        

def main():

    DATABASE_URL: str | None = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
       raise ValueError("DATABASE_URL is not set")

    engine = create_engine(DATABASE_URL, echo=True)

    load_category(csv_path="data/olist/product_category_name_translation.csv",engine=engine)

if __name__ == "__main__":
    main()

