from sqlalchemy import create_engine, text
# import pyodbc
# +pyodbc

Server = 'BPLDEVDB01'
Database = 'sheikh_s'
Driver = 'ODBC Driver 17 for SQL Server'
Database_con =  f'mssql://{Server}/{Database}?driver={Driver}'

engine = create_engine(Database_con)


with engine.connect() as conn:
  result = conn.execute(text('select * from customers with (nolock)'))
  print(result.all())
