my_str = 'aIbohPhoBiA'.lower()
rev_str = ""

for s in my_str:
    rev_str=s + rev_str
print(my_str,id(my_str))
print(rev_str,id(rev_str))

if rev_str == my_str:
    
    print("The string is a palindrome.")
else: 
    print("The string is not a palindrome.")
