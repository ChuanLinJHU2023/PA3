def count_decimal_places(number) :
    number_str = str(number)
    if '.' not in number_str:
        return 0
    decimal_part = number_str.split('.')[1]
    return len (decimal_part)

# def append_1_at_tail(number):
#     x = count_decimal_places(number)
#     return number+0.1*10**(-x)
def append_1_at_tail(number):
    x = count_decimal_places(number)
    if x==0:
        res=str(number)+".1"
    else:
        res=str(number)+"1"
    return eval(res)
# print(count_decimal_places(3.141592))
# print(append_1_at_tail(3.141592))
# print(append_1_at_tail(4.1))
# print(append_1_at_tail(4))