# Generate CSV of playlists from iTunes libary XML

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
custom_list = [
    'Bedwetting Cosmonaut Presents: Down By The Water (Spring Mix 2010)',
    'Indie/Rock Playlist: July (2010)','Top 680 Hip Hop Songs',
    'Ricky Gervais XFM','The Ricky Gervais Show','To Edit'
]

# Ignore both system and custom lists
lists = system_list + custom_list

# List of playlist types (i.e., smart/Genius and Folders) to ignore
types = ['Smart Info','Genius Track ID','Folder']

# Load iTunes library file
with open('Library.xml', 'rb') as fp:
    pl = plistlib.load(fp)

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
