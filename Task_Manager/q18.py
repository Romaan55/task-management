#chatgpt
import asyncio
print("1")
async def main():
    print("4")
    await asyncio.sleep(0)
    print("5")

async def run():
    asyncio.get_running_loop().call_soon(lambda: print("2"))
    asyncio.create_task(main())
    print("6")

asyncio.run(run())