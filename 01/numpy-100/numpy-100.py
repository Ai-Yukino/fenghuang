# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # `Numpy-100.ipynb`
#
# [🍅 Resource link](https://github.com/rougier/numpy-100)

# ## Exericse 1: Import the numpy package under the name `np` (★☆☆)

# + jupyter={"source_hidden": true} tags=[]
# Solution to exercise 1
# ---
import numpy as np
# -

# ## Exercise 2: Print the numpy version and the configuration (★☆☆)

# + jupyter={"source_hidden": true} tags=[]
# Solution to exercise 2
# ---

print("NumPy version: " + np.version.version + "\n---")
print("NumPy config:")
np.show_config()
# -

# # Exercise 3: Create a null vector of size 10 (★☆☆)

# + jupyter={"outputs_hidden": true} tags=[]
# Solution to exercise 3
# ---

np.zeros(10)
# -

# ## Exercise 4: How to find the memory size of any array (★☆☆)

# [Memory management in NumPy | NumPy docs](https://numpy.org/doc/stable/reference/c-api/data_memory.html)

# ## Solution to exercise 4
#
# Call the `nbytes` method on that ndarray, e.g.

a = np.array([-1, 0, 1])
a.nbytes
