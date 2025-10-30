import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def generate_user_vectors(n_users=10, vector_size=128):
    data = np.random.rand(n_users, vector_size)
    np.save("data/users.npy", data)
    return data

def verify_identity(sample_vector, threshold=0.9):
    users = np.load("data/users.npy")
    similarities = cosine_similarity([sample_vector], users)[0]
    max_sim = np.max(similarities)
    return max_sim, max_sim >= threshold


