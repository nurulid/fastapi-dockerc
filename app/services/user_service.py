from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.models.database import User
from app.schema.user import UserCreate

# Endpoint to create a new user

# ini menggunakan cara "with Session engine" untuk memastikan session ditutup secara otomatis
# setelah selesai digunakan, sehingga tidak perlu menutup session secara manual
# ini juga memastikan bahwa session akan ditutup meskipun terjadi error di dalam blok kode tersebut
# def create_user(user: UserCreate):
#   with Session(engine) as session:
#     db_user = User(**user.model_dump())

#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return db_user

# ini menggunakan cara *dependency injection untuk mendapatkan session dari FastAPI
# sehingga tidak perlu membuat session secara manual
def create_user(db_session: Session, user: UserCreate):
  new_user = User(**user.model_dump()) # ini akan membuat instance User dari data yang diberikan
  # model_dump() digunakan untuk mengubah data Pydantic menjadi dictionary yang sesuai dengan model
  # **user.model_dump() ini sama dengan:
  # new_user = User(full_name=user.full_name, email=user.email, password=user.password)
  # jadi kita tidak perlu menulis satu per satu fieldnya
  # ini juga akan mengisi field yang tidak diberikan dengan nilai defaultnya
  # misalnya full_name akan diisi dengan "" jika tidak diberikan

  db_session.add(new_user)
  db_session.commit()
  db_session.refresh(new_user)
  return new_user

# Endpoint to get a specific user by ID
def get_user(db_session: Session, user_id: str):
  # cara pertama untuk mendapatkan post dari user, mwnggunakan selectinload
  # ini akan mengambil user beserta postnya dalam satu query
  # ini akan mengurangi jumlah query yang dilakukan ke database
  # sehingga lebih efisien, terutama jika jumlah postnya banyak
  # selectinload akan melakukan query terpisah untuk mengambil post dari user
  # sehingga tidak akan mempengaruhi performa jika jumlah postnya sedikit
  # cara paling umum digunakan
  statement = select(User).options(selectinload(User.posts)).where(User.id == user_id)
  return db_session.exec(statement).first()

  # cara kedua, lazy load
  # ini akan mengambil user terlebih dahulu, kemudian mengambil postnya
  # statement = select(User).where(User.id == user_id)
  # user = db_session.exec(statement).first()

  # _ = user.posts # lazy query, ini akan memicu query untuk mengambil post dari user
  # jika tidak ada post, maka akan mengembalikan list kosong
  # return user

# Endpoint to get all users
def get_users(db_session: Session):
  return db_session.exec(select(User)).all()
