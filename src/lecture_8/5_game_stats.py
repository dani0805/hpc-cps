import numpy as np

# Seed for reproducibility
np.random.seed(0)

# Array of scores for 5 players across 8 games (randomly generated)
scores = np.random.randint(0, 100, (5, 8))
print("Game scores:\n", scores)

# Indices of top 3 scores for each player
top_3_games = np.argpartition(scores, -3, axis=1)[:, -3:]
# equivalent to sorting and slicing like this, but faster:
# top_3_games = np.argsort(scores, axis=1)[:, -3:]
# does not guarantee order of elements within each row
print("Indices of top 3 scores for each student:\n", top_3_games)

# Now let's use np.take_along_axis to get the actual top 3 scores for each student
top_3_scores = np.take_along_axis(scores, top_3_games, axis=1)
# can also use fancy indexing like this, but it's slower:
# top_3_scores = scores[np.arange(scores.shape[0])[:, None], top_3_games]

print("Top 3 scores for each student:\n", top_3_scores)
