#!/bin/bash/python3

import random

random_num = random.randint(1,10)
print(random_num)
user_choice = 0
user_count = 0
while random_num != user_choice:
    user_choice = input('请输入1-10中一个数字>>>').strip()
    user_choice = int(user_choice)
    if user_choice < random_num:
        print('小了')
    elif user_choice > random_num:
        print('大了')
    user_count += 1
    if user_count > 5:
        print('timeout')
        break
else:
    print('猜对了')

