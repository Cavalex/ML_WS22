import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from arff_to_csv import *
from config import *

def plot(dataset_name, df):

    #df = pd.read_csv(fileName,  sep=',', on_bad_lines="skip") # reads the csv file and creates a dataframe based on it

    if dataset_name == "voting":
        plt.close(fig="all")
        sns.set_style("whitegrid")
        #sns.pairplot(df, hue="class", height=3)
        sns.histplot(df["class"], kde=True)
        plt.show()
        fileToSave = f".{IMAGE_FOLDER}/{dataset_name}_classes.png"
        plt.savefig(fileToSave)

        """ sns.set_style(“whitegrid”);
        sns.FacetGrid(df, hue=’species’, size=5).map(plt.scatter, “sepal_length”, “sepal_width”).add_legend();
        plt.show()
        """
    else:
        print("Not yet implemented ploting for", dataset_name)
