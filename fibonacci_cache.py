import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def fib_seq(stop):
    fib_list =[]
    cached_count = 0
    added_to_cache = 0

    for n in range(stop):
        cached = r.get(n)
        if cached:
            fib_list.append(int(cached))
            cached_count += 1
        else:
            next_num = n if n < 2 else fib_list[-1] + fib_list[-2]
            fib_list.append(next_num)
            r.set(n, next_num)
            added_to_cache += 1

    print(f"Total numbers requested: {stop}")
    print(f"Taken from cache: {cached_count}")
    print(f"Calculated for sequence: {added_to_cache}")

    return fib_list


my_seq1 = fib_seq(25)
my_seq2 = fib_seq(50)
my_seq3 = fib_seq(100)
my_seq4 = fib_seq(2000)

# while len(fib_list) < stop:
#     n = len(fib_list)
#     seq_cached = r.get(n)
#     if seq_cached:
#         fib_list.append(int(seq_cached))
#     else:
#         next_num = fib_list[-1] + fib_list[-2]
#         fib_list.append(next_num)
#         r.set(n, next_num)