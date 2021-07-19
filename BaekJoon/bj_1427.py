num = input()

num_list = list(map(int, str(num)))

num_list.sort(reverse=True)

for i in num_list:
    print(i, end='')