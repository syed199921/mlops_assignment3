import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load raw data
df = pd.read_csv("raw_crypto_data.csv")

# Drop rows with missing values
df_clean = df.dropna()

# Select numeric fields to normalize
numeric_cols = ['current_price', 'market_cap', 'total_volume',
                'price_change_percentage_24h', 'circulating_supply']

# Initialize scaler
scaler = MinMaxScaler()

# Normalize numeric fields
df_clean[numeric_cols] = scaler.fit_transform(df_clean[numeric_cols])

# Optional: keep only necessary columns
columns_to_keep = ['timestamp', 'id', 'symbol'] + numeric_cols
df_processed = df_clean[columns_to_keep]

# Save to processed_data.csv
df_processed.to_csv("processed_crypto_data.csv", index=False)

print("Preprocessing complete. Processed data saved to processed_data.csv.")
