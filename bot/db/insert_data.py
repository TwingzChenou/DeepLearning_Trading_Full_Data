import os
import glob
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'tradingdb',
    'user': 'tradinguser',
    'password': 'tradingpass'
}

DATA_DIR = '/Users/forget/PycharmProjects/PythonProject/PythonProject/DeepLearning_Trading/data/'

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def insert_assets(df, cursor):
    tickers = df['Ticker'].unique()
    for ticker in tickers:
        try:
            cursor.execute(
                "INSERT INTO assets (Ticker) VALUES (%s) ON CONFLICT (Ticker) DO NOTHING;",
                (ticker,)
            )
        except Exception as e:
            print(f"❌ Erreur insertion asset {ticker} :", e)

def insert_market_data(df, cursor):
    records = df[['Date', 'Ticker', 'Close', 'Open', 'High', 'Low', 'Volume']].dropna()
    tuples = [tuple(x) for x in records.to_numpy()]
    try:
        execute_values(cursor,
            """
            INSERT INTO market_data (Date, Ticker, Close, Open, High, Low, Volume)
            VALUES %s
            ON CONFLICT DO NOTHING;
            """, tuples
        )
    except Exception as e:
        print("❌ Erreur insertion données marché :", e)

def main():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        parquet_files = glob.glob(os.path.join(DATA_DIR, '*.parquet'))

        for file in parquet_files:
            print(f"📂 Lecture de {file}")
            df = pd.read_parquet(file, engine='auto')
            df['Date'] = pd.to_datetime(df['Date'])

            insert_assets(df, cursor)
            insert_market_data(df, cursor)

        conn.commit()
        print("✅ Données insérées avec succès.")
    except Exception as e:
        print("❌ Erreur lors de l'insertion :", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()