from sqlmodel import Field, SQLModel, create_engine

# class HeroBase(SQLModel):
#     name: str
#     age: int | None = None

# class Hero(HeroBase, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     # name: str
#     secret_name: str
#     # age: int | None = None

# class HeroPublic(HeroBase,):
#     test:str

# # Code above omitted 👆

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)


class HeroCreate(SQLModel):
    name: str
    secret_name: str
    age: int | None = None


class HeroPublic(SQLModel):
    id: int
    name: str
    secret_name: str
    age: int | None = None

# Code below omitted 👇