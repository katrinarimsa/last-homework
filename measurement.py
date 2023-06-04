import matplotlib.pyplot as plt
import numpy as np

class Measurement:
    def __init__(self, yield_point, tensile_point, fracture_point):
        self.yield_point = yield_point
        self.tensile_point = tensile_point
        self.fracture_point = fracture_point

    def stress_strain_plot(self):
            yield1, strain_yield1 = self.yield_point
            tensile, strain_tensile = self.tensile_point
            fracture, strain_fracture = self.fracture_point

            stress = np.array([0, yield1, tensile, fracture])
            strain = np.array([0, strain_yield1, strain_tensile, strain_fracture])

            plt.plot(strain, stress)
            plt.xlabel("Strain, mm")
            plt.ylabel("Stress, MPa")
            plt.title("Stress-strain curve")
            plt.grid(True)
            plt.show()
