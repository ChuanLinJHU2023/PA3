def count_decimal_places(number) :
    number_str = str(number)
    if '.' not in number_str:
        return 0
    decimal_part = number_str.split('.')[1]
    # 返回小数点后面的位数
    return len (decimal_part)

def append_1_at_tail(number):
    x = count_decimal_places(number)
    return number+0.1*10**(-x)

# print(count_decimal_places(3.141592))
# print(append_1_at_tail(3.141592))