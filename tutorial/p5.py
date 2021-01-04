# x=[i**2 for i in range(1000000000000000)]
# for el in x:
#     print(el)
# ## above wont run due to memory error
# for i in range (1000000000000000):
#     print(i**2)
# # generators allow to store one value at a time and not look at entire sequence. think pointers
# class Gen:
#     def __init__ (self,n):
#         self.n=n
#         self.last=0
#     def __next__(self):
#         return self.next()
#     def next(self):
#         if self.last ==self.n:
#             raise StopIteration()
#         rv= self.last**2
#         self.last+=1
#         return rv
# g=Gen(10000000000000000000000000)
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break
# ## above is what a generator is like
def gen(n):
    for i in range(n):
        yield i**2 # as soon we hit this it return value to where we call this from and pauses function
g=gen(100000)
# for i in g:
#     print(i)
print(next(g))
import sys
x=[i**2 for i in range (100000)]
print(sys.getsizeof(g))## with generator
print(sys.getsizeof(x))## without generator
