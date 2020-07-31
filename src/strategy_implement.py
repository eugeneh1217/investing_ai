from csv_parse import SECTOR_DICT
from comp_pe import compare_pe


def strategy_0(date, constant, growth_average_start_date, growth_average_end_date):
    """implement strategy_0 to return a two lists of tuples"""

    # calls compare_pe() on the entire parsed list: SECTOR_DICT
    # instantiate needed stuff
    dictionary_length = len(SECTOR_DICT)
    sector_list_holder = []
    compare_pe_holder = []
    top_five = []
    last_five = []
    current = 0
    counter = 0

    # run through the dictionary of lists
    for key in SECTOR_DICT.keys():
        """first part to find a list of the 5 best and 5 worst compare_pe() values"""
        sector_list_holder = SECTOR_DICT[key]

        # append all compare_pe() values onto a compare_pe_holder
        for i in sector_list_holder:
            compare_pe_holder.append(sector_list_holder[i][0],
                                     sector_list_holder[i].compare_pe())

        # find the top 5 compare_pe() values
        while current < (len(compare_pe_holder)):
            for j in range(len(top_five)):
                if compare_pe_holder[current][1] > top_five[j]:
                    counter += 1

            if counter >= 1:
                top_five.append(compare_pe_holder[current])

            # remove the lowest value if tuple added, should be able to be simplified but the nested lists make hard
            # look into min() function
            if len(top_five) == 6:
                top_five = removelowest(top_five, 1)

            counter = 0
            current += 1

        # find the lowest 5 compare_pe() values
        while current < (len(compare_pe_holder)):
            for j in range(len(last_five)):
                if compare_pe_holder[current][1] < last_five[j]:
                    counter += 1

            if counter >= 1:
                last_five.append(compare_pe_holder[current])

            if len(last_five) == 6:
                last_five = removehighest(last_five, 1)

            counter = 0
            current += 1

        """implement the strategy_0 formula to yield a list of [(ticker symbol), (# of stocks)]"""

    return top_five, last_five


def removelowest(extended_list, value_column):
    """removes the lowest value of a nested list"""

    LOW = []

    for k in range(len(extended_list)):
        if extended_list[k][value_column] < LOW:
            LOW = extended_list[k]

    extended_list.remove(LOW)
    return extended_list


def removehighest(extended_list, value_column):
    """removes the highest value of a nested list"""

    MAX = []

    for k in range(len(extended_list)):
        if extended_list[k][value_column] > MAX:
            MAX = extended_list[k]

    extended_list.remove(MAX)
    return extended_list


def multiply(x, y):
    """
        set a multiplication function
    """
    return x * y


def divide(x, y):
    """
        set a division function
    """
    return x / y
