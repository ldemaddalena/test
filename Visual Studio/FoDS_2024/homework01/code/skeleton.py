"""Solution for HW01, Foundations of Data Science (376-1983-00L),
Spring Semester 2024."""

import pandas as pd
import seaborn as sns

# load data
hospitals = pd.read_csv("c:/Users/leond/Visual Studio/FoDS_2024/homework01/data/data.csv", index_col=0)

# --------------------------------------------------------------------------------------
# ############################### #
# ##### Getting an overview ##### #
# ############################### #
# question 1
n_rows = hospitals.shape[0]
n_cols = hospitals.shape[1]
print(n_rows, n_cols)

# question 2
n_hospitals = hospitals["Facility.Name"].nunique()
print(n_hospitals)

# question 3
n_states = hospitals["Facility.State Name"].nunique()
print(n_states)
"""
# question 4
most_expensive_hip_and_knee_name = # your solution
most_expensive_hip_and_knee_city = # your solution
most_expensive_hip_and_knee_state = # your solution

# question 4
most_expensive_hip_and_knee_delta = # your solution

# question 5
least_expensive_total_name = # your solution
least_expensive_total_city = # your solution
least_expensive_total_state = # your solution
# ################################ #
# DO NOT change the following code #
# ################################ #
print("*" * 10 + " Getting an overview " + "*" * 10)
print(f"There are {n_rows} rows in the data.")
print(f"There are {n_cols} columns in the data.")
print(f"Data on {n_hospitals} distinct hospitals is reported.")
print(f"{n_states} states are represented in the data.")
print(
    "The most expensive hospital for hip and knee procedures is "
    + most_expensive_hip_and_knee_name
    + " in "
    + most_expensive_hip_and_knee_city
    + ", "
    + most_expensive_hip_and_knee_state
    + "."
)
print(
    f"It's US${most_expensive_hip_and_knee_delta} more expensive than the "
    + "second most expensive hospital."
)
print(
    "The least expensive hospital overall is "
    + least_expensive_total_name
    + " in "
    + least_expensive_total_city
    + ", "
    + least_expensive_total_state
    + "."
)
# --------------------------------------------------------------------------------------
# ##########################
# ##### Missing data ##### #
# ##########################
# question 1
columns_with_missing_data = # your solution (array or list with columns containing missing data)
# question 2

# ################################ #
# DO NOT change the following code #
# ################################ #
print("*" * 10 + " Missing data " + "*" * 10)
print(f"Missing data found in {len(columns_with_missing_data)} columns.")
# --------------------------------------------------------------------------------------
# ############################### #
# ##### Basic visualisation ##### #
# ############################### #
# question 1
fig_pneumonia_cost = # your solution
# DO NOT modify line below
fig_pneumonia_cost.savefig("../output/pneumonia.png")
# question 2
fig_heart_failure_cost_vs_quality = # your solution
# DO NOT modify line below
fig_heart_failure_cost_vs_quality.savefig("../output/heart-failure-cost-vs-quality.png")
"""