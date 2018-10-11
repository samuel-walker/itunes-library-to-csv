# itunes-library-to-csv

This program reads in an iTunes library (exported as Library.xml, File > Library > Export Library) and writes out CSV files of track name, artist, and album for each playlist.

# Requirements

Python 3.x

# Usage

[generate-csv.py](generate-csv.py) reads Library.xml and writes out the CSV files in the same folder.

To use, add Library.xml to this folder and then run the following command in the command prompt (Windows):

`python generate-csv.py`

# Customization

You can modify two pieces of information to customize the script.

## List of system-generated playlists to be ignored

`system_list` contains a list of iTunes-generated playlists to ignore. You can add or remove as you see fit.

```python
system_list = [
    'Library','Downloaded','Music','Downloaded','Movies','Downloaded',
    'TV Shows','Podcasts','Audiobooks'
]
```

## List of personal playlists to be ignored

`custom_list` is empty by default. Add any of your own playlists you wish to ignore here.

```python
custom_list = []
```

## List of playlist types to ignore

Finally, `types` contains playlist types I wanted to ignore. Again, edit these as you see fit.

```python
types = ['Smart Info','Genius Track ID','Folder','Distinguished Kind']
```

# Use case

I use the CSVs with [gmusic-playlist](https://github.com/soulfx/gmusic-playlist) to create new playlists in a [Google Play Music](http://www.music.google.com) account to match those in the iTunes library. It simply uses the CSV to search GPM using the tags from iTunes, so no guarantee it will find the correct songs!
