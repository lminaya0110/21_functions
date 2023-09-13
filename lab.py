print(f"\t\tBasic Functions : \n")

# Write a Python function to sum all the numbers in a list
def my_sum(*args):
    total = 0
    for i in args:
        total += i
    return total
print(f'Sum all numbers : {my_sum(3, 27, 1993)}\n') 


# Write a Python function to find the maximum of three numbers

def find_max(num1, num2, num3):
    nums = []
    nums.extend((num1, num2, num3))
    result = max(nums)
    return result
   
do_this = find_max(8, 35, 15)
print(f'Find Max of 3 Nums : {do_this}\n')
#_______________________________________________________________________

# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def mult_nums(*args):
    multiplied_numbers = 1
    for i in args:
        multiplied_numbers *= i
    return multiplied_numbers

    
first_try = mult_nums(3, 6, 9)
print(f'Multiply all nums in list : {first_try}\n')
#_______________________________________________________________________

# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_this(my_str):

    reversed = ''
    index = len(my_str)
    while index > 0:
        reversed += my_str[ index - 1 ]
        index = index - 1
    return reversed

print("Reversed String : " + reverse_this("The cow jumped over the moon") + "\n")
#_______________________________________________________________________

# Write a Python function to check whether a number falls within a given range

def check_range(required, num_1, num_2):
    
    lst = [i for i in range(num_1, num_2)]
    if required in lst:
        print(f'{required} IS in your list : {lst}')
    else:
        print(f'{required} is NOT in your list : {lst}\n')
            
check_range(1, 2, 15)
 #_______________________________________________________________________

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def distinct_lst(*args):
    lst = [int(i) for i in args]
    new_set = set(lst)
    set_to_lst = list(new_set)
    return set_to_lst

print(f'Distinct List : {distinct_lst(1, 2, 2, 3, 4, 4, 5)} \n')
 #_______________________________________________________________________

# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def find_even_nums(*args):
    even_lst = []
    for i in args:
        if i % 2 == 0:
            even_lst.append(i)
    return even_lst
    
print(f"Find Even Nums : {find_even_nums(1, 2, 3, 4, 5, 6)} \n")
 #_______________________________________________________________________


print(f"\t\tLambda Functions : \n")

#************* LAMBDA FUNCTIONS *************

# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
# Sample Output:
# 25
# 48

add_15 = lambda n: n + 15
multiply = lambda x, y: x * y

print(f'Add 15 : {add_15(10)}\n')
print(f'Multiply : {multiply(6, 8)}\n')
 #_______________________________________________________________________

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))
