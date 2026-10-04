import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie dataset
movies = pd.read_csv("dataset/movies.csv")

print("Dataset loaded successfully!")
print("Number of movies:", len(movies))

# Handle missing genres
movies["genres"] = movies["genres"].fillna("")

# Convert genres into TF-IDF features
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(movies["genres"])

print("TF-IDF matrix created!")

# Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix)

print("Similarity matrix created!")

# Create an index of movie titles
indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()


def recommend_movies(title, number=5):

    if title not in indices:
        print("\nMovie not found.")
        return

    idx = indices[title]

    similarity_scores = list(enumerate(cosine_sim[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Remove the selected movie
    similarity_scores = similarity_scores[1:number + 1]

    print("\n--------------------------------")
    print("Recommended Movies")
    print("--------------------------------")
    print("Because you selected:", title)
    print()

    for i, score in similarity_scores:
        movie_name = movies.iloc[i]["title"]
        print(f"{movie_name} (similarity: {score:.2f})")


# Get movie from user
movie = input("Enter a movie title: ").strip()

# Allow partial movie-name search
matches = movies[
    movies["title"].str.contains(
        movie,
        case=False,
        na=False,
        regex=False
    )
]

if len(matches) == 0:

    print("\nMovie not found.")
    print("\nHere are some available movies:")
    print(movies["title"].head(20).to_string(index=False))

else:

    selected_movie = matches.iloc[0]["title"]

    print("\nSelected movie:", selected_movie)

    recommend_movies(selected_movie)
