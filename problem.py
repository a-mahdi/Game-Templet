# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:35:26 2022

@author: amahd
"""

class Problem(object):
    
    def __init__(self,initial_state,goal_state=None):
        self.goal_state=goal_state
        self.initial_state= initial_state
        
    def actions(self,state):
        raise NotImplementedError("this is should be implemented in the subclass")
        
    def result(self,state, action):
        raise NotImplementedError("this is should be implemented in the subclass")

    def is_goal(self,state):
        return state==self.goal_state
            
        
            
        
    
    def action_cost(self,state1,action,state2):
        return 1
    
    def h(self,node):
        return 0
    
    
    
    
    
        
        
        
       
        
    