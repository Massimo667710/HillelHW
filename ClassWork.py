# def test_func(a, b):
#    return a + b

test_func = lambda a, b: a + b

print(test_func(5, 3))


# def my_curr_func(a):
#     def my_func(b):
#         def my_inner(c):
#             return a + b + c
#         return my_inner
#     return my_func


print(my_curr_func(5)(2))
my_var_1 = my_curr_func(5)
print(my_var_1)
print(my_var_1(2))
