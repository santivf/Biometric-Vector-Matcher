from matcher import generate_user_vectors, verify_identity
import numpy as np

generate_user_vectors() 

sample = np.random.rand(128)
similarity, verified = verify_identity(sample)

print(f"Maximum Identify: {similarity:.2f}")
print("Verified Identify" if verified else "No Verified")


