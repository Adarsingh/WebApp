#app.py file
#

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")

# def home():
#     return "Hello Flask app.py"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)




# from flask import Flask, render_template, request, redirect
# import smtplib

# app = Flask(__name__)

# @app.route('/')
# def home():
#     # return "Hello Flask app.py"
#     return render_template('index.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)



#===================================================================================================
# Perfect Code for task 1 


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


#===================================================================================================




#===================================================================================================


#Working fine for all task. No databse access. No tables for task 2 & 3.




# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/task2')
# def task2():
#     return render_template('task2.html')

# @app.route('/task3')
# def task3():
#     return render_template('task3.html')

# if __name__ == '__main__':
#     app.run(debug=True)





#===================================================================================================


#===================================================================================================


#Working fine for all task. No databse access. Tables for task 2 & 3.

# from flask import Flask, render_template
# import json
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/task2')
# def task2():
#     # Path to the JSON file
#     json_file_path = os.path.join(app.root_path, 'static', 'data', 'query_1_result.json')
    
#     # Read the JSON file
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)
    
#     # Define the dynamic sentence
#     sqlquery1 = "Result for SQL query for task2"
    
#     return render_template('task2.html', data=data, sqlquery1=sqlquery1)

# @app.route('/task3')
# def task3():
#     # Path to the JSON file
#     json_file_path = os.path.join(app.root_path, 'static', 'data', 'query_2_result.json')
    
#     # Read the JSON file
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)
    
#     # Define the dynamic sentence
#     sqlquery1 = "Result for SQL query for task3"
    
#     return render_template('task3.html', data=data, sqlquery1=sqlquery1)
    


# if __name__ == '__main__':
#     app.run(debug=True)



#===================================================================================================



# from flask import Flask, render_template
# import pyodbc
# import json
# import os
# from decimal import Decimal

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'driver': '{ODBC Driver 17 for SQL Server}',
#     'server': 'bootcampaug5server.database.windows.net',
#     'database': 'bootcampaug5db',
#     'uid': 'bootcamp',
#     'pwd': 'Pass@123'
# }

# class DecimalEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Decimal):
#             return float(obj)  # Or str(obj) if you prefer string representation
#         return super(DecimalEncoder, self).default(obj)

# def query_database(query):
#     conn_str = f"DRIVER={db_config['driver']};SERVER={db_config['server']};DATABASE={db_config['database']};UID={db_config['uid']};PWD={db_config['pwd']}"
#     with pyodbc.connect(conn_str) as conn:
#         cursor = conn.cursor()
#         cursor.execute(query)
#         columns = [column[0] for column in cursor.description]
#         rows = cursor.fetchall()
#         results = []
#         for row in rows:
#             row_dict = {}
#             for col_name, value in zip(columns, row):
#                 if isinstance(value, Decimal):
#                     row_dict[col_name] = float(value)  # Convert Decimal to float
#                 else:
#                     row_dict[col_name] = value
#             results.append(row_dict)
#     return results

# def write_to_json(file_path, data):
#     with open(file_path, 'w') as file:
#         json.dump(data, file, cls=DecimalEncoder, indent=4)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/task2')
# def task2():
#     query = "SELECT TOP (20) * FROM [SalesLT].[Customer]"
#     data = query_database(query)
#     json_file_path = os.path.join(app.root_path, 'static', 'data', 'query_1_result.json')
#     write_to_json(json_file_path, data)
#     sqlquery1 = "Result for SQL query for task2"
#     return render_template('task2.html', data=data, sqlquery1=sqlquery1)

# @app.route('/task3')
# def task3():
#     query = "SELECT Name AS 'Product Name', Color, Size, Weight FROM [SalesLT].[Product]"
#     data = query_database(query)
#     json_file_path = os.path.join(app.root_path, 'static', 'data', 'query_2_result.json')
#     write_to_json(json_file_path, data)
#     sqlquery1 = "Result for SQL query for task3"
#     return render_template('task3.html', data=data, sqlquery1=sqlquery1)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
import pyodbc
import json
import os
from decimal import Decimal
from datetime import datetime

app = Flask(__name__)

# Database configuration
db_config = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': 'bootcampaug5server.database.windows.net',
    'database': 'bootcampaug5db',
    'uid': 'bootcamp',
    'pwd': 'Pass@123'
}

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  
        elif isinstance(obj, datetime):
            return obj.isoformat()  
        return super(CustomJSONEncoder, self).default(obj)

def query_database(query):
    conn_str = f"DRIVER={db_config['driver']};SERVER={db_config['server']};DATABASE={db_config['database']};UID={db_config['uid']};PWD={db_config['pwd']}"
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        results = []
        for row in rows:
            row_dict = {}
            for col_name, value in zip(columns, row):
                if isinstance(value, Decimal):
                    row_dict[col_name] = float(value)  
                elif isinstance(value, datetime):
                    row_dict[col_name] = value.isoformat()
                else:
                    row_dict[col_name] = value
            results.append(row_dict)
    return results

def write_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, cls=CustomJSONEncoder, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task2')
def task2():
    query = "SELECT TOP (20) * FROM [SalesLT].[Customer]"
    data = query_database(query)
    json_file_path = os.path.join(app.root_path, 'static', 'data', 'query_1_result.json')
    write_to_json(json_file_path, data)
    sqlquery1 = "Result for SQL query for task2"
    return render_template('task2.html', data=data, sqlquery1=sqlquery1)

@app.route('/task3')
def task3():
    query = "SELECT Name AS 'Product Name', Color, Size, Weight FROM [SalesLT].[Product]"
    data = query_database(query)
    json_file_path = os.path.join(app.root_path, 'static', 'data', 'query_2_result.json')
    write_to_json(json_file_path, data)
    sqlquery1 = "Result for SQL query for task3"
    return render_template('task3.html', data=data, sqlquery1=sqlquery1)

if __name__ == '__main__':
    app.run(debug=True)





#===================================================================================================

#Failed attempt for db connection

# from flask import Flask, render_template
# import pyodbc

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'user': 'bootcamp',
#     'password': 'Pass@123',
#     'server': 'bootcampaug5server.database.windows.net',
#     'database': 'bootcampaug5db',
# }

# def get_db_connection():
#     conn_str = (
#         f"DRIVER={{ODBC Driver 17 for SQL Server}};"
#         f"SERVER={db_config['server']};"
#         f"DATABASE={db_config['database']};"
#         f"UID={db_config['user']};"
#         f"PWD={db_config['password']}"
#     )
#     conn = pyodbc.connect(conn_str)
#     return conn

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/task2')
# def task2():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     query = "SELECT TOP 20 * FROM [SalesLT].[Customer]"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     columns = [column[0] for column in cursor.description]
#     conn.close()
#     return render_template('task2.html', rows=rows, columns=columns)

# @app.route('/task3')
# def task3():
#     return render_template('task3.html')

# if __name__ == '__main__':
#     app.run(debug=True)

