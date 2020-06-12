# -*- coding: utf-8 -*-
"""
    TSPL - TimScriptProgrammingLanguage

 A simple programming language and interpreter in python
 - more of a learning device than a practical use language


Created on Sat May  9 20:24:51 2020

@author: tim_s
"""

# import sys, os


class Exp:
    """ An expression to be evaluated 
    
    can put default behaviour here    
    """    
    def __init__(self):
        pass


class Int(Exp):
    """ A constant int """    
    def __init__(self, i):
         super().__init__()
         self.i = i
        
    def eval(self):
        return self
    
    def __str__(self):
        return str(self.i)
    
    def has_zero(self):
        return self.i == 0
        
        
class Negate(Exp):
    """ Negated expression """
    def __init__(self, e):
        super().__init__()
        self.e = e
        
    def eval(self):
        return Int(-(self.e.eval()))
    
    def __str__(self):
        return "-(" + str(self.e) + ")"
        
    def has_zero(self):
        return self.e.has_zero()        
  
      
class Add(Exp):
    """ Expression representing the result
        of adding two expressions 
    """    
    def __init__(self, e1, e2):
        super().__init__()
        self.e1 = e1
        self.e2 = e2
        
    def eval(self):
        return Int(self.e1.eval().i + self.e2.eval().i)
    
    def __str__(self):
        return "(" + str(self.e1) + " + " + str(self.e2) + ")"
    
    def has_zero(self):
        return self.e1.has_zero() or self.e2.has_zero()
      
        
class Multiply(Exp):
    """ Expression representing the result
        of multiplying two expressions 
    """
    def __init__(self, e1, e2):
        super().__init__()
        self.e1 = e1
        self.e2 = e2
        
    def eval(self):
        return Int(self.e1.eval().i * self.e2.eval().i)
    
    def __str__(self):
        return "(" + str(self.e1) + " * " + str(self.e2) + ")"
    
    def has_zero(self):
        self.e1.has_zero() or self.e2.has_zero()
        
        
# TODO: change implementation to use pure OOP
    
# class Divide(Exp):
#     """ Expression representing the result
#         of dividing two expressions 
#     """    
#     def __init(self, exp1: Exp, exp2: Exp):
#         super().__init__()
#         self.exp1 = exp1
#         self.exp2 = exp2


# class Variable(Exp):
#     """ A variable mapping a string to an expression """    
#     def __init__(self, name: str, value: Exp):
#         super().__init__()
#         self.name = name
#         self.value = value
        

# class Pair(Exp):
#     """ A pair of expressions
    
#        use Nul expression to end list
#        ex: Pair(e1, Pair(e2, Nul)) == [e1, e2]
#     """    
#     def __init__(self, exp1: Exp, exp2: Exp):
#         super().__init__()
#         self.exp1 = exp1
#         self.exp2 = exp2
        
        
# class Nul(Exp):
#     """ Used to represent a null value """    
#     def __init__(self):
#         super().__init__()
        

# class Interpreter:
#     """ TSPL interpreter """    
#     def __init__(self):
#         self.run()
        
#     def run(self):
#         while True:
#             inp: Exp = input('>>> ')
#             if inp == 'quit':
#                 sys.exit()
#             self.eval_exp(inp)
    
#     def eval_exp(self, exp: Exp):
#         print("Eval not yet implemented")
        
        
        
        
# if __name__ == "__main__":
#     Interpreter()
    