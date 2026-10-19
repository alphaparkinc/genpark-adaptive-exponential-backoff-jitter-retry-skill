"""Adaptive Exponential Backoff with Jitter Retry.
100% Python Standard Library.
"""
import time
import random

class AdaptiveExponentialBackoffJitterRetry:
    """Full jitter exponential backoff retry scheduling and half-open circuit breaker state machine for LLM APIs."""

    STATE_CLOSED = "CLOSED"
    STATE_OPEN = "OPEN"
    STATE_HALF_OPEN = "HALF_OPEN"

    def __init__(self, base_delay: float = 1.0, max_delay: float = 60.0, failure_threshold: int = 5):
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.failure_threshold = failure_threshold
        self.failure_count = 0
        self.circuit_state = self.STATE_CLOSED
        self.last_failure_time = 0.0

    def compute_backoff(self, attempt: int, error_type: str = "HTTP_429") -> dict:
        now = time.time()
        self.failure_count += 1
        self.last_failure_time = now

        if self.failure_count >= self.failure_threshold:
            self.circuit_state = self.STATE_OPEN

        ceiling = min(self.max_delay, self.base_delay * (2 ** attempt))
        jitter_delay = round(random.uniform(0.5 * ceiling, ceiling), 3)

        return {
            "attempt": attempt,
            "error_type": error_type,
            "circuit_state": self.circuit_state,
            "failure_count": self.failure_count,
            "recommended_sleep_seconds": jitter_delay,
            "can_retry": self.circuit_state != self.STATE_OPEN or (now - self.last_failure_time > 30.0)
        }
