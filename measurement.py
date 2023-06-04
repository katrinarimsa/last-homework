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
#
# yield_point = 160, 0.02
#
# tensile_point = 215, 0.08
#
# fracture_point = 190, 0.16
#
# try_if_method_works = Measurement(yield_point, tensile_point, fracture_point)
# try_if_method_works.stress_strain_plot()