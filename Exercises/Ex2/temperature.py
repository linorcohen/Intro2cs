#################################################################
# FILE : temperature.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that checks if at least two of three days
# has a higher temperature then the threshold temperature.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################


def is_it_summer_yet(temp_threshold, temp_day_1, temp_day_2, temp_day_3):
    """
    This function checks if two (or more) out of three days has temperature
    higher then the threshold temperature.
    :param temp_threshold: threshold temperature
    :type temp_threshold: int or float
    :param temp_day_1: temperature day 1
    :type temp_day_1: int or float
    :param temp_day_2: temperature day 2
    :type temp_day_2: int or float
    :param temp_day_3: temperature day 3
    :type temp_day_3: int or float
    :return: True, if two or more days had temperature higher
    then the threshold temperature. else, False.
    :rtype: bool
    """
    days_higher_than_threshold = 0
    # the code below checks each day if higher then the threshold,
    # and counts them
    if temp_day_1 > temp_threshold:
        days_higher_than_threshold += 1
    if temp_day_2 > temp_threshold:
        days_higher_than_threshold += 1
    if temp_day_3 > temp_threshold:
        days_higher_than_threshold += 1

    if days_higher_than_threshold >= 2:
        return True
    return False
