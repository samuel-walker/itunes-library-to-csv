# Notes

Path to array of playlists = `/plist/dict/array`
Some playlists are system and can be ignored:
- Library
- Downloaded
- Music
- Downloaded
- Movies
- Downloaded
- TV Shows
- Podcasts
- Audiobooks

Playlists contain arrays of `dict`s, which contain `key`s of "Track ID" matched with `integer`s of the Track ID number. So, generating plain-text versions of the playlists requires finding the Track IDs in `/plist/dict/dict`. This `dict` has `key`s of Track ID and `dict`s with track info.

So to put it in XML refs,
- For `dict` in `/plist/dict/array`, if Name != list above and Folder == FALSE:
  - Playlist name = `/plist/dict/array/dict[index]/string`
  - Playlist tracks = `dict` in `/plist/dict/array/dict[index]/array`
    - For tracks in above
      - Track ID = `/plist/dict/array/dict[10]/array/dict/integer`
        - Search `/plist/dict/dict/key[index]` for Track ID
          - For matching Track IDs,
            - Track name =
            - Track artist =
            - Track album =
