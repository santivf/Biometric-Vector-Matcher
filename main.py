from matcher import generate_user_vectors, verify_identity
import numpy as np

if __name__ == "__main__":
    generate_user_vectors()
    sample = np.random.rand(128)
    similarity, verified = verify_identity(sample)
    print(f"Maximum cosine similarity: {similarity:.2f}")
    print("Threshold met" if verified else "Threshold not met")
