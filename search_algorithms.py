# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:58:43 2022

@author: amahd
"""

import node
import problem


def expand(self,problem,node):
    s=node.state
    for x in problem.actions(s):
        s2=problem.result(s,x)
        cost= node.
        
    