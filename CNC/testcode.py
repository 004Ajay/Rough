# Define the starting position of the tool
x = 0
y = 0
z = 0

# Define the feed rate (units per minute)
feed_rate = 100

# Define the depths for each pass of the tool
depths = [1, 2, 3, 4]

# Generate the CNC codes
codes = []
for depth in depths:
  # Rapidly move the tool to the starting position
  codes.append(f"G00 X{x} Y{y} Z{z}")
  
  # Move the tool down to the specified depth
  codes.append(f"G01 Z{depth} F{feed_rate}")
  
  # Rapidly move the tool back to the starting position
  codes.append(f"G00 Z{z}")

# End the program
codes.append("M02")

# Print the generated codes
print("\n".join(codes))


"""

This program generates a set of CNC codes that instruct a CNC milling machine to move rapidly to a starting position,
move down to a specified depth, and then move back up to the starting position. The specific movements and depths
are specified by the variables defined at the beginning of the program. This program could be extended to include additional
actions and more complex movements, depending on the specific needs of the CNC machine.

"""