import re


def extract_guild_ids(text):
    pattern = r'Guild id=(\w+)'
    matches = re.findall(pattern, text)
    return matches


# Splits string so that it does not reach discord char limit
def split_string(message, max_chars):

    if len(message) < max_chars:
        return [message]

    words = message.split()
    result = []
    current = ''
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            # add word to current piece
            current += ' ' + word if current else word
        else:
            # add current piece to result list and start new piece
            result.append(current)
            current = word
    # add last piece to result list
    if current:
        result.append(current)
    return result
