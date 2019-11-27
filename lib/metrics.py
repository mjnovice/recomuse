# https://github.com/benhamner/Metrics/blob/master/Python/ml_metrics/average_precision.py
import numpy as np


def average_precision(predicted_songs, actual_songs, k=10):
    if len(predicted_songs) > k:
        predicted_songs = predicted_songs[:k]

    if not actual_songs:
        return 0.0

    score = 0.0
    num_hits = 0.0

    for i, p in enumerate(predicted_songs):
        if p in actual_songs and p not in predicted_songs[:i]:
            num_hits += 1.0
            score += num_hits / (i + 1.0)

    return score / min(len(actual_songs), k)


def mean_average_precision(predicted_songs, actual_songs, k=10):
    return np.mean([average_precision(a, p, k) for a, p in zip(actual_songs, predicted_songs)])
