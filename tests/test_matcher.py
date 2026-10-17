import os
import tempfile
import unittest
from pathlib import Path

class TemporaryDirectoryTest(unittest.TestCase):
    def setUp(self):
        self.cwd = Path.cwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)

    def tearDown(self):
        os.chdir(self.cwd)
        self.temp.cleanup()

import numpy as np
from matcher import generate_user_vectors, verify_identity

class MatcherTests(TemporaryDirectoryTest):
    def test_fresh_directory_and_known_vector(self):
        users = generate_user_vectors()
        self.assertTrue(Path("data/users.npy").is_file())
        score, accepted = verify_identity(users[0])
        self.assertAlmostEqual(score, 1)
        self.assertTrue(accepted)

    def test_orthogonal_vector_rejected(self):
        Path("data").mkdir()
        np.save("data/users.npy", [[1., 0.]])
        score, accepted = verify_identity(np.array([0., 1.]))
        self.assertEqual(score, 0)
        self.assertFalse(accepted)
