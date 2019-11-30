def get_trainable_songs(triplet_files):
    songs = set()

    for triplet_file in triplet_files:
        with open(triplet_file, 'r') as f:
            for line in f:
                _, song_id, _ = line.strip().split('\t')
                songs.add(song_id)

    return songs
