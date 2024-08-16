# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #do something before
#         function()
#         function()
#         #do something after
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("Hello")

# @delay_decorator
# def say_bye():
#     print("Bye")

# def say_greeting():
#     print("How are you?")


# say_greeting()
# say_hello() #prints after two seconds as delay decorator is called before

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        difference = end_time-start_time
        print(f"{function.__name__} run speed: {difference}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()
