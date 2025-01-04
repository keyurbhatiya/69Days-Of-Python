from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/your_database"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
