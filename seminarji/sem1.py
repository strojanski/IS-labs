import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def f1(x):
    return -np.abs(x) + np.cos(x)

bounds = np.array([-20, 20])
model = ga(function=f1, dimension=2, variable_type="real", variable_boundaries=bounds)
model.run()
