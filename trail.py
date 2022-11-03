#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:08:32 2022

@author: parth
"""

x = [
     'a',
     'b',
     {
      'foo':1, 
      'bar': 
          {'x' : 10, 
           'y': 20, 
           'z':30}, 
          'baz':3}, 
         'c', 
         'd'
         ]
    
    
    
class Airplane:
    def __init__(self, manufacturer:str, model:str):
        self.manufacturer = manufacturer
        self.model = model
        self.engine_on = False 
        self.flying = False
        
        print(f'Created a new {self.manufacturer} {self.model}airplane')
    def __repr__(self):
        return f'{self.manufacturer}{self.model}'
    
    @classmethod
    def from_string(cls, name:str):
        import re 
        m = re.search(r"([a-zA-z]+)(\d+)",name)
        if m:
            return cls(m.group(1), m.group(2))
        raise Exception("Invalid")
    
class Hangar:
    def __init__(self, airplanes:list):
        self.airplanes = [Airplane.from_string(i) for i in airplanes]
    
    def count(self):
        return len(self.airplanes)
