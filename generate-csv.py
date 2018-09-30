# Generate CSV of playlists
# playlist, track id, song, artist, album

# Using plistlib
import plistlib

# List of system-generated playlists to be ignored
system_list = ['Library','Downloaded','Music','Downloaded','Movies','Downloaded','TV Shows','Podcasts','Audiobooks']
]

# List of personal playlists to be ignored
custom_list = ['Bedwetting Cosmonaut Presents: Down By The Water (Spring Mix 2010)','Indie/Rock Playlist: July (2010)','Top 680 Hip Hop Songs','Ricky Gervais XFM','The Ricky Gervais Show','To Edit']

# Ignore both system and custom lists
lists = system_list + custom_list

# Tried to make a list of playlist types (i.e., smart) to ignore
# But had trouble implimenting later
types = ['Smart Info','Genius Track ID','Folder']

# Open iTunes library file
with open('Library.xml', 'rb') as fp:
    pl = plistlib.load(fp)

# Create CSV for writing
import csv

csv = open('songs.csv', "w")

columnTitleRow = "playlist, name, artist, album\n"
csv.write(columnTitleRow)

# Iterate over library file to ID playlists and extract tracks, match tracks
for i in pl['Playlists']:
    if i['Name'] in lists or 'Smart Info' in i or 'Genius Track ID' in i or 'Folder' in i:
        print('Ignore')
    else:
        # print(i['Name'])
        playlist = i['Name']
        # print(i['Playlist Items'])
        for item in i['Playlist Items']:
            # print(track['Track ID'])
            trackID = item['Track ID']
            # print("Track ID = " + str(trackID))
            # print(trackID)
            for track in pl['Tracks']:
                # print("Track = " + track)
                if int(track) == trackID:
                    row = playlist + ',' + pl['Tracks'][str(track)]['Name'] + ',' + pl['Tracks'][str(track)]['Artist'] + ',' + pl['Tracks'][str(track)]['Album'] + '\n'
                    for i in row:
                        i = i.strip
                    csv.write(row)
