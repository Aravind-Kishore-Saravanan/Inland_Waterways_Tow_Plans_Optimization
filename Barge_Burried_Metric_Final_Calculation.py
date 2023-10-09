import pandas as pd
import numpy as np
import Connections_Calculation
import Barge_Metric_Calculation


file_path = "C:/Users/aravi/Desktop/Matrix.xlsx"  # The file path that has the Fleet Configuration

# Assuming the data starts from the first cell (A1) in the Excel sheet
data_frame = pd.read_excel(file_path, sheet_name="Fleet_Configuration_Input")

# Convert the data into a matrix.
Barge_Matrix = data_frame.values
print(Barge_Matrix)

# Calculate the number of connections of each Barge in the Fleet
Connections_Matrix = Connections_Calculation.calculate_connections(Barge_Matrix)
print(Connections_Matrix)

# Calculate the single shot barge burried metric of each Barge
Metric_Matrix = Barge_Metric_Calculation.calculate_metric(Connections_Matrix)
print(Metric_Matrix)

# Converting Metric Matrix into a list
Barge_Matrix_Array = np.array((Barge_Matrix))
Barge_List = [1,2,3,4,5,6,7,8,9,10,11,12]
Single_Shot_Barge_Burried_Metric = []

for i in Barge_List:
    a = np.where(Barge_Matrix_Array == i)
    Single_Shot_Barge_Burried_Metric.append(Metric_Matrix[a[0][0]][a[1][0]])

print(Barge_List)
print(Single_Shot_Barge_Burried_Metric)



