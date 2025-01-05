from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+pymysql://root:''@localhost/apicrud"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
