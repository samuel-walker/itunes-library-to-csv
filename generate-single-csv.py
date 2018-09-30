# You can use this script to generate a single csv instead of multiple

# Open CSV for writing
with open('songs.csv', 'wt', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(('playlist', 'name', 'artist', 'album'))
    # Iterate over library file to find desired playlists
    for i in pl['Playlists']:
        # If playlist is in ignore lists, ignore it
        if i['Name'] in lists:
            print('Ignore')
        elif True:
            # If playlist is in ignored types, ignore it
            for type in types:
                if type in i:
                    print('Ignore')
                    ignore = True
                else:
                    ignore = False
            # Otherwise, we want it
            if ignore == True:
                continue
            else:
                playlist = i['Name']
                print(playlist)
                # Iterate over playlist items to find Track IDs
                for item in i['Playlist Items']:
                    trackID = item['Track ID']
                    # Iterate over entire library tracks to find matches
                    for track in pl['Tracks']:
                        # If a match is found
                        if int(track) == trackID:
                            # Selector
                            t = pl['Tracks'][str(track)]
                            print(t['Name'])
                            # Grab info from track
                            row = [playlist,t['Name'],t['Artist'],t['Album']]
                            # Add info to the CSV
                            writer.writerows([row])
