#!/usr/bin/python3

inp_text = input('input a number(exit to bye):')

input_sum = 0
input_count = 0

while inp_text != 'exit':
    input_count += 1
    input_sum += float(inp_text)
    inp_text = input('input a number(exit to bye):')

if input_count == 0:
    print("last result input_sum is %d"%input_sum)
else:
    print("avg is %f"%(input_sum/input_count))
