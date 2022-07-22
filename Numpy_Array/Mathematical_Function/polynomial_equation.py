import numpy as np
import matplotlib.pyplot as plt

input_x = np.arange(1, 15)
output_x_square = np.array(input_x * input_x)
output_x_cube = np.array(output_x_square*input_x)
output_x_power_four = np.array(output_x_cube*input_x)
output_x_power_five = np.array(output_x_power_four*input_x)



print("input_x = {}\n output = {} \n cube of x = {}".format(input_x, output_x_square,
                                                               output_x_cube))

plt.figure(1)
plt.plot(input_x, output_x_square, color='red', marker='o')
plt.xlabel('x')
plt.ylabel('f(x)= x*x')
plt.show()

plt.figure(2)
plt.plot(input_x, output_x_cube, color='red', marker='o')
plt.xlabel('x')
plt.ylabel('f(x)= x*x*x')
plt.show()


plt.plot(input_x, output_x_power_four, color='red', marker='o')
plt.xlabel('x')
plt.ylabel('f(x)= x*x*x*x')
plt.show()

plt.plot(input_x, output_x_power_four, color='red', marker='o')
plt.xlabel('x')
plt.ylabel('f(x)= x*5')
plt.show()