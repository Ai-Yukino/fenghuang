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

# # `pd-merge-101`
#
# <div align="center">
#     <img src="images/pd-merge-101.png" style="width: 65%; border-radius: 10px">
# </div>
#
# 🖼 Image source: screenshot of resource below on April 14, 2022
#
# ---
#
# [📝 StackOverflow answer](https://stackoverflow.com/questions/53645882/pandas-merging-101)
#

# ## 🐍 Python imports 🐍

import pandas as pd
import numpy as np

# ## 🗃 Get data 🗃

# +
## Create dictionaries
np.random.seed(0)
dict_left = {"key": ["A", "B", "C", "D"], "value": np.random.randn(4)}
dict_right = {"key": ["B", "D", "E", "F"], "value": np.random.randn(4)}

## Create df's
df_left = pd.DataFrame(dict_left)
df_right = pd.DataFrame(dict_right)
# -

df_left

df_right

# ## ❄ INNER JOIN ❄

df_left.merge(df_right, on="key", how="inner")
