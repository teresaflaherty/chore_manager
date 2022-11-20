import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Server connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection():
    host_name = "localhost"
    user_name = "root"
    user_password = "choreslist"
    db_name = "chores"
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
        exit()

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
        exit()


def read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        row_headers = [x[0] for x in cursor.description]
        results = cursor.fetchall()
        results_list = []
        for result in results:
            result_dict = {}
            for i in range(len(result)):
                result_dict[row_headers[i]] = result[i]
            results_list.append(result_dict)
        return results_list
    except Error as err:
        print(f"Error: '{err}'")
        exit()


def setup_database():
    connection = create_server_connection("localhost", "root", "choreslist")

    create_database_query = "CREATE DATABASE IF NOT EXISTS chores"
    create_database(connection, create_database_query)

    create_chores_table = """
    CREATE TABLE IF NOT EXISTS chores (
      id INT PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      frequency INT NOT NULL,
      reminder_time VARCHAR(20) NOT NULL,
      time_remaining INT NOT NULL
      );
     """

    connection = create_db_connection()  # Connect to the Database
    execute_query(connection, create_chores_table)  # Execute our defined query

    pop_teacher = """
    INSERT INTO chores VALUES
    (1, 'Do the Dishes', 1, 'Evening', 0),
    (2, 'Unload the Dishwasher', 1, 'Morning', 0),
    (3, 'Make the Bed', 1, 'Morning', 1),
    (4, 'Send Alan around the Kitchen', 2, 'Evening', 2),
    (5, 'Send Alan around', 7, 'Evening', 0),
    (6, 'Check the Post', 1, 'Morning', 1),
    (7, 'Clear off Tables', 1, 'Evening', 1),
    (8, "Sweep where Alan Can't Reach", 7, 'Morning', 4),
    (9, 'Mop with Floor Cleaner', 30, 'Morning', 1),
    (10, 'Dust All Surfaces', 7, 'Morning', 3),
    (11, 'Clean the Toilets', 7, 'Morning', 1),
    (12, 'Clean the Sinks', 7, 'Morning', 7),
    (13, 'Clean the Tub and Shower', 14, 'Morning', 12),
    (14, 'Clean the Mirrors and Windows', 30, 'Morning', 16),
    (15, 'Change the Sheets', 10, 'Morning', 7),
    (16, 'Towel Wash', 14, 'Morning', 13),
    (17, 'Grocery Shopping', 3, 'Evening', 2),
    (18, 'Take Out the Bins (if full)', 1, 'Evening', 1),
    (19, 'Clean the Fridge', 60, 'Morning', 55),
    (20, 'Clean the Oven and Microwave', 60, 'Morning', 44),
    (21, "Change Alan's Bag", 60, 'Morning', 33),
    (22, "Change Alan's Filter", 90, 'Morning', 66),
    (23, 'Hoover the Curtains', 30, 'Morning', 13),
    (24, 'Hoover the Furniture', 30, 'Morning', 29),
    (25, 'Clean the Walls', 90, 'Morning', 75),
    (26, 'Dust the Skirting Boards', 30, 'Morning', 20),
    (27, 'Organize the Drawers/Presses', 30, 'Morning', 10),
    (28, 'Organize the Wardrobes', 30, 'Morning', 16),
    (29, 'Wipe the Kitchen Counters', 1, 'Evening', 1),
    (30, 'Tidy the Couches', 1, 'Evening', 1),
    (31, 'Feed Remy', 1, 'Morning', 1),
    (32, 'Bathe Remy', 5, 'Morning', 3);
    """

    execute_query(connection, pop_teacher)
