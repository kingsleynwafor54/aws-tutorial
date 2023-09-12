# aws-tutorial


def creating_a_simple_csv_file():
    # Sample data
    data = {'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'San Francisco', 'Los Angeles']}
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Specify the file path where you want to save the CSV file
    csv_file_path = 'sample_data.csv'

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"CSV file '{csv_file_path}' created successfully.")
creating_a_simple_csv_file()
