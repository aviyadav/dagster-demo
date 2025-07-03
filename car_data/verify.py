import duckdb

conn = duckdb.connect(database="data/car_data.duckdb")

df = conn.execute("from avg_price_per_brand").fetchall()
print(df)