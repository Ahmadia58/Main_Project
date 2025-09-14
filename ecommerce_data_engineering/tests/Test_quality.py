import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:1013@localhost:5432/postgres")

def test_no_nulls(table, columns ):
    for col in columns:
        result = pd.read_sql(f"SELECT COUNT(*) FROM {table} WHERE {col} IS NULL", engine)
        assert result.iloc[0,0] == 0, f"NULLs found in customer_id of datawarehouse.customer_dim"

def  test_no_duplicates(table, key_col):
    result = pd.read_sql(f"SELECT {key_col}, COUNT(*) FROM {table} GROUP BY {key_col} HAVING COUNT(*) > 1", engine)
    assert result.empty, f"Duplicates found in {key_col} of {table}"

# Run tests
test_no_nulls("datawarehouse.customer_dim", ["customer_id", "customer_state", "customer_city"])
test_no_duplicates("datawarehouse.orders_fact", "order_id")

print("There arent any null and duplicats")