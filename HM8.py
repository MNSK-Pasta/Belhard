from threading import Condition, Thread, BoundedSemaphore, Event, Barrier
from queue import Queue
from time import sleep, time
import multiprocessing
import os
import asyncio


# def doubler(number): #1
#
#     print(threading.currentThread().getName() + '\n')
#     print(number * 2)
#     print()
#
# if __name__ == '__main__':
#     for i in range(5):
#         my_thread = threading.Thread(target=doubler, args=(i,))
#         my_thread.start()
#
#
# data = [] #2
# lock = threading.RLock()
#
#
# def who_am_i(what):
#     print(f'Thread {threading.currentThread()} says: {what}')
#     lock.acquire()
#     global data
#     data.append(what)
#     time.sleep(1)
#     lock.release()
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         thread = threading.Thread(target=who_am_i, args=(f"I'm {i}",))
#         thread.start()
#     print(data)
# cv = Condition() #3
# q = Queue()
#
#
# def order_processor(name):
#     while True:
#         with cv:
#             while q.empty():
#                 cv.wait()
#             try:
#                 order = q.get_nowait()
#                 print(f'{name}: {order}')
#                 if order == 'stop':
#                     break
#             except:
#                 pass
#             sleep(0.1)
#
#
# Thread(target=order_processor, args=('thread 1',)).start()
# Thread(target=order_processor, args=('thread 2',)).start()
# Thread(target=order_processor, args=('thread 3',)).start()
#
# for i in range(10):
#     q.put(f'order{i}')
# for _ in range(3):
#     q.put('stop')
# with cv:
#     cv.notify_all()

# ticket_office = BoundedSemaphore(value=3)
#
#
# def ticket(number): #4
#     start_s = time()
#     with ticket_office:
#         sleep(1)
#         print(f'client {number}, service time: {time() - start_s}')
#
#
# buy = [Thread(target=ticket, args=(i,)) for i in range(5)]
# for b in buy:
#     b.start()
#
# event = Event() #5
#
#
# def worker(name):
#     event.wait()
#     print(f'Worker: {name}')
#
#
# event.clear()
# workers = [Thread(target=worker, args=(f'wrk {i}',)) for i in range(5)]
# for w in workers:
#     w.start()
# print('Main Thread')
# event.set()
# br = Barrier(3) #6
# store = []
#
#
# def f1(x):
#     print("calc part1")
#     store.append(x ** 2)
#     sleep(0.5)
#     br.wait()
#
#
# def f2(x):
#     print('calc part2')
#     store.append(x * 2)
#     sleep(1)
#     br.wait()
#
#
# Thread(target=f1, args=(3,)).start()
# Thread(target=f2, args=(7,)).start()
#
# br.wait()
#
# print("Result:", sum(store))
# def do_this(what): #7
#     who_am_i(what)
#
#
# def who_am_i(what):
#     print(f'Process {os.getpid()} says: {what}')
#
#
# if __name__ == '__main__':
#     who_am_i('Im the main programm')
#     for n in range(4):
#         process = multiprocessing.Process(
#             target=do_this,
#             args=(f'I, function {n}',)
#         )
#         process.start()
async def counter():
    count = 0
    while True:
        print(count)
        count += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} sec')
        count += 1
        await asyncio.sleep(1)


async def main():
    task_1 = asyncio.create_task(print_time())
    task_2 = asyncio.create_task(counter())
    await asyncio.gather(task_1, task_2)


if __name__ == '__main__':
    asyncio.run(main())
