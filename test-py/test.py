# my_str = 'aIbohPhoBiA'.lower()
# rev_str = ""

# for s in my_str:
#     rev_str=s + rev_str
# print(my_str,id(my_str))
# print(rev_str,id(rev_str))

# if rev_str == my_str:
    
#     print("The string is a palindrome.")
# else: 
#     print("The string is not a palindrome.")


# text: str = "Ashish"
# def reverse_string(text: str)-> str:
#     n = len(text)-1
#     result = ''
#     while n>=0 :
#         result= result + text[n]
#         n-=1
#     return result
# print(reverse_string(text))
# s = ''

# for txt in text:
#     s= txt+s

# print(s)

# def delete_str(data:str):
#     vowel ="aeiou"
#     return [char for char in data if char in vowel]

# print(delete_str("Python and Data Science A"))

# def return_string(data):
#   vowels = 'aeiouAEIOU'
#   result = ''.join([char for char in data if not char.isalpha() or char in vowels])
#   return result

# print(return_string(data ="Python and Data Science A"))


# def is_prime(number):

#   for i in range(2,int(number/2)+1):
#     # print(int(number/2),number/2)
#     if(number % i ==0):
#       return False
#   return True

# result = map(is_prime, range(10))

# print(list(result))
# def add(number):
#   total = 0
#   for i in range(2,number + 1):
#     # print(i,is_prime(i))
#     if is_prime(i):
#       total = total + i
#   return total
# print(add(10))
# def gen():
#   for i in range(18):
#     yield i

# g = gen()

# print(next(g),"start")
# print(next(g),"start")

# print(next(g),"start")

# for _ in g:
#   print(_)
# data = (x**2 for x in range(10))
# print(data)
# print(next(data))

# l=[x*x for x in range(10000000000000000)]
# print(l[0])
# g=(x*x for x in range(10000000000000000))
# print(next(g))

# import random
# import time
# names = ['Sunny','Bunny','Chinny','Vinny']
# subjects = ['Python','Java','Blockchain']

# def people_list(num_people):
#   results = []
#   for i in range(num_people):
#     person = {
#       'id':i,
#       'name': random.choice(names),
#       'subject':random.choice(subjects)
#     }
#   results.append(person)
#   return results
# t1 = time.time()
# people = people_list(10000000)
# t2 = time.time()
# print(f'Took {t2-t1}')

# def people_generator(num_people):
#   for i in range(num_people):
#     person = {
#       'id':i,
#       'name': random.choice(names),
#       'major':random.choice(subjects)
#       }
#   yield person

# t1 = time.time()
# people = people_generator(10000000)
# t2 = time.time()

# print(f'Took {t2-t1}')

# Define decorators
# def bold_decorator(func):
#     def wrapper():
#         return f"<b>{func()}</b>"
#     return wrapper

# def italic_decorator(func):
#     def wrapper():
#         return f"<i>{func()}</i>"
#     return wrapper

# # Apply multiple decorators
# @bold_decorator
# @italic_decorator
# def get_text():
#     return "Hello, World!"

# # Call the function
# print(get_text())


# def love(fun):
#   def inner():
#     return fun.__name__
#   return inner
# @love
# def fun_test():
#   print("testing")

# print(fun_test())  

# def dob(fun):
#   def inner(n):
#     return fun(n**2)
#   return inner

# def calc(num):
#   print(num)

# @dob
# def cal(num):
#   print(num)

# calc(11)
# cal(11)

# vowels=['a','e','i','o','u']

# lists = "ashisg binodra"

# l0 = [char for char in vowels if char in lists]
# print(l0)

# def fib():
#   a,b = 0,1
#   while True:
#     yield a
#     a,b = b,a+b
# data = fib()
# for _ in range(11):
#   print(next(data))

# Recursive function for Fibonacci series
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# # Input: Number of terms
# num_terms = int(input("Enter the number of terms: "))

# # Generate and print the Fibonacci series
# series = [fibonacci_recursive(i) for i in range(num_terms)]
# print(f"Fibonacci series: {series}")

# Flat list with alternating keys and values
# flat_list = ["name", "Alice", "age", 25, "city", "New York"]

# n=len(flat_list)
# # Convert to dictionary
# dict_obj = {k:v for k,v in enumerate(flat_list)}
# print(dict_obj)

## Given a string `s = "abcvderndsgh"` and an integer `k = 2`, divide the string into segments of length `k`, and **reverse every alternate 2 segments**, starting with skipping the first 2 segments.
s = "abcdefghij"
k = 2

words = []

for i in range(0, len(s), k):
    # Reverse the chunk if it's at an even index, otherwise keep it as is
    chunk = s[i:i+k]
    words.append(''.join(reversed(chunk)) if (i // k) % 2 == 0 else chunk)

print(words)