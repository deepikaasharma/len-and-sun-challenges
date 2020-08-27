list_of_lists = [[1, 2, 3], [1.0, 2.0, 3.0]]

print(len(list_of_lists))

list_to_sum = [112, 115, 276, 431]
print(sum(list_to_sum))

"""Given this list of daily high temperatures:

daily_temps = [61.2, 59.0, 59.4, 58.9, 60.1, 55.3, 55.6]

Calculate the average high for this week.

Note:

    You are trying to calculate the mean of this list
    Use the sum() and len() functions to do this
    Give the exact answer that appears when you calculate the answer in python

"""
daily_temps = [61.2, 59.0, 59.4, 58.9, 60.1, 55.3, 55.6]

print(len(daily_temps))
print(sum(daily_temps)/len(daily_temps))