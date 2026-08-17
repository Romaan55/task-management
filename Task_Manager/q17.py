import asyncio                  # Async ka system
import aiohttp                  # URLs fetch karne ke liye


async def fetch(url, session):  # Ek URL fetch karo
    try:
        async with session.get(url) as response:  # Request bhejo
            return await response.text()          # Result return karo
    except Exception as e:                       # Error pakro
        return f"Error: {e}"                      # Error return karo


async def fetchAll(urls, limit):                 # Sab URLs fetch karo
    semaphore = asyncio.Semaphore(limit)         # Requests limit karo

    async with aiohttp.ClientSession() as session:  # Session banao

        async def limited_fetch(url):             # Limited request
            async with semaphore:                 # Limit follow karo
                return await fetch(url, session)  # URL fetch karo

        tasks = [limited_fetch(url) for url in urls]  # Tasks banao
        results = await asyncio.gather(*tasks)         # Sab results lo

    return results                                # Results return karo


# Example URLs
urls = [                                      # URLs ki list
    "https://example.com",                    # URL 1
    "https://example.org",                    # URL 2
    "https://example.net"                     # URL 3
]

results = asyncio.run(fetchAll(urls, 2))     # Max 2 requests ek waqt

print(results)                                # Results print karo