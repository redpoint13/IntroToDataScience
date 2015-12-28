import numpy as np
import pandas as pd
from scipy import linalg as LA

A = pd.read_csv('turnstile_data_master_with_weather.csv')


#A = np.random.randint(0, 10, 25).reshape(5, 5)
#print A
e_vals, e_vecs = LA.eig(A)
print e_vals