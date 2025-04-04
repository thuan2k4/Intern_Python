import asyncio
from time import time, sleep

def Work_For_A():
    print("Working in A")
    sleep(3)

def Work_For_B():
    print("Working in B")
    sleep(2)

# start = time()

# Work_For_A()
# Work_For_B()

# print(f"Time taken: {time() - start}")

async def Work_Async_For_A():
    print("Working in A")
    await asyncio.sleep(3)

async def Work_Async_For_B():
    print("Working in B")
    await asyncio.sleep(2)  

async def main():
    start = time()
    await asyncio.gather(Work_Async_For_A(), Work_Async_For_B())
    print(f"Time taken: {time() - start}")

if __name__ == "__main__":
    asyncio.run(main())