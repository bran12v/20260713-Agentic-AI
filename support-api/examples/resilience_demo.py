import asyncio
import logging
import os
import time

import httpx

from support_api.http_resilience import request_with_retry
from support_api.logging import configure_logging

async def main() -> None:
    """This is a demonstration of the retry functionality."""
    configure_logging()
    logging.getLogger("httpx").setLevel(logging.WARNING)
    base_url = os.environ.get("API_BASE_URL", "http://localhost:5000")
    start = time.perf_counter()

    async with httpx.AsyncClient(base_url=base_url, timeout=10.0) as client:
        for n in range(50):
            response = await request_with_retry(
                client, "GET", "/tickets", max_retries=5
            )
            print(f"request {n}: status={response.status_code}")

    elapsed = time.perf_counter() - start
    print(f"\n50 requests completed in {elapsed:.2f}s; retries logged above.")

if __name__ == "__main__":
    asyncio.run(main())