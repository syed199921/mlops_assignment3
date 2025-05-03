import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle
def train_model():
    # Load preprocessed data
    df = pd.read_csv("processed_crypto_data.csv")

    # Define features and target
    features = ['market_cap', 'total_volume', 'price_change_percentage_24h', 'circulating_supply']
    X = df[features]
    y = df['current_price']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")

    # Save model to disk
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved to model.pkl")
    # Load preprocessed data
    df = pd.read_csv("processed_crypto_data.csv")

    # Define features and target
    features = ['market_cap', 'total_volume', 'price_change_percentage_24h', 'circulating_supply']
    X = df[features]
    y = df['current_price']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")

    # Save model to disk
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved to model.pkl")
