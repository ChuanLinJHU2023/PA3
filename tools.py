# tools.py provides some simple math functions for other programs.
def count_decimal_places(number):
    # Given a number, this function counts the digits behind the decimal point
    # For example, count_decimal_places(3.141592)==6
    # For example, count_decimal_places(3)==0
    number_str = str(number)
    if '.' not in number_str:
        return 0
    decimal_part = number_str.split('.')[1]
    return len (decimal_part)

def append_1_at_tail(number):
    # Given a number, this function append "1" to the tail of this number
    # For example, append_1_at_tail(4.11)==4.111
    # For example, append_1_at_tail(4)==4.1
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