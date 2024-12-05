from sqlalchemy import create_engine
import pandas as pd

# Connecting to PostgreSQL and extracting data:
postgres_engine = create_engine('postgresql+psycopg2://postgres:123456789@localhost:5432/mydb')
customers_df = pd.read_sql("SELECT * FROM customers", postgres_engine)
print("Data PostgreSQL:")
print(customers_df)

# Connecting to MySQL and extracting data:
mysql_engine = create_engine('mysql+pymysql://root:123456789@localhost:3306/mydb')
sales_df = pd.read_sql("SELECT * FROM sales", mysql_engine)
print("Data MySQL:")
print(sales_df)

# Save to Parquet format
customers_df.to_parquet('customers.parquet', index=False)
sales_df.to_parquet('sales.parquet', index=False)
print(" Parquet File ")