import numpy as np
import pandas as pd

# Importing Barge List
data_frame2 = pd.read_excel("C:/Users/aravi/Desktop/Model_Input.xlsx", sheet_name="Barge_List")
Barge_Matrix = data_frame2.values
Barges = Barge_Matrix[0]

# Vessels List
Vessels = [1,2,3,4]

# Importing the Processing Times
data_frame4 = pd.read_excel("C:/Users/aravi/Desktop/Model_Input.xlsx", sheet_name="Processing_Time_Matrix")
Time_Matrix = data_frame4.values
Process_Times = Time_Matrix[:, 1:]

# Initializing Assignment, Available_Times and Process_Times Array
Assignment = np.zeros((len(Barges), len(Vessels)))
Available_Times = np.zeros(len(Vessels))
Process_Times = np.array(Process_Times)

# Calculating Assignment Matrix
for i in range(len(Barges)):
    minimum_available_time = np.where(Available_Times == np.min(Available_Times)) # Find Minimum available time of the vessels
    minimum_available_processing_time = np.min(Process_Times[i,minimum_available_time]) # Find processing time of barge for the vessel with minimum available time
    for j in minimum_available_time[0]:
        if Process_Times[i][j] == minimum_available_processing_time:
            Assignment[i][j] = 1   # Assign the value 1 to the vessel whose processing time is equal to minimum availabe processing time
            Available_Times[j] += Process_Times[i][j] # Update the available time of the assigned vessel with the processing time of the barge by the vessel
            break

# Printing the Assignment Matrix which has values 1 if a barge is assigned to a vessel
print(Assignment)
