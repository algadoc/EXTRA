def read_reader_data(file_info_dir):
    match file_info_dir["year"]:
        case 2018:
            return read_reader_data_2018(file_info_dir["pdf_reader"])
        case 2019:
            return read_reader_data_2019(file_info_dir["pdf_reader"])
        case 2020:
            return read_reader_data_2020(file_info_dir["pdf_reader"])
        case 2021:
            return read_reader_data_2021(file_info_dir["pdf_reader"])
        case 2022:
            return read_reader_data_2022(file_info_dir["pdf_reader"])
    
def read_reader_data_2018(reader_obj):
    return None

def read_reader_data_2019(reader_obj):
    return None

def read_reader_data_2020(reader_obj):
    return None
    
def read_reader_data_2021(reader_obj):
    return None

def read_reader_data_2022(reader_obj):
    return None