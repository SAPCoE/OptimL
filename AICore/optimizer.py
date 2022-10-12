import pyomo
from pyomo.environ import *
def make_change_pyomo(amount, coins):
    model = ConcreteModel()
    model.x = Var(coins.keys(), domain=NonNegativeIntegers)
    
    model.amount = Constraint(expr = sum(model.x[c]*coins[c] for c in coins.keys()) == amount)
    
    model.total = Objective(expr = sum(model.x[c] for c in coins.keys()), sense=minimize)

    SolverFactory('gurobi').solve(model)
    return {c: int(model.x[c]()) for c in coins.keys()} 

import gurobipy as gp
def make_change_gurobi(amount, coins):
    model = gp.Model('coin-changer-gurobi')
    x = model.addVars(coins.keys(), vtype=gp.GRB.INTEGER,name='x')
    model.addConstr(sum(x[c]*coins[c] for c in coins.keys()) == amount)
    model.setObjective(sum(x[c] for c in coins.keys()), sense=gp.GRB.MINIMIZE)
   
    model.optimize()
    return {c: int(x[c].x) for c in coins.keys()} 

import xpress as xp
def make_change_xpress(amount, coins):
    model = xp.problem('coin-changer-xpress')
    x = {(c): xp.var(vartype=xp.integer,name='x(' + c + ')') for c in coins.keys()}
    model.addVariable(x)
    model.addConstraint(sum(x[c]*coins[c] for c in coins.keys()) == amount)
    model.setObjective(sum(x[c] for c in coins.keys()), sense=xp.minimize)
    
    model.solve()
    return {c: int(model.getSolution(x[c])) for c in coins.keys()} 