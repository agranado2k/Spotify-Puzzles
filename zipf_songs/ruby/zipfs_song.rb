class ZipfsSong
  def self.choose_popularities(songs_strucure)
        select_songs_by_q(songs_to_be_selected(songs_strucure), include_q(f1(songs_strucure), include_index(song_list(songs_strucure))))
  end

  def self.select_songs_by_q(songs, songs_list)
    songs_list_sorted = songs_list.sort do |song_a, song_b|
      result = -1
      result = 1 if song_a[:q] > song_b[:q]
      result = 1 if song_a[:q] == song_b[:q] && song_a[:index] < song_b[:index]
      result
    end
    songs_list_sorted.reverse[0..(songs-1)].map{|song| song[:name]}
  end

  def self.calculate_zi(f1, song_index)
    f1/song_index
  end

  def self.calculate_qi(fi,zi)
    fi/zi.to_f
  end

  def self.include_index(songs_list)
    songs_list.map.with_index{|song, index| song.merge(index: (index+1))}
  end

  def self.include_q(f1, songs_list)
    songs_list.map{|song| song.merge(q: calculate_qi(song[:listened], calculate_zi(f1, song[:index])))}
  end

  def self.song_list(structure)
    structure[:song_list]
  end

  def self.f1(structure)
    structure[:song_list].first[:listened]
  end

  def self.songs_to_be_selected(structure)
    structure[:have_to_choose]
  end
end