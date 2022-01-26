import random
import itertools
import functools
import inspect

"""
define check_types
    if the severity is zero, return a no-op decorator
    define a generic messaging function that prints a message if the severity is 1 and raises a TypeError if the severity is 2
    define checker, which will itself be a decorator!
        look at the function's `__annotations__` - if there aren't any, forward the function through!
            make sure that each of the function's annotations is a type (e.g. int) and not some other value (e.g. 5)
        define a wrapper function, itself decorated with `functools.wraps`, which takes in *args and **kwargs
            bind the arguments *args and **kwargs to the original function, to see what _would_ go into the function
            check that each of the arguments match the expected type in the annotations dictionary, if its present
                if any fail, send a message that there was a violation
            compute the function's actual return value on the supplied arguments
            check that the return value matches the expected type of the return value in the annotations dictionary, if present
                if it fails, send a message that there was a violation
            return the return value
        return the wrapper function
    return the checker decorator
"""

def bind_args(function, *args, **kwargs):
    sig = inspect.signature(function).bind(*args, **kwargs)
    return sig.arguments

def demonstrate_complex_arguments(a, b=1, *c, d=1, **e):
    pass

d = bind_args(demonstrate_complex_arguments, 1, 2, 3, 4, d=10, e=11, f=12, g=13)

def foo_orig(a: int, b: str) -> bool:
    return b[a] == 'X'
    
def check_types(severity):
    def checker(function):
        
        def report(msg):
            if severity == 1:
                print('fail', msg)
            elif severity == 2:
                raise TypeError(msg)
                            
        
        if severity == 0:
            return function
        else:
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                sig = bind_args(demonstrate_complex_arguments, *args, **kwargs)
                sig = dict(sig)
                ann = function.__annotations__
                #print('sig', sig)
                #print('ann', ann)
                argsError = False
                for k,v in ann.items():
                    if k != 'return' and isinstance(v, type): #only check types, not hard coded values
                        if sig.get(k, None) and type(sig[k]) != v: #they do not match
                            report('arg: ' + k)
                            argsError = True
                output = None
                if not argsError:
                    output = function(*args, **kwargs)
                    k = 'return'
                    if k in ann:
                        v = ann[k]
                        if isinstance(v, type):
                            if sig.get(k, None) and type(sig[k]) != v:
                                report('return ' + k)
                    
                return output
                
            return wrapper
            
    return checker
    
    
@check_types(severity=1)
def foo(a: int, b: str) -> bool:
    return b[a] == 'X'
    


    

out0 = foo(1, "apple")
out1 = foo(1, "aXple")
out2 = foo(1, "XXXXX")

out3 = foo(0.5, "XXXXX")
out4 = foo(False, "XXXXX")
out5 = foo('hi', "XXXXX")

out6 = foo(6, 8687)
out7 = foo(6, 0.5)
out8 = foo(6, True)



print(out0, out1, out2)
print(out3, out4, out5)
print(out6, out7, out8)








