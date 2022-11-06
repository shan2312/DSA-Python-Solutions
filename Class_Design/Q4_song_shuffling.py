import random

class Song:
    def __init__(self, title, genre) -> None:
        self.title = title
        self.genre = genre

class Shuffle:
    def __init__(self, favourite_genre):
        self.favourite_genre = favourite_genre
        self.song_list = []
        self.start_index_of_unplayed_songs = 0

    def addSong(self, song):
        self.song_list.append(song)
        if song.genre == self.favourite_genre:
            self.song_list.append(song)

    def swap_songs(self, i, j):
        self.song_list[i], self.song_list[j] = self.song_list[j], self.song_list[i]

    def restart_shuffle(self):
        self.start_index_of_unplayed_songs = 0

    def get_random_unplayed_song(self):
        num_songs = len(self.song_list)

        if num_songs == 0:
            return None

        if self.start_index_of_unplayed_songs >= num_songs:
            self.restart_shuffle()

        song_to_play_idx = random.randint(self.start_index_of_unplayed_songs, num_songs - 1)
        song_to_play = self.song_list[song_to_play_idx]
        self.swap_songs(self.start_index_of_unplayed_songs, song_to_play_idx)
        self.start_index_of_unplayed_songs += 1

        if song_to_play_idx > 0 and self.song_list[song_to_play_idx - 1] == song_to_play:
            self.swap_songs(self.start_index_of_unplayed_songs, song_to_play_idx - 1)
            self.start_index_of_unplayed_songs += 1

        if song_to_play_idx < num_songs - 1 and self.song_list[song_to_play_idx + 1] == song_to_play:
            self.swap_songs(self.start_index_of_unplayed_songs, song_to_play_idx + 1)
            self.start_index_of_unplayed_songs += 1

        return song_to_play

    def playSong(self):
        song_to_play = self.get_random_unplayed_song()
        if song_to_play is None:
            print('Error: no songs added, please use addSongs to add songs')
            return

        print(song_to_play.title)
        
if __name__ == '__main__':
        # Test 1 - add 3 songs and shuffle them 
    songShuffler = Shuffle('genre1') 
    songShuffler.addSong(Song('Song 1', 'genre1')) 
    songShuffler.addSong(Song('Song 2', 'genre2')) 
    songShuffler.addSong(Song('Song 3', 'genre1')) 

    print('Test 1:') 
    songShuffler.playSong() 
    songShuffler.playSong() 
    songShuffler.playSong() 
    print()

    # Test 2 - shuffle whole playlist and reset 
    songShuffler = Shuffle('genre1') 
    songShuffler.addSong(Song('Song 1', 'genre1')) 
    songShuffler.addSong(Song('Song 2', 'genre2')) 
    songShuffler.addSong(Song('Song 3', 'genre1')) 

    print('Test 2:') 
    songShuffler.playSong() 
    songShuffler.playSong() 
    songShuffler.playSong() 

    songShuffler.playSong() 
    songShuffler.playSong() 
    songShuffler.playSong() 
    print()

    # Test 3 - no songs added 
    songShuffler = Shuffle('genre1') 

    print('Test 3:') 
    print(songShuffler.playSong() == None) 
    print()

    # Test 4 - add songs, shuffle a few times, then add another song and shuffle more 
    songShuffler = Shuffle('genre1') 
    songShuffler.addSong(Song('Song 1', 'genre1')) 
    songShuffler.addSong(Song('Song 2', 'genre2')) 
    songShuffler.addSong(Song('Song 3', 'genre1')) 

    print('Test 4:') 
    songShuffler.playSong() 
    songShuffler.playSong() 

    songShuffler.addSong(Song('Song 4', 'genre1')) 
    songShuffler.playSong() 
    songShuffler.playSong() 
    print()