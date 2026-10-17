# Biometric Vector Matcher

![Conceptual illustration of Biometric Vector Matcher; not program output](assets/conceptual-cover.webp)

*Conceptual illustration, not program output.*

An educational cosine-similarity demonstration using synthetic numerical vectors.

## Problem and objective

Show how a sample vector can be compared with a stored matrix and checked against a threshold.

## Scope and limitations

The vectors are random, not extracted from faces, fingerprints, or voices. A threshold result does not verify a person's identity. The default threshold of 0.9 is illustrative and uncalibrated. The script replaces the generated dataset on each run; there is no enrollment workflow, user identification output, or production authentication.

## How it works

`generate_user_vectors` creates 10 vectors with 128 dimensions and writes `data/users.npy`, creating the directory if needed. `verify_identity` loads the matrix, computes cosine similarity against each row, and returns the maximum score plus a threshold decision. `main.py` compares an independent random sample.

## Technologies

Python, NumPy, scikit-learn (cosine similarity).

## Installation and configuration

Use Python 3.11. From the repository root:

```powershell
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements-lock.txt
```

`requirements-lock.txt` records the reviewed environment; `requirements.txt` lists direct dependencies.

On macOS/Linux, replace `.venv/Scripts/python` with `.venv/bin/python`.

## Run and example output

```powershell
.venv/Scripts/python main.py
```

The two output lines report `Maximum cosine similarity: <score>` and a threshold decision. Random scores vary. For a deterministic positive control:

```powershell
.venv/Scripts/python -c "from matcher import generate_user_vectors, verify_identity; users=generate_user_vectors(); score, accepted=verify_identity(users[0]); print(f'{score:.2f}, {bool(accepted)}')"
```

```text
1.00, True
```

## Data source

Synthetic vectors generated locally. `data/users.npy` is a local NumPy file, not a biometric database.

## Verification

```powershell
.venv/Scripts/python -m unittest discover -s tests -v
```

Verified with Python 3.11.9: two unit tests and the demo passed. Tests check creation of a fresh data directory, a known-vector match, and orthogonal-vector rejection.

## Possible next steps

Future work could separate enrollment from matching and study threshold behavior with labeled synthetic pairs.
