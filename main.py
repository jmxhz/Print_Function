# Print_Function
"""
version:1.0
author:Zhou Yulin
description:the use of print
"""


def print_01():
    print("输出1到4，用‘，’隔开：")
    print(1, 2, 3, 4,end='\n')


def print_02(n):
    print()
    print("输出0到n个数，用‘，’隔开：")
    for i_num in range(n):
        print(i_num,end=',')


def print_03(num1, num2):
    print()
    print()
    print("减法输出，使用format:")
    print('{} - {} = {}'.format(num1, num2, num1 - num2),end='\n')


def print_04(num1, num2):
    print()
    print("加法输出，使用f:")
    print(f'{num1} + {num2} = {num1 + num2}',end='\n')


num = 10
num1 = 2**2
num2 = 2**num
num3 = num1 - num2
print_01()
print_02(num)
print_03(num1, num2)
print_04(num1, num2)

