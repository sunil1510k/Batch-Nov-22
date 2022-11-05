
import sys

x = 10
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))

print('--------------------------------------------------------------')

x = 10.55
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))


print('--------------------------------------------------------------')

x = "10"
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))


print('--------------------------------------------------------------')

x = True
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))


print('--------------------------------------------------------------')

x = 10j
print( 'Value of x = ', x )
print( 'Type of x = ', type(x ))
print( 'Memory Allocated to x = ', sys.getsizeof(x), "bytes" )
print('Memory address at which x is stored', id(x))

