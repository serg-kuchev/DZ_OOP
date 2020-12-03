file_list = ['1.txt', '2.txt', '3.txt']

from collections import OrderedDict


for name in file_list:
    a = {}
    with open(name, encoding='utf-8') as f:
        line_count = 0
        for line in f:
            line_count += 1
        # print(line_count)


s_dict = {'1.txt': 8, '2.txt': 1, '3.txt': 9}
sorted_dict = OrderedDict(sorted(s_dict.items(), key=lambda x: x[1]))
# print(*sorted_dict)


with open('all123.txt', 'w', encoding='utf-8') as f3:
    for it in sorted_dict:
        print(it)
        with open(it, encoding='utf-8') as f:
            f3.write(f'{it}\n')
            f3.write((f'{sorted_dict[it]}\n'))
            f3.writelines(f.readlines())
