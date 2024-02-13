"""
awaitables: coroutines(async def), tasks, Futures
coroutine function, coroutine object
run(), Runner(), sleep(), [create_task(), add_done_callback()], close(), gather() (schedule calls concurrently)
"""

import asyncio

# coroutine function
async def get_task(x):
    await asyncio.sleep(2)
    return f'Task {x}'

async def user_api(user):
    print(user)
    bg_tasks = set()
    for i in range(3):
        task = asyncio.create_task(get_task(i))
        bg_tasks.add(task)
        print(await task, user)
        task.add_done_callback(bg_tasks.discard)
    return f"{user} tasks are done"

async def main():
    concurrent_tasks = await asyncio.gather(
        user_api('user 1'),
        user_api('user 2'),
        user_api('user 3'),
        user_api('user 4')
    )
    print(f'Now printing concurrent tasks')
    print(concurrent_tasks)

if __name__ == '__main__':
    # asyncio.run(user_api("first user"))
    asyncio.run(main())
    # asyncio.run(user_api("second user"))



