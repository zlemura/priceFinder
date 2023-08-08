from DatabaseRecord import DatabaseRecord
def extract_database_records(limit):
    database_records = []
    file = open('files/football_cards_database_records.txt','r')
    for line in file:
        current_line_split = line.split(",")
        database_records.append(DatabaseRecord(current_line_split[0], current_line_split[1], current_line_split[2],
                                               current_line_split[3],current_line_split[4], current_line_split[5],
                                               current_line_split[6], current_line_split[7], current_line_split[8]))
    file.close()
    return database_records