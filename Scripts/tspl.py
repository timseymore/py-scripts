# -*- coding: utf-8 -*-
"""
    TSPL - TimScriptProgrammingLanguage

 A functional programming language and interpreter in python
 - more of a learning device than a practical use language


Created on Sat May  9 20:24:51 2020

@author: tim_s
"""

import sys, os


# TODO: change implementation to use pure OOP

class Exp:
    """ An expression to be evaluated 
    
    can put default behaviour here    
    """    
    def __init__(self):
        pass


class Int(Exp):
    """ A constant int """    
    def __init__(self, num: int):
        super().__init__()
        self.num = num
        
        
class Negate(Exp):
    """ Negated expression """
    def __init__(self, exp: Exp):
        super().__init__()
        self.exp = exp
  
      
class Add(Exp):
    """ Expression representing the result
        of adding two expressions 
    """    
    def __init__(self, exp1: Exp, exp2: Exp):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2
      
        
class Multiply(Exp):
    """ Expression representing the result
        of multiplying two expressions 
    """
    def __init__(self, exp1: Exp, exp2: Exp):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2
    
    
class Divide(Exp):
    """ Expression representing the result
        of dividing two expressions 
    """    
    def __init(self, exp1: Exp, exp2: Exp):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2


class Variable(Exp):
    """ A variable mapping a string to an expression """    
    def __init__(self, name: str, value: Exp):
        super().__init__()
        self.name = name
        self.value = value
        

class Pair(Exp):
    """ A pair of expressions
    
       use Nul expression to end list
       ex: Pair(e1, Pair(e2, Nul)) == [e1, e2]
    """    
    def __init__(self, exp1: Exp, exp2: Exp):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2
        
        
class Nul(Exp):
    """ Used to represent a null value """    
    def __init__(self):
        super().__init__()
        

class Interpreter:
    """ TSPL interpreter """    
    def __init__(self):
        self.run()
        
    def run(self):
        while True:
            inp: Exp = input('>>> ')
            if inp == 'quit':
                sys.exit()
            self.eval_exp(inp)
    
    def eval_exp(self, exp: Exp):
        print("Eval not yet implemented")
        
        
        
        
if __name__ == "__main__":
    Interpreter()
    