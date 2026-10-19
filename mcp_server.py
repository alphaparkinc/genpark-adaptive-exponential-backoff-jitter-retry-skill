"""MCP Server wrapper for Adaptive Exponential Backoff Jitter Retry."""
import json
import sys
from client import AdaptiveExponentialBackoffJitterRetry

backoff = AdaptiveExponentialBackoffJitterRetry()

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [
                {
                    "name": "calculate_retry_backoff",
                    "description": "Calculate full-jitter sleep duration and evaluate circuit breaker health",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "attempt": {"type": "integer"},
                            "error_type": {"type": "string", "default": "HTTP_429"}
                        },
                        "required": ["attempt"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        res = backoff.compute_backoff(args.get("attempt", 1), args.get("error_type", "HTTP_429"))
        return {
            "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
        }
    return {}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            try:
                r = json.loads(line)
                out = handle_request(r)
                print(json.dumps(out), flush=True)
            except Exception as e:
                print(json.dumps({"error": str(e)}), flush=True)
