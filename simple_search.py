from fetch_games import get_from_local
from collections import defaultdict

"""
Some variables:
    1. data_dump: it is the full game records from sites
    2. game_dict: game id as key, game name, alias, url as value
    3. analyzed_game_dict: all the possible search term as key, game ids as value
    4. history_map: history search term as key, game ids as value

Work flow:
    I. create game_dict and analyzed_game_dict from data_dump
    II. run the search on history map first, if found, return all the hits
    III. run the search on analyzed_game_dict, if found, return data from game_dict with title and url
"""

# index game data
data_dump = get_from_local()

# term analysis
analyzed_game_dict = defaultdict(set)
game_dict = dict()
for game in data_dump:
    key_words = set(game['name'].lower().split())
    for name in key_words:
        analyzed_game_dict[name].add(game['id'])
    game_dict[game['id']] = (game['name'], game['aliases'] if game['aliases'] else "", game['site_detail_url'])
history_map = defaultdict(set)


def print_title(game_set):
    print 'Title: ', game_set[0], ' | Site: ', game_set[2]


def search(search_word):
    found = False
    if history_map:
        if search_word in history_map.keys():
            for v in history_map[search_word]:
                print_title(game_dict[v])
            found = True

    if not found:
        for k, v in analyzed_game_dict.items():
            if search_word == k:
                for game_id in v:
                    history_map[search_word].add(game_id)
                    print_title(game_dict[game_id])

# demo, user input
while True:
    n = raw_input("Search for a game: ").strip().lower()
    if n == 'q':
        break
    else:
        search(n)