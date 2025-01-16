'''
This program will calculate the surface area of one side of a cube, the total surface area, and the volume
based on the users input of one edge of the cube.
'''

# Initialize a variable with the users input using the input function, 
# and then convert the input to an integer using the int function.
user_input = int(input("Enter the length of one edge of the cube: "))

# Calculate the surface area of one side of the cube by multiplying the user input by itself.
side_area = user_input * user_input

# Calculate the total surface area of the cube by multiplying the surface area of one side by 6.
total_area = side_area * 6

# Calculate the volume of the cube by cubing the user input.
volume = user_input ** 3

# Create an f-string to format results
results = f"""
The surface area of one side of the cube is: {side_area}
The total surface area of the cube is: {total_area}
The volume of the cube is: {volume}
"""

# Print the results
print(results)