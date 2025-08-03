from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained KNN model and product data
model, df = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    product_list = df['ProductID'].tolist()
    return render_template("index.html", products=product_list)

@app.route("/recommend", methods=["POST"])
def recommend():
    selected_product = request.form["product"]

    # Get product features
    product_features = df[df['ProductID'] == selected_product][['Price', 'Rating', 'Popularity', 'Category', 'Brand']].values

    # Find nearest neighbors
    distances, indices = model.kneighbors(product_features)

    # Get recommended products (excluding the selected one itself)
    recommended_products = df.iloc[indices[0][1:]][['ProductID', 'Price', 'Rating', 'Popularity']].to_dict(orient='records')

    return render_template("result.html", selected_product=selected_product, recommendations=recommended_products)

if __name__ == "__main__":
    app.run(debug=True)
