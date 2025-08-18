# MiniProject4---Swiggy-s-Restaurant-Recommendation-System-using-Streamlit
The system should recommend restaurants to users based on input features such as city, rating, cost, and cuisine preferences. The application will utilize clustering or similarity measures to generate recommendations and display results in an easy-to-use Streamlit interface
Approach:
●	The dataset is provided as a CSV file with the following columns:
●	['id', 'name', 'city', 'rating', 'rating_count', 'cost', 'cuisine',
●	 'lic_no', 'link', 'address', 'menu']
●	Categorical: name, city, cuisine
●	Numerical: rating, rating_count, cost
1. Data Understanding and Cleaning
●	Duplicate Removal: Identify and drop duplicate rows.
●	Handling Missing Values: Impute or drop rows with missing values.
●	Save the cleaned data to a new CSV file (cleaned_data.csv).
2. Data Preprocessing
●	Encoding: Apply One-Hot Encoding to categorical features (name, city, cuisine).
○	Save the encoder as a Pickle file (encoder.pkl).
●	Ensure all features are numerical after encoding.
●	Create a preprocessed dataset (encoded_data.csv).
●	Ensure the indices of cleaned_data.csv and encoded_data.csv match.
3. Recommendation Methodology
●	Clustering or Similarity Measures:
○	Use K-Means Clustering or Cosine Similarity to identify similar restaurants based on input features.
○	Use the encoded dataset for computations.
●	Result Mapping:
○	Map the recommendation results (indices) back to the non-encoded dataset (cleaned_data.csv).
4. Streamlit Application
●	Build an interactive application with the following components:
○	User Input: Accept user preferences (e.g., city, cuisine, rating,price,etc).
○	Recommendation Engine: Process the input, query the encoded data, and generate recommendations.
○	Output: Display recommended restaurants using cleaned_data.csv.

Results: 
●	Data Preprocessing
○	Cleaned Dataset (cleaned_data.csv):
■	Categorical and numerical features with missing values and duplicates removed.
○	Encoded Dataset (encoded_data.csv):
■	Preprocessed numerical dataset with categorical features One-Hot Encoded.
○	Encoder File (encoder.pkl):
■	Serialized One-Hot Encoder for Streamlit use.
●	Recommendation System
○	Clustering or Similarity-based recommendation engine.
○	Mapping results from encoded_data.csv to cleaned_data.csv for interpretation.
●	Streamlit Application
○	User-friendly interface for input and output.
○	Clear display of recommendations from the cleaned dataset.

