import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load MovieLens dataset


movies = pd.read_csv("dataset/movies.csv")

print("Dataset loaded successfully!")
print("Number of movies:", len(movies))


# 2. Prepare movie genres


movies["genres"] = movies["genres"].fillna("")


# 3. Convert genres into numerical
#    TF-IDF features


tfidf = TfidfVectorizer(
    stop_words="english"
)

tfidf_matrix = tfidf.fit_transform(movies["genres"])

print("TF-IDF matrix created!")


# 4. Calculate cosine similarity

cosine_sim = cosine_similarity(tfidf_matrix)

print("Similarity matrix created!")


# 5. Create movie index


indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()

# 6. Recommendation function


def recommend_movies(title, number=5):

    # Check whether movie exists
    if title not in indices:
        print("\nMovie not found.")
        print("Please enter a movie from the dataset.")
        return

    # Find movie index
    idx = indices[title]

    # Get similarity scores
    similarity_scores = list(
        enumerate(cosine_sim[idx])
    )

    # Sort by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Remove the movie itself
    similarity_scores = similarity_scores[1:number + 1]

    print("\n--------------------------------")
    print("Recommended Movies")
    print("--------------------------------")
    print("Because you selected:", title)
    print()

    for i, score in similarity_scores:

        movie_name = movies.iloc[i]["title"]

        print(
            f"{movie_name} "
            f"(similarity: {score:.2f})"
        )



# 7. Ask the user for a movie


print("\nMovie Recommendation System")
print("--------------------------------")

movie = input("Enter a movie title: ").strip()

# Search for the movie without requiring an exact match
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