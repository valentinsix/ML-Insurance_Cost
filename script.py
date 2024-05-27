#-------------------------------------------------SETUP-------------------------------------------------------------

#Imports 

import sklearn
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

#Defining a space to save the figures 

PROJECT_ROOT_DIR = "."
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images")
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

#-------------------------------------------------GET THE DATA--------------------------------------------------------------

HOUSING_PATH = os.path.join("datasets", "insurance.csv")

def load_insurance_data(housing_path=HOUSING_PATH):
    csv_path = housing_path
    return pd.read_csv(csv_path)

insurance = load_insurance_data()
print(insurance.head())
