import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def fib_seq(stop):
    fib_list =[]
    for n in range(stop):
        cached = r.get(n)
        if cached:
            fib_list.append(int(cached))
            if n % 1000 == 0:
                print(f"F({n}) - from cache")
        else:
            next_num = n if n < 2 else fib_list[-1] + fib_list[-2]
            fib_list.append(next_num)
            r.set(n, next_num)
            if n % 1000 == 0:
                print(f"F({n}) - added to cache")
    return fib_list


my_seq1 = fib_seq(25)
print(my_seq1)

my_seq2 = fib_seq(50)
print(my_seq2)

my_seq3 = fib_seq(100)
print(my_seq3)

my_seq4 = fib_seq(1000)
print(my_seq4)

# while len(fib_list) < stop:
#     n = len(fib_list)
#     seq_cached = r.get(n)
#     if seq_cached:
#         fib_list.append(int(seq_cached))
#     else:
#         next_num = fib_list[-1] + fib_list[-2]
#         fib_list.append(next_num)
#         r.set(n, next_num)