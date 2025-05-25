# [Mean-Variance-Standard Deviation Calculator](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator)

Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

# Development
Write your code in mean_var_std.py. For development, you can use main.py to test your code. In order to run your code, type python3 main.py into the GitPod terminal and hit enter. This will cause the included CPython interpreter to run the main.py file.

# Testing
The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience.
