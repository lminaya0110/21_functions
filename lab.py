
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

print(distinct_lst(1, 2, 2, 3, 4, 4, 5))
 #_______________________________________________________________________

