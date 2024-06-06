import pandas as pd

def process_data(data_file):
    # Read data
    df = pd.read_csv(data_file)
    
    # Drop missing values
    df = df.dropna()
    
    # Perform certain operations
    # For example, calculate the sum of a column
    total = df['column'].sum()
    
    return total

import pandas as pd

def test_process_data():
    # Create a sample DataFrame
    data = {'column': [1, 2, 3, None, 5]}
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv('test_data.csv', index=False)
    
    # Call the process_data function
    result = process_data('test_data.csv')
    
    # Check the result
    assert result == 11  # Sum of non-missing values in the 'column' column