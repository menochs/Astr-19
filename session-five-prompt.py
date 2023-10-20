# writes out a table of the function sin(x) vs. x 
# x is tabulated between 0 and 2pi with a thousand entries 

import numpy as np 

def main(): 
	# x is tabulated between 0 and 2pi with a thousand entries 
    x_values = np.linspace(0, 2 * np.pi, 1000)

    # Calculate sin values
    sin_values = np.sin(x_values)

    print("x          sin(x)")

    for i in range(1000):
        print(f"{x_values[i]:.5f}     {sin_values[i]:.5f}")

if __name__ == "__main__":
    main()