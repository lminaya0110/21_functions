
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

def reverse_this(my_string):
    letters = [i for i in my_string]
    for i in reversed(letters):
        print(i)
    

print(reverse_this("The cow jumped over the moon"))
#_______________________________________________________________________



