# Fibonacci Sequence in Python
n, t1, t2 = input(), 0, 1
for i in range(0, int(n)):
    if i == 1:
        print(t1, '\t ')
        continue
    if i == 2:
        print(t2, '\t')
        continue
        i = i + 1
    next_num = t1 + t2
    t1 = t2
    t2 = next_num
    print(next_num)
