
def extract_search_terms(limit):
    search_terms = []
    file = open('files/football_cards_search_terms.txt','r')
    for line in file:
        current_line = line.strip()
        if current_line not in search_terms:
            search_terms.append(current_line)
            if limit != None:
                if len(search_terms) >= limit:
                    break
    file.close()
    return search_terms