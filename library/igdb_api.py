from igdb_api_python import igdb

igdb = igdb('44abe2c0cd85cbc3b8d54ebfcf5d5de1')

result = igdb.games(1942)

for game in result:
    print("Retrieved: " + game["name"])