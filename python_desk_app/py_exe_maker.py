"""
You can use the pyinstaller package to package a Python script into a standalone executable with an icon. 
This command will create a standalone executable in the dest folder. The executable will have the specified icon.
"""


# First, install pyinstaller using pip
!pip install pyinstaller

# Next, navigate to the directory where your Python script is located
# and run the following command to package the script with an icon
!pyinstaller --onefile --icon=path/to/icon.ico script.py



