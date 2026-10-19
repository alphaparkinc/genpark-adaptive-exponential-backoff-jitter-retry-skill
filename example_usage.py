"""Example usage for Adaptive Exponential Backoff with Jitter Retry."""
from client import AdaptiveExponentialBackoffJitterRetry

if __name__ == "__main__":
    backoff = AdaptiveExponentialBackoffJitterRetry()
    for i in range(1, 4):
        res = backoff.compute_backoff(attempt=i)
        print(f"Attempt {i} backoff:", res)
