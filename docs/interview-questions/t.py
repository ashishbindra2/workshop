# class A:
#     def show(self):
#         print("A.show")

# class B(A):
#     def show(self):
#         print("B.show")

# class C(A):
#     def show(self):
#         print("C.show")

# class D(C,B):
#     pass

# obj = D()
# obj.show()   # Output?


# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b, a+b
# f = fib()
# for i in range(1,10):
#     print(next(f))

# l = [6,5,4,3,32,1]

# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i]>l[j]:
#              l[i], l[j] = l[j],l[i]

# print(l)

# s = "ashihsaa"

# # print("Is a Palindrome") if(s == s[::-1]) else print("No")
# flag = True
# for  i,w in enumerate(s,start=1):
#     if w != s[len(s) - i]:
#         print("No")
#         flag = False
#         break

# if flag:
#     print("Is a Palindrome")

# d = {4:"asd",3:"sd",2:"sds",1:"sd"}
# data = {'apple': 3, 'banana': 1, 'cherry': 2}

# d2 = {}
# for i in sorted(d):
#     d2[i] = d[i]

# print(d2)

# sorted_dict = {k: d[k] for k in sorted(d)}
# print(sorted_dict)


# list1 = [1,2,3,4,5,6,7,8,9]
# k = 10

# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] + list1[j] == k:
#             print(list1[i],list1[j])


# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)


# print(fib(10))

# s = "The Sky is Blue"
# o = "Blue is The Sky"

# v = ""
# for i in s.split():
#     v = i + "_" + v
# print(v[: len(v) - 1])

# l = s.split()
# l = l[::-1]
# l = " ".join(l)
# print(l)
# v = "/*apples are & found% only @red & green"

# s = ''

# for i in v:
#     if((i>='A' and i <='Z') | (i>='a' and i <= 'z') | (i==' ')):
#         s = s + i
# print(s)

# s = "asdafdfbvnonwvjsdnvosdnvdsnoidn"

# ch = {}
# for i in s:
#     ch[i] = ch.get(i,0) + 1

# print(ch)

# print(max(ch,key=ch.get))

# l = [111, 22, 44, 5, 6, 23, 45, 56, 67]

# maxi: int = l[0]
# mini: int = l[0]
# for i in l:
#     if i > maxi:
#         maxi = i
#     if mini > i:
#         mini = i

# print(maxi, mini)
# l = [1,2,3,4,5,6]
# sum = 0

# for i in l:
#     if i==3:
#         raise Exception("Exception: 0 is found")
#     else:
#         sum+=1

# s = "aabbccaaaafffeiii"
# p = ""
# new = ""
# count = 1
# for i in s:
#     if i == p:
#         count += 1
#     else:
#         if p:
#             new += p + str(count)
#         p = i
#         count = 1


# print(new)
# for n in range(1, 20):
#     if n % 15 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)

# s = 'I_Am_Coder'

# # print(s.swapcase().replace("_","."))
# l = []
# for i in s.split('_'):
#     l.append(i.capitalize().swapcase()) # l.append(i[0].lower() + i[1:].upper())
# print(".".join(l))

# import typing

# new_dict = {}
accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
# # for i in accounts:
# #     name = i[0]
# #     new_dict[name] = new_dict.get(name,set()) | set(i[1:])


# # for k,v in new_dict.items():

# new = []
# for i in accounts:
#     name = i[0]
#     email =  sorted(set(i[1:]))
#     new.append([name] + email)
# print(new)
accounts = [
    ["David", "David0@m.co", "David1@m.co"],
    ["David", "David3@m.co", "David4@m.co"],
    ["David", "David4@m.co", "David5@m.co"],
    ["David", "David2@m.co", "David3@m.co"],
    ["David", "David1@m.co", "David2@m.co"],
]

# accounts = [
#     ["David", "David4@m.co", "David2@m.co", "David4@m.co"],
#     ["John", "John7@m.co", "John5@m.co", "John3@m.co"],
#     ["Fern", "Fern6@m.co", "Fern4@m.co", "Fern5@m.co"],
#     ["Celine", "Celine0@m.co", "Celine7@m.co", "Celine7@m.co"],
#     ["Gabe", "Gabe8@m.co", "Gabe8@m.co", "Gabe1@m.co"],
#     ["Ethan", "Ethan1@m.co", "Ethan6@m.co", "Ethan6@m.co"],
#     ["Celine", "Celine4@m.co", "Celine8@m.co", "Celine6@m.co"],
#     ["Celine", "Celine0@m.co", "Celine0@m.co", "Celine4@m.co"],
# ]

accounts =[["Hanzo","Hanzo2@m.co","Hanzo3@m.co"],["Hanzo","Hanzo4@m.co","Hanzo5@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co"],["Hanzo","Hanzo3@m.co","Hanzo4@m.co"],["Hanzo","Hanzo7@m.co","Hanzo8@m.co"],["Hanzo","Hanzo1@m.co","Hanzo2@m.co"],["Hanzo","Hanzo6@m.co","Hanzo7@m.co"],["Hanzo","Hanzo5@m.co","Hanzo6@m.co"]]

accounts = [["Lily","Lily4@m.co","Lily5@m.co"],["Lily","Lily8@m.co","Lily9@m.co"],["Lily","Lily15@m.co","Lily16@m.co"],["Lily","Lily19@m.co","Lily20@m.co"],["Lily","Lily6@m.co","Lily7@m.co"],["Lily","Lily10@m.co","Lily11@m.co"],["Lily","Lily5@m.co","Lily6@m.co"],["Lily","Lily13@m.co","Lily14@m.co"],["Lily","Lily9@m.co","Lily10@m.co"],["Lily","Lily1@m.co","Lily2@m.co"],["Lily","Lily3@m.co","Lily4@m.co"],["Lily","Lily2@m.co","Lily3@m.co"],["Lily","Lily11@m.co","Lily12@m.co"],["Lily","Lily7@m.co","Lily8@m.co"],["Lily","Lily12@m.co","Lily13@m.co"],["Lily","Lily18@m.co","Lily19@m.co"],["Lily","Lily17@m.co","Lily18@m.co"],["Lily","Lily16@m.co","Lily17@m.co"],["Lily","Lily14@m.co","Lily15@m.co"],["Lily","Lily0@m.co","Lily1@m.co"]]

names = [acc[0] for acc in accounts]
new = [set(acc[1:]) for acc in accounts]

merged = True
while merged:
    merged = False
    i = 0

    while i < len(new):
        j = i + 1
        while j < len(new):
            if new[i] & new[j]:
                new[i] |= new[j]
                del new[j]
                del names[j]
                merged = True

            else:
                j += 1
        i += 1

for i, name in enumerate(names):
    new[i] = [name] + sorted(new[i])

print(new)
