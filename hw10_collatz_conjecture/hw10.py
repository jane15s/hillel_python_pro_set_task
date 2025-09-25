from multiprocessing import Process, Queue, cpu_count

def collatz_check(num):
    seen = set()
    while num != 1:
        if num in seen:
            return False
        seen.add(num)

        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    return True

def worker(start, end, queue):
    for num in range(start, end):
        if not collatz_check(num):
            queue.put(f"Hypothesis failed for {num}")
            return
    queue.put(f"Checked numbers from {start} to {end-1}")


if __name__ == "__main__":
    to_in_range = 100
    num_processes = cpu_count()
    # print(f"num_processes: {num_processes}")
    chunk_size = to_in_range // num_processes
    # print(f"chunk_size: {chunk_size}")

    queue = Queue()
    processes = []

    for i in range(num_processes):
        start = i * chunk_size + 1
        end = (i + 1) * chunk_size + 1 if i < num_processes - 1 else to_in_range + 1
        # print(f"start: {start} end: {end}")
        p = Process(target=worker, args=(start, end, queue))
        # print(p.name)
        processes.append(p)
        p.start()

    finished_processes = 0
    while finished_processes < num_processes:
        message = queue.get()
        print(message)
        finished_processes = finished_processes + 1

    for process in processes:
        process.join()

# def collatz(num):
#     my_list = [num]
#     while num != 1:
#         if num % 2 == 0:
#             num //= 2
#         else:
#             num = num * 3 + 1
#         my_list.append(num)
#     return my_list


# def collatz(num):
#     my_list = [num, ]
#     if num % 2 == 0:
#         new_num = num // 2
#     else:
#         new_num = num * 3 + 1
#     while new_num != 1:
#         num = new_num
#         if new_num % 2 == 0:
#             new_num = new_num // 2
#         else:
#             new_num = new_num * 3 + 1
#         my_list.append(num)
#     my_list.append(1)
#     return my_list