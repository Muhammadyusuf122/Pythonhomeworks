# Load the JSON file
import pandas as pd
iris_df = pd.read_json('iris.json')

# Show shape and column names
print("Shape:", iris_df.shape)
print("Columns:", iris_df.columns.tolist())
