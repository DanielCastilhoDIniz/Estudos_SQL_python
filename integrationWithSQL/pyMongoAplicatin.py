from sqlalchemy import create_engine, MetaData
from sqlalchemy import create_engine, Table
from sqlalchemy import create_engine, Column
from sqlalchemy import create_engine, Integer
from sqlalchemy import create_engine, String
from sqlalchemy import create_engine, ForeignKey

engine = create_engine('sqlite:///:memory')
metadata_obj = MetaData(schema='teste')

user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(68)),
    Column('nickname', String(50), nullable=False) 
)

user_prefs = Table(
    'user_prefs',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

for table in metadata_obj.sorted_tables:
    print(table)
    
    
print(user_prefs.primary_key)
print(user_prefs.columns)
print(user.columns)
print(metadata_obj.tables)

    