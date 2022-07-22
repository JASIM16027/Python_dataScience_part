import numpy as np
import matplotlib.pyplot as plt

input_array = np.linspace(-np.pi, np.pi, 12)

output_array = np.sin(input_array)
output_array_inverse_sin = np.arcsin(input_array)

print(output_array)

plt.figure(1)
plt.plot(input_array, output_array, color='red', marker='o')
plt.plot(input_array, output_array_inverse_sin, color='red', marker='o')

plt.xlabel('x')
plt.ylabel("f(x) = sin(x)")
plt.show()
plt.figure(2)
plt.plot(input_array, np.tan(input_array), color='red', marker='x')
plt.show()

