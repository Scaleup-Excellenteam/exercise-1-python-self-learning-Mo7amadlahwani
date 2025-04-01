"""
This script selects a random date between two given dates and checks if it falls on a Monday.
If the randomly chosen date is not a Monday, it prints: "Ain't gettin' no vinaigrette today :(".
"""
import datetime
import random


def no_vinnigrete(date_entry1, date_entry2):
    """
       Selects a random date between two given dates and checks if it falls on a Monday.
       If the randomly chosen date is not a Monday, it prints: "Ain't gettin' no vinaigrette today :(".

       Args:
       date_entry1 (str): The first date as a string in the format "YYYY-MM-DD".
       date_entry2 (str): The second date as a string in the format "YYYY-MM-DD".

       Returns:
       None: This function does not return any value. It prints a message if the random date is not a Monday.

       If the provided date strings are invalid, the function will print "invalid date!!".
    """
    try:
        date1 = datetime.datetime.strptime(date_entry1.strip(), "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date_entry2.strip(), "%Y-%m-%d")
        epoch_time1 = int(date1.timestamp())
        epoch_time2 = int(date2.timestamp())
        if epoch_time1 > epoch_time2:
            random_date = random.randint(epoch_time2, epoch_time1)
        else:
            random_date = random.randint(epoch_time1, epoch_time2)
        final_date = datetime.datetime.fromtimestamp(random_date).date()
        if final_date.weekday() != 0:
            print("Ain't gettin' no vinaigrette today :(")
    except ValueError:
        print("invalid date!!")


if __name__ == "__main__":
    no_vinnigrete("2023-07-10", "2023-07-10")
