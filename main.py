import sys

import matplotlib.pyplot as plt
import numpy as np
from measurement import Measurement
''''
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
'''
yield_values = []
strain_yield = []
tensile_values = []
strain_tensile = []
fracture_values = []
strain_fracture = []

#exp 1
# 160, 215, 190
# 0.02, 0.08, 0.16
#exp 2
# 180, 220, 193
# 0.02, 0.08, 0.18
#exp. 3
# 155, 218, 195
# 0.03, 0.07, 0.15

def neg_checked(table):
    for element in table:
        if float(element) < 0:
            print("Only provide positive values")
            return 1
        else:
            return 0

for i in range (3):
    stress_values = input("Please indicate yield, tensile and fracture stress values (in MPa) for experiment {x}, respectively ".format(x=i+1))

    stress_values_table = stress_values.split(',')
    if neg_checked(stress_values_table) == 1:
        sys.exit()
    yield_values.append(int(stress_values_table[0]))
    tensile_values.append(int(stress_values_table[1]))
    fracture_values.append(int(stress_values_table[2]))

    strain_values = input("Please indicate yield, tensile and fracture strain values (in mm) for experiment {x}, respectively ".format(x=i+1))

    strain_values_table = strain_values.split(',')
    if neg_checked(strain_values_table) == 1:
        sys.exit()
    strain_yield.append(float(strain_values_table[0]))
    strain_tensile.append(float(strain_values_table[1]))
    strain_fracture.append(float(strain_values_table[2]))

print(yield_values)
print(tensile_values)
print(fracture_values)
print(strain_yield)
print(strain_tensile)
print(strain_fracture)

def insert_sort(arr): #taken from pp7 homework
    n = len(arr)
    for i in range(n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

sorted_yield_values = insert_sort(yield_values)
sorted_tensile_values = insert_sort(tensile_values)
sorted_fracture_values = insert_sort(fracture_values)
sorted_strain_yield = insert_sort(strain_yield)
sorted_strain_tensile = insert_sort(strain_tensile)
sorted_strain_fracture = insert_sort(strain_fracture)

print(sorted_yield_values)
print(sorted_tensile_values)
print(sorted_fracture_values)
print(sorted_strain_yield)
print(sorted_strain_tensile)
print(sorted_strain_fracture)

yield_point = (sorted_yield_values[1], sorted_strain_yield[1])
tensile_point = (sorted_tensile_values[1], sorted_strain_tensile[1])
fracture_point = (sorted_fracture_values[1], sorted_strain_fracture[1])

print(yield_point)
print(tensile_point)
print(fracture_point)

measurement = Measurement(yield_point, tensile_point, fracture_point)
measurement.stress_strain_plot()
# plot_yield_value = sorted_yield_values[1]
# plot_tensile_value = sorted_tensile_values[1]
# plot_fracture_value = sorted_fracture_values[1]
# plot_strain_yield_value = sorted_strain_yield[1]
# plot_strain_tensile_value = sorted_strain_tensile[1]
# plot_strain_fracture_value = sorted_strain_fracture[1]



# yield1 = int(input("Please indicate the yield stress value"))
# strain_yield1 = float(input("Please indicate the yield stress strain value"))
#
# tensile = int(input("Please indicate the tensile stress value"))
# strain_tensile = float(input("Please indicate the tensile stress strain value"))
#
# fracture = int(input("Please indicate the fracture stress value"))
# strain_fracture = float(input("Please indicate the fracture stress strain value"))



# yield1 = 160
# strain_yield1 = 0.02
#
# tensile = 215
# strain_tensile = 0.08
#
# fracture = 190
# strain_fracture = 0.16
#
# print(yield1)
#
# M1 = measurement.Measurement((yield1, strain_yield1), (tensile, strain_tensile) , (fracture, strain_fracture))
# D = [(0, 0), (yield1, strain_yield1), (tensile, strain_tensile) , (fracture, strain_fracture)]
# stress = np.array([d[0] for d in D])
# strain = np.array([d[1] for d in D])
#
# plt.plot(strain, stress)
# plt.xlabel('strain, mm')
# plt.ylabel("stress, MPa")
# plt.title("Stress-strain curve")
# plt.grid(True)
# plt.show()
