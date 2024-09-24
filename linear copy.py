import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the dataset (replace with your actual data source)
# For example, you might be using the seaborn 'mpg' dataset:
mpg = sns.load_dataset('mpg').dropna()  # Load the dataset and drop any missing values

# Create the regression plot
plt.figure(figsize=(10, 6))
sns.regplot(data=mpg, x="horsepower", y="weight", robust=True)

# Set plot labels and title
plt.xlabel('Horsepower')
plt.ylabel('Weight')
plt.title('Regression Plot of Horsepower vs Weight')

# Show the plot
plt.show()
