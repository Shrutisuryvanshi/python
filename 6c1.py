def outer_function(a, b):
   
    def inner_function():
        return a + b
    
    
    addition = inner_function()
    return addition + 5


result = outer_function(3, 4)
print(result)  
