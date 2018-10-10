# Written for python 3.7.0

# Generate CSVs of playlists from iTunes libary XML

# Using plistlib to read Apple Proprety List format
import plistlib
# Using csv to write csv file
import csv

# List of system-generated playlists to be ignored
system_list = [
    'Library','Downloaded','Music','Downloaded','Movies','Downloaded',
    'TV Shows','Podcasts','Audiobooks'
]

# List of personal playlists to be ignored
custom_list = []

# Ignore both system and custom lists
lists = system_list + custom_list

# List of playlist types (i.e., smart/Genius and Folders) to ignore
types = ['Smart Info','Genius Track ID','Folder','Distinguished Kind']

# Load iTunes library file
with open('Library.xml', 'rb') as fp:
    pl = plistlib.load(fp)

# Iterate over library file to find desired playlists
for i in pl['Playlists']:
    # If playlist is in ignore lists, ignore it
    ignore = False
    if i['Name'] in lists:
        print('Ignore (system): ' + i['Name'])
    else:
        # If playlist is in ignored types, ignore it
        # Check if it is
        for type in types:
            if type in i:
                ignore = True
        # If it is, ignore it
        if ignore == True:
            print('Ignore (type): ' + i['Name'])
            continue
        # Otherwise, we want it
        else:
            playlist = i['Name'].replace('/', '')
            print('Writing: '+ playlist)
        ignore = False
        # Open CSV for writing
        with open('playlists/' + playlist + '.csv', 'wt', errors='ignore',
        newline='') as f:
            writer = csv.writer(f)
            # header, uncomment if desired
            # writer.writerow(('title', 'artist', 'album'))
            # Iterate over playlist items to find Track IDs
            for item in i['Playlist Items']:
                trackID = item['Track ID']
                # Iterate over entire library tracks to find matches
                for track in pl['Tracks']:
                    # If a match is found
                    if int(track) == trackID:
                        # Selector
                        t = pl['Tracks'][str(track)]
                        # print(t['Name'])
                        # Grab info from track, ignoring missing data
                        data = {
                            "Name": '',
                            "Artist": '',
                            "Album": ''
                        }
                        # make a for loop
                        for x in data:
                            try:
                                data[x] = t[x]
                            except KeyError:
                                data[x] = ""
                        row = [data["Name"], data["Artist"], data["Album"]]
                        # Add info to the CSV
                        writer.writerows([row])
