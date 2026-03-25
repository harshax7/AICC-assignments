import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
data = {
    'Movie A': [5, 5, 0, 0],
    'Movie B': [4, 5, 0, 0],
    'Movie C': [0, 0, 4, 5],
    'Movie D': [0, 0, 5, 4]
}

users = ['User1', 'User2', 'User3', 'User4']

df = pd.DataFrame(data, index=users)

print("User-Movie Matrix:\n")
print(df)

model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(df)


target_user = 'User1'
target_index = df.index.get_loc(target_user)

distances, indices = model.kneighbors(
    df.iloc[target_index].values.reshape(1, -1),
    n_neighbors=3
)

print("\nNearest Neighbors for", target_user)

for i in range(len(indices.flatten())):
    if i == 0:
        continue  # Skip itself
    print(f"{df.index[indices.flatten()[i]]} with distance {distances.flatten()[i]:.2f}")


neighbor_index = indices.flatten()[1]  # closest neighbor
neighbor_ratings = df.iloc[neighbor_index]

target_ratings = df.loc[target_user]

recommended_movies = []

for movie in df.columns:
    if target_ratings[movie] == 0 and neighbor_ratings[movie] > 0:
        recommended_movies.append(movie)

print("\nRecommended Movies for", target_user, ":\n", recommended_movies)