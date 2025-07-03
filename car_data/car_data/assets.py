
import dagster as dg
import polars as pl
import duckdb


CSV_URL = "https://raw.githubusercontent.com/Azure/carprice/refs/heads/master/dataset/carprice.csv"
CSV_PATH = "data/carprice.csv"

DUCKDB_PATH = "data/car_data.duckdb"
TABLE_NAME = "avg_price_per_brand"

@dg.asset
def car_data_file(context: dg.AssetExecutionContext):
    """ Download the car data CSV file from the URL and save it locally. """
    context.log.info('Downloading CSV file')
    
    df = pl.read_csv(CSV_URL)
    df = df.with_columns([
        pl.col("normalized-losses").cast(pl.Float64, strict=False),
        pl.col("price").cast(pl.Float64, strict=False)
    ])

    df.write_csv(CSV_PATH)

@dg.asset(deps=[car_data_file])
def avg_price_table(context: dg.AssetExecutionContext):
    """ Compute average car price per brand and store it in DuckDB."""
    context.log.info('Creating aggregated DuckDB table')

    df = pl.read_csv(CSV_PATH)
    df.drop_nulls(['price'])

    avg_price_df = df.group_by("make").agg(pl.col("price").mean().alias("avg_price"))

    data = [(row['make'], row['avg_price']) for row in avg_price_df.to_dicts()]

    with duckdb.connect(DUCKDB_PATH) as duckdb_conn:
        duckdb_conn.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
        duckdb_conn.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (make TEXT, avg_price DOUBLE)")

        # Insert data into DuckDB table
        duckdb_conn.executemany(f"INSERT INTO {TABLE_NAME} (make, avg_price) VALUES (?, ?)", data)

    duckdb_conn.close()
    
    context.log.info(f"Table '{TABLE_NAME}' created in DuckDB at {DUCKDB_PATH}")