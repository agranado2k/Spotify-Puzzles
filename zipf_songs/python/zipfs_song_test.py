# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

from zipfs_song import ZipfsSong

# 2. Zipf’s Song (Difficulty Level: Medium)
# Problem ID: zipfsong

# Your slightly pointy-bearded boss has assigned you to write software to find the best songs from different music albums. And the software should be finished in an hour. 
# But don’t panic, you don’t have to solve the problem of writing an AI with good taste. At your disposal is the impeccable taste of a vast horde of long-tailed monkeys. 
# Well, at least almost. The monkeys are not very communicative (or rather, you’re not sure which song “Ook!” is supposed to refer to) so you can’t ask them which songs are the best.
#  What you can do however is to look at which songs the monkeys have listened to and use this information to deduce which songs are the best.

# At first, you figure that the most listened to songs must be the best songs. However, you quickly realize that this approach is flawed. 
# Even if all songs of the album are equally good, the early songs are more likely to be listened to more often than the later ones, because monkeys will tend to start listening to the 
# first song, listen for a few songs and then, when their fickle ears start craving something else, stop listening. Instead, if all songs are equal, you expect that their play 
# frequencies should follow Zipf’s Law.

# Zipf’s Law is an empirical law originally formulated about word frequencies in natural languages, but it has been observed that many natural phenomena, such as population sizes and 
# incomes, approximately follow the same law. It predicts that the relative frequency of thei’th most common object (in this case, a song) should be proportional to 1/i.

# To illustrate this in our setting, suppose we have an album where all songs are equally good. Then by Zipf’s Law, you expect that the first song is listened to twice as often as the 
# second song, and more generally that the first song is listened to i times as often as the i’th song. When some songs are better than others, those will be listened to more often than 
# predicted by Zipf’s Law, and those are the songs your program should select as the good songs. Specifically, suppose that song i has been played fi times but that Zipf’s Law predicts 
# that it would have been played zi times. Then you define the quality of song i to be qi = fi / zi. Your software should select the songs with the highest values of qi.

# Input
# The first line of input contains two integers n and m (1 ≤ n ≤ 50000, 1 ≤ m ≤ n), the number of songs on the album, and the number of songs to select. Then follow n lines. 
# The i’th of these lines contains an integer fi and string si, where 0 ≤ fi ≤ 10^12 is the number of times the i’th song was listened to, and si is the name of the song. 
# Each song name is at most 30 characters long and consists only of the characters ‘a’-‘z’, ‘0’-‘9’, and underscore (‘_’).

# Output
# Output a list of the m songs with the highest quality qi, in decreasing order of quality. If two songs have the same quality, give precedence to the one appearing first on the 
# album (presumably there was a reason for the producers to put that song before the other).

# Sample input 1
# 4 2
# 30 one
# 30 two
# 15 three
# 25 four
# Sample output 1
# four
# two
# Sample input 2
# 15 3
# 197812 re_hash
# 78906 5_4
# 189518 tomorrow_comes_today
# 39453 new_genious
# 210492 clint_eastwood
# 26302 man_research
# 22544 punk
# 19727 sound_check
# 17535 double_bass
# 18782 rock_the_house
# 198189 19_2000
# 13151 latin_simone
# 12139 starshine
# 11272 slow_country
# 10521 m1_a1
# Sample output 2
# 19_2000
# clint_eastwood
# tomorrow_comes_today

