class CatVsDog
  attr_reader :cats, :dogs

  def maximize_viewers(votes)
    lovers_votes = votes.chunk { |n| n[0]}.max_by { |animal, ary| ary.size}[1].size
    haters_votes = votes.chunk { |n| n[1]}.max_by { |animal, ary| ary.size}[1].size
    
    return lovers_votes if lovers_votes > haters_votes
    haters_votes
  end

  def initialize(cats, dogs,  voters)
    @cats = cats
    @dogs = dogs
  end
end