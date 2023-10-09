import pandas as pd

# Importing the input values of Parameters to calculate priority score
file_path = "C:/Users/aravi/Desktop/Matrix.xlsx"  # The file path that has the input data of parameters
sheet_name2 = "Priority_Calculation_Input"  # Sheet name of the file
data_frame_2 = pd.read_excel(file_path, sheet_name=sheet_name2)

# Normalization of Parameters
Min_Time_in_Fleet = data_frame_2['Time_in_Fleet'].min()
Max_Time_in_Fleet = data_frame_2['Time_in_Fleet'].max()
data_frame_2['N_Time_in_Fleet'] = 1 - (
            (data_frame_2['Time_in_Fleet'] - Min_Time_in_Fleet) / (Max_Time_in_Fleet - Min_Time_in_Fleet))
Min_Time_to_Deliver = data_frame_2['Time_to_Deliver'].min()
Max_Time_to_Deliver = data_frame_2['Time_to_Deliver'].max()
data_frame_2['N_Time_to_Deliver'] = (data_frame_2['Time_to_Deliver'] - Min_Time_to_Deliver) / (
            Max_Time_to_Deliver - Min_Time_to_Deliver)
Min_Commodity_Weightage = data_frame_2['Commodity_Weightage'].min()
Max_Commodity_Weightage = data_frame_2['Commodity_Weightage'].max()
data_frame_2['N_Commodity_Weightage'] = (data_frame_2['Commodity_Weightage'] - Min_Commodity_Weightage) / (
            Max_Commodity_Weightage - Min_Commodity_Weightage)
Min_Barge_Burried_Metric = data_frame_2['Barge_Burried_Metric'].min()
Max_Barge_Burried_Metric = data_frame_2['Barge_Burried_Metric'].max()
data_frame_2['N_Barge_Burried_Metric'] = (data_frame_2['Barge_Burried_Metric'] - Min_Barge_Burried_Metric) / (
            Max_Barge_Burried_Metric - Min_Barge_Burried_Metric)

# Calculating Priority Score by assigning equal weightage of 0.25 for all 4 parameters
data_frame_2['Priority'] = 0.25 * (data_frame_2['N_Time_in_Fleet']) + 0.25 * (
data_frame_2['N_Time_to_Deliver']) + 0.25 * (data_frame_2['N_Commodity_Weightage']) + 0.25 * (
                           data_frame_2['N_Barge_Burried_Metric'])

# Creating the sequence by sorting the priority scores
data_frame_2 = data_frame_2.sort_values(by='Priority')
Sequence = data_frame_2['Barge'].values

# Printing the Barge Sequence
print(data_frame_2)
print("The Sequence is", '\n', Sequence)
