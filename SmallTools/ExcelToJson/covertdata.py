import xlrd


# get all the key from left to right
def get_key_name(worksheet):
    sh = worksheet.sheet_by_index(0)
    print(sh.row_values(0))

# get the key type

# get the value and covert it by type

# get the json key-pair

worksheet = xlrd.open_workbook('test.xlsx')
get_key_name(worksheet)


