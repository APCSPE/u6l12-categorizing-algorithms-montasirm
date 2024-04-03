import math

def function_a(some_list):
   count = 0
   for i in range(len(some_list)):
       print("hello")
       count = count + 1
   print(count)


def function_b(some_list):
   count = 0
   for i in range(len(some_list)):
       print("hello")
       count = count + 1
   for i in range(len(some_list)):
       print("hello")
       count = count + 1
   print(count)


def function_c(some_list):
   count = 0
   for i in range(len(some_list)):
       for j in range(len(some_list)):
           print("hello")
           count = count + 1
   print(count)


def function_d(some_list):
   count = 0
   for i in range(len(some_list)):
       for j in range(len(some_list)):
           for k in range(len(some_list)):
               print("hello")
               count = count + 1
   print(count)


def function_e(some_list):
   count = 0
   times = math.log2(len(some_list))  # log base 2 of list length
   times = int(times)  # convert to int
   for i in range(times):
       print("hello")
       count = count + 1
   print(count)


def function_f(some_list):
   count = 0
   times = 8
   for i in range(times):
       print("hello")
       count = count + 1
   print(count)


def function_g(some_list):
   count = 0
   times = 2 ** len(some_list)  # 2^(list length)
   for i in range(times):
       print("hello")
       count = count + 1
   print(count)


def function_h(some_list):
   count = 0
   times = math.factorial(len(some_list))
   for i in range(times):
       print("hello")
       count = count + 1
   print(count)


# TEST CODE
my_list_5 = [1, 2, 3, 4, 5]
my_list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_25 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

#function_a(my_list_5)
#function_a(my_list_10)
#function_a(my_list_25)

#function_b(my_list_5)
#function_b(my_list_10)
#function_b(my_list_25)

#function_c(my_list_5)
#function_c(my_list_10)
#function_c(my_list_25)

#function_d(my_list_5)
#function_d(my_list_10)
#function_d(my_list_25)

#function_e(my_list_5)
#function_e(my_list_10)
#function_e(my_list_25)

#function_f(my_list_5)
#function_f(my_list_10)
#function_f(my_list_25)

#function_g(my_list_5)
#function_g(my_list_10)
#function_g(my_list_25)

#function_h(my_list_5)
#function_h(my_list_10)
#function_h(my_list_25)

