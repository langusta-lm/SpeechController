def remove_command_from_query(query, commands):
    word_split = check_command_in_query(query, commands)
    if word_split:
        result = query.split(word_split[0])[-1]
        print('in remover from query', word_split, result)
        return result


def check_command_in_query(query, commands):
    result = []
    # if not isinstance(commands, list): commands = [commands]
    for command in commands:
        if command.lower() in query.lower():
            result.append(command)

    if result:
        return result
    else:
        return False


def check_word_phrase(words, query):
    """Checking if phrases occur in the query string"""
    good, bad = 0, 0
    for word in words:
        if word not in query:  # checking pojedyczne slowa
            bad += 1
        elif word in query:
            good += 1
    if good >= bad:
        # print(words, query)
        return True
    else:
        return False
