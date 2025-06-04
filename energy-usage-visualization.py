#!/usr/bin/env python
# coding: utf-8

# # Energy Consumption Analysis in Ireland (1990-2022)

# This Jupyter Notebook analyzes energy consumption trends in Ireland using data exported from the Sustainable Energy Authority of Ireland (SEAI). 
# We visualize the data through both line plots and stack plots to examine individual fuel type contributions as well as overall energy trends.

# # Step 1: Import Necessary Libraries

# In[1]:


import matplotlib.pyplot as plt # matplotlib.pyplot is used for plotting graphs
import numpy as np # Numpy python library is used for handling arrays & numerical operations


# # Step 2: Load Dataset and Extract Headers
# 

# In[3]:


# Define the file path
file_path = r'C:\Users\KRISHNA SURESH\Downloads\energy_data.csv' #The r denotes a raw string which enables Python to interpret backslashes in the string as literal characters and not as escape characters


# In[ ]:


# Load the data skipping the first row (header) and the first column ('Year')
# numpy's genfromtxt function is used to load data from the CSV file. 
# The delimiter=',' specifies that the file is comma-separated. 
# skip_header=1 enables to ignore the first row, which is the header row with column names.
data = np.genfromtxt(file_path, delimiter=',', skip_header=1)

# Opens the CSV file to read the headers. 
# readline() reads the first line, strip() removes any whitespaces, and split(',') splits the header string into a list at the commas.
with open(file_path, 'r') as csvfile:
    headers = csvfile.readline().strip().split(',')


# # Step 3: Line Plot of Energy Usage by Fuel Type
# 

# In[ ]:


# Extract the 'Year' column for the x-axis.
# The colon : in data[:, 0] is used to select all rows (:) of the first column (0) of the data array.
# The first column in the CSV file is 'Year'.
years = data[:, 0]  

# Create a line plot for each fuel type over time
# Creates a figure with a specified size of 15x10 inches.
plt.figure(figsize=(15, 10)) 

# Iterate over each fuel type and plot its trend
# The for loop iterates over the columns of the data (except the first column, which is 'Year'). 
# For each column, it creates a line plot with years on the x-axis and the energy data on the y-axis.
# Use label=headers[i] to assign the corresponding header as the label for the legend.
for i in range(1, data.shape[1]):  # Starting from 1 to skip the 'Year' column.
    plt.plot(years, data[:, i], label=headers[i])

# Plot total energy usage across all fuel types    
# calculates the total energy consumption by summing all columns for each row except the first column.
#(data[:, 1:]). sum(axis=1) performs the summation across rows.
# Plot the total energy consumption with a thicker black line (color='k' and linewidth=3).
total_energy = data[:, 1:].sum(axis=1)
plt.plot(years, total_energy, label='Total', color='k', linewidth=3)

# Add legend, labels, title, and grid to the line plot.
plt.legend(loc='upper left',shadow=True) # legend function.

plt.xlabel('Year')
plt.ylabel('Energy Consumption')
plt.title('Energy Consumption by Fuel Type in Ireland (1990-2022)')
plt.grid(True)

# Show the line plot created.
plt.show()


# # Step 4: Stack Plot of Energy Usage by Fuel Type

# In[ ]:


# Create stackplot here.

# Create a new figure for the stack plot.
plt.figure(figsize=(15, 10))

# Prepare data for stack plot (Exclude 'Year' column).
data_to_stack = [data[:, i] for i in range(1, data.shape[1])]  

# Plot the stack plot.

# The stackplot function is called with years as the x-axis and data_to_stack as the y-axis values, creating a stack plot. 
# labels=headers[1:] uses the headers (excluding 'Year') for the legend.
plt.stackplot(years, data_to_stack, labels=headers[1:])

# Add legend, labels, title, and grid to the stack plot.
plt.legend(loc='upper left',shadow=True) # legend function.

plt.xlabel('Year')
plt.ylabel('Energy Consumption')
plt.title('Stack Plot of Energy Consumption by Fuel Type in Ireland (1990-2022)')
plt.grid(True)

# Show the stack plot created.
plt.show()


# # Summary

# This notebook provides:
#  - A clear line plot showing trends in energy use by fuel type.
#  - A stacked area chart visualizing contributions of each fuel type to total energy.
#  - A useful visual comparison of individual and collective energy consumption patterns in Ireland over 30 years.
# 

# In[ ]:




