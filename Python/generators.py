#Generator are a way of creating iterators. Generators are written just like a normal function but we use yield() instead of return() for returning a result.
#Unlike regular functions which on encountering a return statement terminates entirely, generators use a yield statement in which the state of the function is saved from the last call and can be picked up or resumed the next time we call a generator function. Another great advantage of the generator over a list is that it takes much less memory. 


# def generator(): 
#     t = 1
#     print ('First result is ',t) 
#     yield t 
 
#     t += 1
#     print ('Second result is ',t) 
#     yield t 
 
#     t += 1
#     print('Third result is ',t) 
#     yield t 
 
# call = generator() 
# next(call) 
# next(call) 
# next(call)

######################################################

# generator = (num ** 2 for num in range(10)) 
# for num in generator:
#     print(num)

# def csv_reader(file_name):
#     file = open(file_name)
#     result = file.read().split("\n")
#     return result

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

# csv_gen = (row for row in open(file_name))

csv_gen = csv_reader("C:/Users/Admin/Desktop/Open.src/bug-free-potato/Python/some_csv.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

# In addition to yield, generator objects can make use of the following methods:

# .send()
# .throw()
# .close()