import streamlit as st
import pandas as pd
import pickle
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv('/Users/muthu/OneDrive/Desktop/Python/Swiggy Recommendation system/cleaned_data.csv')
encoded_df = pd.read_csv('/Users/muthu/OneDrive/Desktop/Python/Swiggy Recommendation system/encoded_data.csv')

# Load encoder
with open('/Users/muthu/OneDrive/Desktop/Python/Swiggy Recommendation system/encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

# Train KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
df["cluster"] = kmeans.fit_predict(encoded_df)

# Streamlit UI
st.title("🍽️ Restaurant Recommendation Engine")

# Sidebar inputs
city = st.sidebar.selectbox("City", sorted(df["City"].unique()))
cuisine = st.sidebar.selectbox("Cuisine", sorted(df["cuisine"].unique()))
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 3.5)
max_cost = st.sidebar.slider("Maximum Cost", 100, 1000, 500)

if st.sidebar.button("Search Restaurants"):
    # Filter
    filtered_df = df[
        (df["City"] == city) &
        (df["cuisine"].str.lower() == cuisine.lower()) &
        (df["rating"] >= min_rating) &
        (df["cost"] <= max_cost)
    ]

    if not filtered_df.empty:
        st.subheader("Recommended Restaurants")
        for _, row in filtered_df.head(5).iterrows():
            st.markdown(f"""
            ### {row['name']}
            - 📍 City: {row['City']}
            - 🍽️ Cuisine: {row['cuisine']}
            - ⭐ Rating: {row['rating']} ({row['rating_count']} reviews)
            - 💰 Cost: ₹{row['cost']}
            - 🏠 Address: {row['address']}
            """)
    else:
        st.warning("No restaurants match your filters.")
else:
    st.info("Set your preferences and click 'Search Restaurants'.")
