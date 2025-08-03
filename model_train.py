import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle

# Load dataset
df = pd.read_csv("products.csv")

# Store product IDs separately
product_ids = df['ProductID']

# Features for similarity
X = df[['Price', 'Rating', 'Popularity', 'Category', 'Brand']]

# KNN model
model = NearestNeighbors(n_neighbors=4, metric='euclidean')
model.fit(X)

# Save model and product IDs
with open("model.pkl", "wb") as f:
    pickle.dump((model, df), f)

print("✅ Model trained and saved as model.pkl")
