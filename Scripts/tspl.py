# -*- coding: utf-8 -*-
"""
    TSPL - TimScriptProgrammingLanguage

 A functional programming language and interpreter in python
 - more of a learning device than a practical use language


Created on Sat May  9 20:24:51 2020

@author: tim_s
"""



class Exp:
    """ An expression to be evaluated """
    
    def __init__(self):
        pass


class Const(Exp):
    """ A constant int """
    
    def __init__(self, num: int):
        super().__init__()
        self.num = num
        
        
class Neg(Exp):
    """ Negated expression """
    def __init__(self, exp: Exp):
        super().__init__()
        self.num = num
  
      
class Add(Exp):
    """ Expression representing the result
        of adding two expressions 
    """
    
    def __init__(self, exp1: Exp, exp2: Exp):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2
      
        
class Mult(Exp):
    """ Expression representing the result
        of multiplying two expressions 
    """
    def __init__(self, exp1: Exp, exp2: Exp):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2
    
    
class Div(Exp):
    """ Expression representing the result
        of dividing two expressions 
    """
    
    def __init(self, exp1: Exp, exp2: Exp):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2


class Var(Exp):
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
        inp: Exp = input('>>> ')
        self.eval_exp(inp)
    
    def eval_exp(self, exp: Exp):
        print("Not yet implemented")
        
