# import statements
import pandas as pd
from statsmodels.api import datasets
import numpy as np

# 1) load the dataset
# and store as mtcars
mtcars = datasets.get_rdataset("mtcars").data

# 2) convert miles per gallon
# to kilometers per liter
# using 1 MPG = 0.43 Kilometers per liter
mtcars["v_kml"] = mtcars["mpg"] * 0.43

# 3) Create c_am (character) from am that is a binary
# variable
mtcars["c_am"] = np.where(
    # Condition:
    mtcars["am"] == 1,
    # TRUE mapping
    "Automatic",
    # FALSE mapping
    "Manual"
)

# 4) add c_cyl that
# that has descriptive
# variables instead of numerics
mtcars["c_cyl"] = mtcars["cyl"].astype(str) + " cylinders"



