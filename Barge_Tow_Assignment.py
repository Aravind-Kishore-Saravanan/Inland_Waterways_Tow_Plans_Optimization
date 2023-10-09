import gurobipy as gp

from gurobipy import GRB
from gurobipy import quicksum
import pandas as pd

file_path = "C:/Users/aravi/Desktop/Model_Input.xlsx"  # The file path that has the Input Values

data_frame = pd.read_excel(file_path, sheet_name="Destination_Matrix")
Destination_Matrix = data_frame.values
Barge_Destination = Destination_Matrix[:, 1:]  # Creating a Matrix for Barge and its Destination

data_frame2 = pd.read_excel(file_path, sheet_name="Barge_List")
Barge_Matrix = data_frame2.values
Barges = Barge_Matrix[0] # Creating the list of Barges

data_frame3 = pd.read_excel(file_path, sheet_name="Distance_Matrix")
Distance_Matrix = data_frame3.values
Distance = Distance_Matrix[:, 1:] # Creating a Matrix for Distance between Barge and Tow Locations

data_frame5 = pd.read_excel(file_path, sheet_name="Priority_Element_Input")
Priority_Matrix = data_frame5.values
Priority = Priority_Matrix[:, 1:] # Creating a Matrix for Priority element of Barges if assigned to tows


Tows=[1] # List of Tows to be Built

Vessels=[1,2,3,4] # List of Vessels available to carry the barges from fleet to the tow location


Ports = [100,77,61,57,86.5,55.3,56,102] # List of Destination Mile Points

Up_Speed = [6,6,6,6] # Upstream speed of Vessel

Down_Speed =[10,10,10,10] # Downstream speed of Vessel

Unit_Operating_Cost = 12 # Cost of Operating the Vessel per unit time

Tow_Capacity=[54] # Capacity of the Tows

Fixed_Stopping_Cost = 1000 # Cost Incurred when a Tow stops at a port

Stopping_Cost=50 # Cost Incurred per Barge for its unloading in the destination port

M = 10000 # A large Constant

# Creating the Model
m = gp.Model("Barge-Tow_Assignment")

# Decision Variables
X = {}
Y = {}
Z = {}

for b in range(len(Barges)):
    for v in range(len(Vessels)):
        for t in range(len(Tows)):
            X[b,v, t] = m.addVar(vtype=GRB.BINARY, name="X[" + str(b) + "," + str(v) + "," +str(t) + "]", lb=0)
for t in range(len(Tows)):
   for p in range(len(Ports)):
        Y[t, p] = m.addVar(vtype=GRB.BINARY, name="Y[" + str(t) + "," + str(p)  + "]", lb=0)
for t in range(len(Tows)):
    for p in range(len(Ports)):
        Z[t, p] = m.addVar(vtype=GRB.INTEGER, name="Z[" + str(t) + "," + str(p)  + "]", lb=0)


# Objective Function
m.setObjective(
    0.5*(quicksum(X[b, v, t] * Unit_Operating_Cost * (((Distance[b][t])/Up_Speed[v])+((Distance[b][t])/Down_Speed[v])) for b in range(len(Barges)) for v in range(len(Vessels)) for t in range(len(Tows))) +
    quicksum(Y[t, p] * Fixed_Stopping_Cost for t in range(len(Tows)) for p in range(len(Ports)))+
    quicksum(Z[t, p] * Stopping_Cost for t in range(len(Tows)) for p in range(len(Ports))))
    + 0.5*(quicksum(X[b, v, t] * Priority[b][t] for b in range(len(Barges)) for t in range(len(Tows)) for v in range(len(Vessels))))
    , GRB.MINIMIZE) # Multi Objective Function with 0.5 weight for two minimization problems

# Constraints
for b in range(len(Barges)):
    m.addConstr(quicksum(X[b, v, t] for v in range(len(Vessels)) for t in range(len(Tows))) == 1) # Makes sure that a barge is assigned to only one vessel and one tow
for t in range(len(Tows)):
    m.addConstr(quicksum(X[b, v, t] for v in range(len(Vessels)) for b in range(len(Barges))) <= Tow_Capacity[t]) # Ensures that the total number of barges assigned to a tow doesn’t exceed the capacity of the tow
for t in range(len(Tows)):
    for p in range(len(Ports)):
        m.addConstr(quicksum(X[b, v, t] * Barge_Destination[b][p]  for b in range(len(Barges)) for v in range(len(Vessels)) ) == Z[t,p]) # Calculates the number of barges a Tow carries to a Port
for t in range(len(Tows)):
    for p in range(len(Ports)):
        m.addConstr(Z[t,p] <= M*Y[t, p]) # Makes sure that Y_tp takes the value of 1 only when a tow is stopping at a port and the value of Z_tp  is greater than 0



# Solving the Model
m.optimize ()


# Feasibility Check and Population of Results
if m.status == GRB.INFEASIBLE:
    print("The model is infeasible.")

    # Compute the Irreducible Inconsistent Subsystem (IIS)
    m.computeIIS()

    # Print the infeasible constraints
    print("Infeasible constraints:")
    for constr in m.getConstrs():
        if constr.IISConstr:
            print(constr.ConstrName)
else:
    print("The model is feasible.")

for v in m.getVars():
    if v.x >=1:
        print((v.VarName, v.x))
