import time

def sourse_chain(number, sum_namber):
    chain_list = [number, sum_namber]
    new_sum = sum_namber
    while number != chain_list[-1] and new_sum != 1:
        print(f"number - {number}, new_sum - {new_sum}, sum_namber - {sum_namber}")
        new_sum = sourse_sum_divider(new_sum)
        chain_list.append(new_sum)
        time.sleep(1)
    print("Sourse_chain FINISH")
    return chain_list

def sourse_sum_divider(n):
    list_divider = []
    # print("Sourse_sum_divider START")
    for divider in range(1, n):
        if n % divider == 0:
            list_divider.append(divider)
    return sum(list_divider)

# sourse_chain(sourse_sum_divider(25), 25)

chain_number = []
number = 12495
while True:
    number += 1
    Flag = True
    sum_numbers = sourse_sum_divider(number)
    chain_list = sourse_chain(number, sum_numbers)
    print(chain_list)
