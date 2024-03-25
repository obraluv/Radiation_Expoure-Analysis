import statistics  # module is imported in order to calculate standard deviation

Location =  ['City_Centre', 'Industrial_Zone', 'Residential_District', 'Rural_Outskirts', 'Downtown']
Radiation_levels = [[22, 19, 20, 31, 28], [35, 32, 30, 37, 40], [15, 12, 18, 20, 14], [9, 13, 16, 14,7], [25, 18, 22, 21, 26]]

level_total = []  # an empty string is created to store all radiation levels provided above and get their total

for level in Radiation_levels:  # a for loop to iterate the radiation levels list and get hold of each radiation level
    level_total += level        # add each radiation level to the empty list created
average = sum(level_total) / len(level)  # calculate the average by diving the sum total of all radiation levels by their total number
std_dev = statistics.stdev(level_total)   # calculkate standard deviation by calling the statistics module

print(f"The Average is : {average}")
print(f"The standard deviation is {std_dev}")

# the line of code below sets a condition to true if the user has more input,and a while loop is created that continues
# to iterate as long as the user has more input.
more_radiation_levels = True 
while more_radiation_levels:
    user_input = input("Do you have more radiation levels? 'Y' or 'N'?")
    if user_input == 'Y'.lower():
        
        # a try-except block is formed to get hold of the user input error and avoid program from crashing
        try:
            # if user input more than one radiation level, input is split into a list of substrings, using the comma as the delimiter.
            new_level = (input("Please enter your radiation level:")).split(',')
            
            # Each substring between the commas is extracted and converted to integer then added to a new list named new_measurement .
            new_measurement =[int(x) for x in new_level]
            
            # sum of the new_radiation levels are calculated and printed out
            new_measurement_total = sum(new_measurement)
            
            print(f"New level added: {new_measurement}")
            print(new_measurement_total)
        
        # if the user input is different from what is expected, the exception below is raised telling the user what is expected
        except ValueError:
            print("Invalid input, please input a numerical value, separate with a comma if more than 1.")
    
    # if the user has no more input, the while loop is exit by setting the condition created above to false
    elif user_input == 'N'.lower():
        more_radiation_levels = False
        print("Exit")
    
    else:
        print("Invalid input, please enter Y or N ")
    

