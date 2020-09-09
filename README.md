## Function Plotter
A Cross platform desktop tool for plotting fucntions 

# Description
GUI application takes a string from user which has sequence of variable, operators and operands and takes minimum value and maximum value then pass it through some checking error, if it passes it, graph will be plotted in the same GUI

# Dependencies 
1. [PySide2](https://pypi.org/project/PySide2/)
   - To install it use following command
   ```
   pip3 install Pyside2
   ```
2. [Matplotlib](https://matplotlib.org/)
   - To install it use following command
   ```
   pip3 install matplotlib
   ```
3. [Numpy](https://numpy.org/)
   - To install it use following command
   ```
   pip3 install numpy
   ```
- There's deployment for **Linux OS** in this [Link](https://drive.google.com/file/d/1vPqj8I54hJtxIGi0Mzike1AzZR9YuhXm/view?usp=sharing)
- You can use the application withought downloading the deployment, just follow next steps
  1. clone the repository in your local disk
  2. open terminal in same directory which the repository has been downloaded
  3. write in terminal this command
  ```
  python3 GUI_main.py
  ```

# Supported equations
- the application supports the basics operation multiplication `*`, division `/`, addition `+`, subtraction `-` and power `^`
- the application supports any depth of parentheses
- the application doesn't support checking math as complex numbers: ![imaginary number](https://latex.codecogs.com/gif.latex?%5Csqrt%7B-1%7D)
- the application support any range input to plot the function if the function is defined in the given range
-  the application works with any **string** variable name 

# Code pipeline
The implementation of the application mainly is based on 2 algorithm or pipeline
1. Graphical user interface code or design
2. Logic code for processing the equation

The implemntation is designed so it can be easly add other operations or complex equation 
After filling the inputs in GUI and click **Plot** button, some checking error will be applied in the following sequence
  1. check if the equation section is empty
  2. check if there is wrong variable name or multiple variable names
  3. check if the maximum value section is empty
  4. check if the maximum value is valid number, not string or anything else
  5. check if the minimum value section is empty
  6. check if the minimum value is valid number, not string or anything else
  7. check if the maximum value is greater than minimum value, not less than or equal

If the inputs of the GUI are passed all of this checkings, the application will try a sample or test case to check if the equation has valid sequence of operators and operands
- try to solve the equation with the maximum value
  - check if there's invalid sequence of parentheses
  - check if there's invalid sequence of operators
  - check if there's invalid sequence of operands
  - check if the operators and operands aren't matching

It was the final check, if the equation passed it, the graph will be plotted in the same GUI
The graph is plotted using **Matplolib**, so we can get use of its toolbar in our application