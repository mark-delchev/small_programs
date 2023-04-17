import pandas as pd
from sklearn.model_selection import train_test_split

# Load data into a pandas DataFrame
data = pd.read_csv("your_data.csv")

# Shuffle the data
data = data.sample(frac=1).reset_index(drop=True)

# Specify split ratio
train_size = 0.8

# Split data into training and validation sets
train_data, val_data = train_test_split(data, train_size=train_size)
