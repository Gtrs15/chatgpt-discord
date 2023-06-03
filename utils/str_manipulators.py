import re


def extract_guild_ids(text):
    pattern = r'Guild id=(\w+)'
    matches = re.findall(pattern, text)
    return matches
