# genpark-adaptive-exponential-backoff-jitter-retry-skill

[![Verified by Smithery](https://smithery.ai/badge/@alphaparkinc/genpark-adaptive-exponential-backoff-jitter-retry-skill)](https://smithery.ai/servers/@alphaparkinc/genpark-adaptive-exponential-backoff-jitter-retry-skill)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![Website](https://img.shields.io/badge/Website-GenPark.ai-green)](https://www.genpark.ai)

> Full jitter exponential backoff retry scheduling and half-open circuit breaker state machine for LLM APIs

## Quick Installation & MCP Integration
Add to your Claude Desktop or Cursor configuration:
```json
{
  "mcpServers": {
    "genpark-adaptive-exponential-backoff-jitter-retry-skill": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

## Zero Dependencies
Implemented entirely in Python 3 standard library.
