import math # Will use to calculate
import pandas as pd # Will use to make table
import matplotlib.pyplot as plt # Will use to draw graph

#Note: I created this code by myself, and not copy anywhere else. I also do not use AI for writing my code.

# Function to calculate concentration for 1st Order Integrated Rate Law
def calc_concentration(c0,k,t):
    c = c0*math.exp(-k*t)
    rounded_c = round(c,2)
    return rounded_c

# Function to calculate half-life for 1st Order Integrated Rate Law
def calc_half_life(k):
    half_life = math.log(2)/k
    rounded_half_life = round(half_life, 2)
    return rounded_half_life

# Let say this is our value from experiment:
c0 = float(input("Enter the initial concentration (c0): "))
k = float(input("Enter the rate constant (k): "))
t = []
count = 1

while count==1:
    t.append(int(input("Enter the time value (seconds): ")))
    print("Do you want to add more input for time? (y/n)")
    answer = input("")
    if answer.lower() != "y":
        count = 0
    

# Create a list here to organize the data in Pandas
list_of_c = []
list_of_half_life = []

# Coding for calculating the value, also put those data in the list
for i, t_val in enumerate(t):
    list_of_c.append(calc_concentration(c0,k,t_val))
    list_of_half_life.append(calc_half_life(k))
print("For 1st Order Integrated Rate Law, rate constant (k) remains the same over time. Your k value is ",k)
# This is for organized data (using Pandas)
data = {
    "Time (s)": t,
    "Final Concentration (M)": list_of_c,
}

# Create a table here
df = pd.DataFrame(data)
print(df.to_string(index=False))

# Try to create a graph out of data
df.plot(x="Time (s)", y="Final Concentration (M)", kind="line", marker= "o")

# Adding labels for the graph
plt.title("Concentration over Time")
plt.ylabel("Concentration (M)")
plt.grid(True)
plt.show()