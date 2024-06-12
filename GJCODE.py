import pandas as pd

# Create a DataFrame with sample data
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35]
}

df = pd.DataFrame(data)

# Calculate the sum of the 'age' column
total_age = df['age'].sum()

# Print the result
print(f"The total age is: {total_age}")
