from csv import reader

# Lists to hold complete CSV Files
# BASIC_MATERIALS_SECTOR_NON_PARSED = []
# COMMUNICATION_SERVICES_SECTOR_NON_PARSED = []
# CONSUMER_CYCLICAL_SECTOR_NON_PARSED = []
# CONSUMER_DEFENSIVE_SECTOR_NON_PARSED = []
# ENERGY_SECTOR_NON_PARSED = []
# FINANCIAL_SERVICES_SECTOR_NON_PARSED = []
# HEALTHCARE_SECTOR_NON_PARSED = []
# INDUSTRIALS_SECTOR_NON_PARSED = []
# TECHNOLOGY_SECTOR_NON_PARSED = []
# UTILITIES_SECTOR_NON_PARSED = []

# Lists to hold parsed CSV Files
# BASIC_MATERIALS_SECTOR = []
# COMMUNICATION_SERVICES_SECTOR = []
# CONSUMER_CYCLICAL_SECTOR = []
# CONSUMER_DEFENSIVE_SECTOR = []
# ENERGY_SECTOR = []
# FINANCIAL_SERVICES_SECTOR = []
# HEALTHCARE_SECTOR = []
# INDUSTRIALS_SECTOR = []
# TECHNOLOGY_SECTOR = []
# UTILITIES_SECTOR = []

# Dictionary
SECTOR_DICT = {}

# read csv file as a list of lists
def source():
    """
        source all the csv files from assets folder
    """
    with open('BasicMaterialsList.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        global BASIC_MATERIALS_SECTOR_NON_PARSED
        BASIC_MATERIALS_SECTOR_NON_PARSED = list_of_rows

    with open('CommunicationServicesList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global COMMUNICATION_SERVICES_SECTOR_NON_PARSED
        COMMUNICATION_SERVICES_SECTOR_NON_PARSED = list_of_rows

    with open('ConsumerCyclicalList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global CONSUMER_CYCLICAL_SECTOR_NON_PARSED
        CONSUMER_CYCLICAL_SECTOR_NON_PARSED = list_of_rows

    with open('ConsumerDefensiveList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global CONSUMER_DEFENSIVE_SECTOR_NON_PARSED
        CONSUMER_DEFENSIVE_SECTOR_NON_PARSED = list_of_rows

    with open('EnergyList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global ENERGY_SECTOR_NON_PARSED
        ENERGY_SECTOR_NON_PARSED = list_of_rows

    with open('FinancialServicesList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global FINANCIAL_SERVICES_SECTOR_NON_PARSED
        FINANCIAL_SERVICES_SECTOR_NON_PARSED = list_of_rows

    with open('HealthcareList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global HEALTHCARE_SECTOR_NON_PARSED
        HEALTHCARE_SECTOR_NON_PARSED = list_of_rows

    with open('IndustrialsList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global INDUSTRIALS_SECTOR_NON_PARSED
        INDUSTRIALS_SECTOR_NON_PARSED = list_of_rows

    with open('TechnologyList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global TECHNOLOGY_SECTOR_NON_PARSED
        TECHNOLOGY_SECTOR_NON_PARSED = list_of_rows

    with open('UtilitiesList.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        list_of_rows = list(csv_reader)
        global UTILITIES_SECTOR_NON_PARSED
        UTILITIES_SECTOR_NON_PARSED = list_of_rows

def parser_zip(csv_source, first_column, second_column):
    """
        parse a single column in the given csv_source
    """
    first_list = []
    second_list = []
    total_list = []

    length = len(csv_source)

    for i in range(length-1):
        first_list.append(csv_source[i+1][first_column])
    for i in range(length-1):
        second_list.append(csv_source[i+1][second_column])

    total_list = list(zip(first_list, second_list))

    return total_list

def parse_all_sectors():
    """
        parse all sectors
    """
    global BASIC_MATERIALS_SECTOR
    global COMMUNICATION_SERVICES_SECTOR
    global CONSUMER_CYCLICAL_SECTOR
    global CONSUMER_DEFENSIVE_SECTOR
    global ENERGY_SECTOR
    global FINANCIAL_SERVICES_SECTOR
    global HEALTHCARE_SECTOR
    global INDUSTRIALS_SECTOR
    global TECHNOLOGY_SECTOR
    global UTILITIES_SECTOR

    BASIC_MATERIALS_SECTOR = parser_zip(BASIC_MATERIALS_SECTOR_NON_PARSED,1,2)
    COMMUNICATION_SERVICES_SECTOR = parser_zip(COMMUNICATION_SERVICES_SECTOR_NON_PARSED,1,2)
    CONSUMER_CYCLICAL_SECTOR = parser_zip(CONSUMER_CYCLICAL_SECTOR_NON_PARSED,1,2)
    CONSUMER_DEFENSIVE_SECTOR = parser_zip(CONSUMER_DEFENSIVE_SECTOR_NON_PARSED,1,2)
    ENERGY_SECTOR = parser_zip(ENERGY_SECTOR_NON_PARSED,1,2)
    FINANCIAL_SERVICES_SECTOR = parser_zip(FINANCIAL_SERVICES_SECTOR_NON_PARSED,1,2)
    HEALTHCARE_SECTOR = parser_zip(HEALTHCARE_SECTOR_NON_PARSED,1,2)
    INDUSTRIALS_SECTOR = parser_zip(INDUSTRIALS_SECTOR_NON_PARSED,1,2)
    TECHNOLOGY_SECTOR = parser_zip(TECHNOLOGY_SECTOR_NON_PARSED,1,2)
    UTILITIES_SECTOR = parser_zip(UTILITIES_SECTOR_NON_PARSED,1,2)

def dictionaryC(sector_A, sector_B, sector_C, sector_D, sector_E, sector_F, sector_G, sector_H, sector_I, sector_J):
    """
        Create the dictionary, separate method itsself means globalizing the variable
    """
    DICT = {
        "Basic_Materials_Sector":sector_A,
        "Communication_Services_Sector":sector_B,
        "Consumer_Cyclical_Sector":sector_C,
        "Consumer_Defensive_Sector":sector_D,
        "Energy_Sector":sector_E,
        "Financial_Services_Sector":sector_F,
        "Healthcare_Sector":sector_G,
        "Industrials_Sector":sector_H,
        "Technology_Sector":sector_I,
        "Utilities_Sector":sector_J
    }
    return DICT


source()
parse_all_sectors()
SECTOR_DICT = dictionaryC(BASIC_MATERIALS_SECTOR, COMMUNICATION_SERVICES_SECTOR, CONSUMER_CYCLICAL_SECTOR, CONSUMER_DEFENSIVE_SECTOR, ENERGY_SECTOR, FINANCIAL_SERVICES_SECTOR, HEALTHCARE_SECTOR, INDUSTRIALS_SECTOR, TECHNOLOGY_SECTOR, UTILITIES_SECTOR)
