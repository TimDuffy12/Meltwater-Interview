def add_keyword(temp_word, keyword_list):
    if temp_word != "":
        keyword_list.append(temp_word)


def parse_phrase(char, keyword_iter, temp_word):
    delim = char
    while True:
        char = next(keyword_iter)
        if char == delim:
            break
        else:
            temp_word += char
    return temp_word


def parse_keywords(keyword_string):
    delimiters = {' ', ','}
    phrase_delimeters = {'\'', '"'}
    keyword_list = []
    temp_word = ""
    keyword_string = keyword_string.lstrip()

    keyword_iter = iter(keyword_string)
    for char in keyword_iter:
        if char in delimiters:
            add_keyword(temp_word, keyword_list)
            temp_word = ""
        elif char in phrase_delimeters:
            temp_word = parse_phrase(char, keyword_iter, temp_word)
        else:
            temp_word += char
    keyword_list.append(temp_word)

    return keyword_list


def main():
    with open('keywords.txt') as f:
        raw_keywords = f.read()
    
    keywords = parse_keywords(raw_keywords)

    with open('concord_hymn.txt') as f:
        file_data = f.read()
    
    for keyword in keywords:
        file_data = file_data.replace(keyword, 'XXXX')
    
    with open('concord_hymn_censored.txt', 'w') as f:
        f.write(file_data)


if __name__ == "__main__":
    main()