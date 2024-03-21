# pip install mysql-connector-python
import mysql.connector
import pandas as pd

# Configure connection parameters
host = "kk"
port = 3306
database = "ahmad_schema"
username = "username"
password = "password"

try:
    # Establish connection
    connection = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=username,
        password=password
    )

    # Create a cursor
    cursor = connection.cursor()

    # Execute a SELECT query
    query = "SELECT FullName,City FROM Persons"
    cursor.execute(query)
    df_list=[]
    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)
        df_list.append(row)



    df =pd.DataFrame(df_list,columns=['fullName',"City"])
    # Close the cursor and connection
    cursor.close()
    connection.close()

except mysql.connector.Error as e:
    print("Error:", e)
print(df)
