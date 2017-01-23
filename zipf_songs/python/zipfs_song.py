#!/usr/local/bin/python

class ZipfsSong:
  @staticmethod
  def calculate_zi(f1, song_index):
    return f1/song_index

  @staticmethod
  def calculate_qi(fi,zi):
    return fi/float(zi)

  @staticmethod
  def include_index(song_list):
    index = 1
    for song in song_list:
      song['index'] = index
      index +=1 
    return song_list

  @staticmethod
  def include_q(f1, song_list):
    for song in song_list:
      song['q'] = ZipfsSong.calculate_qi(song['listened'], ZipfsSong.calculate_zi(f1, song['index']))

    return song_list

  @staticmethod
  def compare_song(song_a, song_b):
    if song_a['q'] > song_b['q']:
      return 1
    if song_a['q'] == song_b['q'] and song_a['index'] < song_b['index']:  
      return 1 
    
    return -1

  @staticmethod
  def select_songs_by_q(songs_number, song_list):
    result = []
    selected_songs = sorted(song_list, reverse=True, cmp=ZipfsSong.compare_song)[:songs_number]
    for song in selected_songs:
      result.append(song['name'])
    return  result

  @staticmethod
  def choose_popularities(structure):
    songs_number = structure['have_to_choose']
    song_list = structure['song_list']
    f1 = structure['song_list'][0]['listened']

    return ZipfsSong.select_songs_by_q(songs_number, ZipfsSong.include_q(f1, ZipfsSong.include_index(song_list)))


def main():
  n_songs, select_songs = raw_input().split()
  n_songs = int(n_songs)
  select_songs = int(select_songs)
  song_list = []
  n = 0

  while n != n_songs:
    listened, name = raw_input().split()
    listened = int(listened)
    song_list.append({'listened': listened, 'name': name})      
    n += 1

  songs = ZipfsSong.choose_popularities({'songs': n_songs, 'have_to_choose': select_songs, 'song_list': song_list})
  for song in songs:
    print(song)

main()