class ZipfsSongTests(unittest.TestCase):
  def test_calculate_zi(self):
    f1 = 30
    song_2_index, z2 = 2, 15
    song_3_index, z3 = 3, 10

    self.assertEqual(z2, ZipfsSong.calculate_zi(f1, song_2_index))
    self.assertEqual(z3, ZipfsSong.calculate_zi(f1, song_3_index))

  def test_calculate_qi_for_first_song(self):
    f1, z1, q1 = 30, 30, 1
    self.assertEqual(q1, ZipfsSong.calculate_qi(f1, z1))

  def test_calculate_qi_for_second_song(self):
    f2, z2, q2 = 30, 15, 2
    self.assertEqual(q2, ZipfsSong.calculate_qi(f2, z2))

  def test_calculate_qi_for_third_song(self):
    f3, z3, q3 = 15, 10, 1.5
    self.assertEqual(q3, ZipfsSong.calculate_qi(f3, z3))

  def test_include_indexies_for_songs_list(self):
    song_list = [{'listened': 30, 'name': 'one'},
                {'listened': 30, 'name': 'two'},
                {'listened': 15, 'name': 'three'},
                {'listened': 25, 'name': 'four'}]

    output = [{'index': 1, 'listened': 30, 'name': 'one'},
              {'index': 2, 'listened': 30, 'name': 'two'},
              {'index': 3, 'listened': 15, 'name': 'three'},
              {'index': 4, 'listened': 25, 'name': 'four'}]

    self.assertEqual(output, ZipfsSong.include_index(song_list))

  def test_include_q_for_each_song(self):
    f1 = 30
    song_list = [{'index': 1, 'listened': 30, 'name': 'one'},
              {'index': 2, 'listened': 30, 'name': 'two'},
              {'index': 3, 'listened': 15, 'name': 'three'},
              {'index': 4, 'listened': 25, 'name': 'four'}]

    output = [{'index': 1, 'q': 1.0, 'listened': 30, 'name': 'one'},
              {'index': 2, 'q': 2.0, 'listened': 30, 'name': 'two'},
              {'index': 3, 'q': 1.5, 'listened': 15, 'name': 'three'},
              {'index': 4, 'q': 3.5714285714285716, 'listened': 25, 'name': 'four'}]

    self.assertEqual(output, ZipfsSong.include_q(f1, song_list))

  def test_select_songs_with_highest_q(self):
    songs_number = 2
    song_list = [{'index': 1, 'q': 1.0, 'listened': 30, 'name': 'one'},
              {'index': 2, 'q': 2.0, 'listened': 30, 'name': 'two'},
              {'index': 3, 'q': 1.5, 'listened': 15, 'name': 'three'},
              {'index': 4, 'q': 3.5714285714285716, 'listened': 25, 'name': 'four'}]

    songs_selected = ['four', 'two']

    self.assertEqual(songs_selected, ZipfsSong.select_songs_by_q(songs_number, song_list))

  def test_sample_1(self):
    # skip
    input = {'songs': 4, 'have_to_choose': 2, 
      'song_list': [{'listened': 30, 'name': 'one'},
                {'listened': 30, 'name': 'two'},
                {'listened': 15, 'name': 'three'},
                {'listened': 25, 'name': 'four'}]}
    output = ['four','two']

    self.assertEqual(output, ZipfsSong.choose_popularities(input))

  def test_sample_2(self):
    # skip
    input = {'songs': 15, 'have_to_choose': 3, 
      'song_list': [{'listened': 197812, 'name': 're_hash'},
                {'listened': 78906, 'name': '5_4'},
                {'listened': 189518, 'name': 'tomorrow_comes_today'},
                {'listened': 39453, 'name': 'new_genious'},
                {'listened': 210492, 'name': 'clint_eastwood'},
                {'listened': 26302, 'name': 'man_research'},
                {'listened': 22544, 'name': 'punk'},
                {'listened': 19727, 'name': 'sound_check'},
                {'listened': 17535, 'name': 'double_bass'},
                {'listened': 18782, 'name': 'rock_the_house'},
                {'listened': 198189, 'name': '19_2000'},
                {'listened': 13151, 'name': 'latin_simone'},
                {'listened': 12139, 'name': 'starshine'},
                {'listened': 11272, 'name': 'slow_country'},
                {'listened': 10521, 'name': 'm1_a1'}
                ]}
    output = ['19_2000','clint_eastwood', 'tomorrow_comes_today']

    self.assertEqual(output, ZipfsSong.choose_popularities(input))


  def test_sample_3(self):
    # skip
    input = {'songs': 5, 'have_to_choose': 2, 
      'song_list': [{'listened': 30, 'name': 'one'},
                {'listened': 30, 'name': 'two'},
                {'listened': 15, 'name': 'three'},
                {'listened': 25, 'name': 'four'},
                {'listened': 12, 'name': 'five'}]}
    output = ['four','two']

    self.assertEqual(output, ZipfsSong.choose_popularities(input))

  def test_sample_4(self):
    # skip
    input = {'songs': 5, 'have_to_choose': 2, 
      'song_list': [{'listened': 30, 'name': 'one'},
                {'listened': 30, 'name': 'two'},
                {'listened': 15, 'name': 'three'},
                {'listened': 25, 'name': 'four'},
                {'listened': 20, 'name': 'five'}]}
    output = ['four','five']

    self.assertEqual(output, ZipfsSong.choose_popularities(input))


if __name__ == '__main__':
  unittest.main()