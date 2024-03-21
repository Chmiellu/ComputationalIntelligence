from tqdm.notebook import tqdm
import matplotlib.pyplot as plt
import random
import numpy as np

class Task:
    def __init__(self, size):
        self.size = size
        self.Weight_limit = np.random.randint(10 * self.size, 20 * self.size)
        self.Size_limit = np.random.randint(10 * self.size, 20 * self.size)
        while True:
            self.weights = np.random.random(self.size) * 10 * self.Weight_limit / self.size
            self.sizes = np.random.random(self.size) * 10 * self.Size_limit / self.size
            self.costs = np.random.random(self.size) * self.size
            if self.weights.sum() > 2 * self.Weight_limit and self.sizes.sum() > 2 * self.Size_limit:
                break
generated_task = Task(size=3)
print(generated_task.__dict__)
# >> {
#     'size': 3,
#     'Weight_limit': 30,
#     'Size_limit': 33,
#     'weights': array([ 16.17, 32.24, 43.58]),
#     'sizes': array([ 87.66, 94.98, 81.57]),
#     'costs': array([ 2.43, 1.66, 0.02])
#     }