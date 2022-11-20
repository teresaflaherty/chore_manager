from datetime import datetime, date, timedelta
from time import sleep

from database_functions import setup_database, read_query, execute_query, create_db_connection


def run_server():
    # The two times of day to surface the chores
    morning = datetime.strptime("08:00:00", '%H:%M:%S').time()
    evening = datetime.strptime("18:00:00", '%H:%M:%S').time()

    while True:
        surface_expired_chores("Morning")
        decrement_chore_counter()
        sleep(10)

        # current_time = datetime.now().time().replace(microsecond=0)
        # sleep(calculate_sleep_time(morning, evening, current_time))
        # if current_time == morning:
        #     decrement_chore_counter()
        #     surface_expired_chores("Morning")
        # elif current_time == evening:
        #     surface_expired_chores("Evening")
        #
        # sleep(calculate_sleep_time(morning, evening, current_time))


def decrement_chore_counter():
    decrement_query = "UPDATE chores SET time_remaining = time_remaining - 1 WHERE time_remaining != 0;"
    execute_query(db_connection, decrement_query)


def surface_expired_chores(time_of_day):
    get_chores_query = f"SELECT * FROM chores WHERE reminder_time = '{time_of_day}' AND time_remaining = 0;"
    relevant_chores = read_query(db_connection, get_chores_query)

    with open("chores_to_do.txt", 'w') as chore_file:
        for chore in relevant_chores:
            chore_file.write(f"{chore['name']}\n")


def calculate_sleep_time(morning, evening, current_time):
    # current_time = datetime.strptime("07:59:55", '%H:%M:%S').time()

    if current_time < morning:
        # If it's too early, sleep until 8AM
        sleep_time = datetime.combine(date.today(), morning) - datetime.combine(date.today(), current_time)
        print(f"sleeping until breakfast! {sleep_time.total_seconds()} seconds to go")
    elif current_time < evening:
        # If the morning has already passed, sleep until 6PM
        sleep_time = datetime.combine(date.today(), evening) - datetime.combine(date.today(), current_time)
        print(f"sleeping until dinner! {sleep_time.total_seconds()} seconds to go")
    else:
        # If the evening has already passed, sleep until 8AM tomorrow
        sleep_time = datetime.combine(date.today(), morning) + timedelta(days=1) - datetime.combine(date.today(),
                                                                                                    current_time)
        print(f"sleeping until tomorrow! {sleep_time.total_seconds()} seconds to go")
    return sleep_time.total_seconds()


if __name__ == "__main__":
    setup_database()
    db_connection = create_db_connection()
    run_server()
