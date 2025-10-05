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