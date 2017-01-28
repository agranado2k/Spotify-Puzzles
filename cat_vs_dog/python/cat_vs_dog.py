#!/usr/local/bin/python

import sys
from bipartite_grath import bipartiteMatch

class CatVsDog:
  
  @staticmethod
  def maximize_viewers(votes):
    
    cat_lovers, dog_lovers, cat_haters = CatVsDog.create_the_lovers_and_haters_list(votes)
    bipartite_grath = CatVsDog.create_bipartite_grath(cat_lovers, dog_lovers, cat_haters)
    max_matching, p, u = bipartiteMatch(bipartite_grath)

    # print("votes", len(votes))
    # print("max_matching", len(max_matching))

    return (len(votes) - len(max_matching))

  @staticmethod
  def create_the_lovers_and_haters_list(votes):
    dog_lovers, cat_haters, cat_lovers, count = {}, {}, [], 0

    for vote in votes:
      vote = "%s %d" % (vote, count)
      count += 1

      if vote[0] == "D":
        partial_vote = vote.split(' ')

        if partial_vote[0] in dog_lovers:
          dog_lovers[partial_vote[0]].add(vote)
        else:
          dog_lovers[partial_vote[0]] = set([vote])

        if partial_vote[1] in cat_haters:
          cat_haters[partial_vote[1]].add(vote)
        else:
          cat_haters[partial_vote[1]] = set([vote])
      else:
        cat_lovers.append(vote)

    # print("dog_lovers: ", dog_lovers)
    # print("cat_haters: ", cat_haters)
    # print("cat_lovers: ", cat_lovers)

    return cat_lovers, dog_lovers, cat_haters

  @staticmethod
  def create_bipartite_grath(cat_lovers, dog_lovers, cat_haters):
    bipartite_grath = {}
    for cat_vote in cat_lovers:
      partial_cat_vote = cat_vote.split()
      bipartite_grath[cat_vote] = dog_lovers.get(partial_cat_vote[1],set()) | cat_haters.get(partial_cat_vote[0], set())

    # print("bipartite_grath: ", bipartite_grath)
    return bipartite_grath

def main():
  T = raw_input()
  if T != '':
    answers = []
    for t in xrange(0, int(T)):
      config_line = raw_input()
      if config_line != '':
        cats, dogs, voters = config_line.split()
        votes = []
        if voters > 0:
          for i in xrange(0, int(voters)):
            vote = raw_input()
            votes.append(vote)
          
          answers.append(CatVsDog.maximize_viewers(votes))
    
    for a in answers:
      print(a)

  return 0

sys.exit(main())
