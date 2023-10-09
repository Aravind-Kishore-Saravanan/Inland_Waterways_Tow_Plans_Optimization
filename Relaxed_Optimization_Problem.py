import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum
import numpy as np
import pandas as pd

# Importing Barge List
data_frame2 = pd.read_excel("C:/Users/aravi/Desktop/Model_Input.xlsx", sheet_name="Barge_List")
Barge_Matrix = data_frame2.values
Barges = Barge_Matrix[0]

# Order Sequence
Order = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]

# Vessel List
Vessels = [1, 2, 3, 4]

# Importing Processing Times
data_frame4 = pd.read_excel("C:/Users/aravi/Desktop/Model_Input.xlsx", sheet_name="Processing_Time_Matrix")
Time_Matrix = data_frame4.values
Process_Times = Time_Matrix[:, 1:]

# Vessel Available Time which denotes the maximum time of operating the vessels
Vessel_Available_Time = [6, 6, 6, 6]

# Priority Element Matrix - If a barge is scheduled in the order defined by Phase 1, the priority is 1, else the priority is 2.
# This is to ensure barges are scheduled in that sequence
Priority = np.full((len(Barges),len(Barges)),2)
for i in range(len(Barges)):
    for j in range(len(Barges)):
        if i == j:
            Priority[i][j] = 1

# Creating the Model
m = gp.Model("Barge-Tow_Assignment")

# Decision Variables
X = {}
T = {}
for b in range(len(Barges)):
    for v in range(len(Vessels)):
        for o in range(len(Order)):
            X[b, v, o] = m.addVar(vtype=GRB.BINARY, name="X[" + str(b) + "," + str(v) + "," + str(o) + "]", lb=0) # 1 if Barge b is assigned to Vessel v in Order Sequence o, 0 otherwise
for v in range(len(Vessels)):
    T[v] = m.addVar(vtype=GRB.CONTINUOUS, name="T[" + str(v) + "]", lb=0) # Total Operational time of Vessel v

# Objective function
m.setObjective(
    0.5 * (quicksum(X[b, v, o] * Process_Times[b][v] for b in range(len(Barges)) for v in range(len(Vessels)) for o in range(len(Order))))
    + 0.5 *(quicksum(X[b, v, o] * Priority[b][o] for b in range(len(Barges)) for v in range(len(Vessels)) for o in range(len(Order)))),
    GRB.MINIMIZE) # Multi objective with two minimization problems with 0.5 weights

#Constraints
for b in range(len(Barges)):
    m.addConstr(quicksum(X[b, v, o] for v in range(len(Vessels)) for o in range(len(Order))) == 1) # Ensures that a barge is assigned to only one vessel in one order sequence

for v in range(len(Vessels)):
    m.addConstr(quicksum(X[b, v, o] * Process_Times[b][v] for b in range(len(Barges)) for o in range(len(Order))) == T[v]) # Calculate the total time to process all the assigned barges by a vessel

for v in range(len(Vessels)):
    m.addConstr(T[v] <= Vessel_Available_Time[v]) # Ensures that the total operational time of a vessel doesn’t exceed the available time of that vessel

# Solve the Model
m.optimize ()

# Print the Results
for v in m.getVars():
    if v.x >=0.1:
        print((v.VarName, v.x))
