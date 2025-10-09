import psycopg2

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'tradingdb',
    'user': 'tradinguser',
    'password': 'tradingpass'
}

TABLES_SQL = [

    """
    CREATE TABLE IF NOT EXISTS assets (
        id SERIAL PRIMARY KEY,
        Ticker TEXT UNIQUE
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS market_data (
        id SERIAL PRIMARY KEY,
        Date TIMESTAMP,
        Ticker VARCHAR,
        Close FLOAT,
        Open FLOAT,
        High FLOAT,
        Low FLOAT,
        Volume FLOAT,
        CONSTRAINT unique_ticker_date UNIQUE (Date, Ticker)
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS features (
        id SERIAL PRIMARY KEY,
        Date TIMESTAMP,
        Ticker VARCHAR,
        distance_ma_50_9 FLOAT,
        distance_ma_100_9 FLOAT,
        distance_ma_9_25 FLOAT,
        distance_ma_50_25 FLOAT,
        distance_ma_100_25 FLOAT,
        distance_ma_100_50 FLOAT,
        roc_8 FLOAT,
        roc_52 FLOAT,
        Vol_52 FLOAT,
        Momentum_Ajusted_Vol_52 FLOAT,
        Perf_ytd FLOAT
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS trades (
        id SERIAL PRIMARY KEY,
        Date TIMESTAMP,
        Ticker VARCHAR,
        quantity FLOAT,
        strategy VARCHAR,
        status VARCHAR
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS backtest (
        id SERIAL PRIMARY KEY,
        start_date TIMESTAMP,
        end_date TIMESTAMP,
        Ticker VARCHAR,
        strategy VARCHAR,
        return_total FLOAT,
        sharpe_ratio FLOAT,
        max_drawdown FLOAT,
        log TEXT
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS model_prediction (
        id SERIAL PRIMARY KEY,
        Date TIMESTAMP,
        asset_id INTEGER REFERENCES assets(id),
        prediction FLOAT,
        model_version FLOAT
    );
    """

]


def create_tables():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for table_sql in TABLES_SQL:
            cursor.execute(table_sql)

        conn.commit()
        print("✅ Tables créées avec succès.")

    except Exception as e:
        print("❌ Erreur lors de la création des tables :", e)

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    create_tables()
