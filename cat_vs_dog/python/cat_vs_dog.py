#!/usr/local/bin/python

class CatVsDog:
  @staticmethod

  def maximize_viewers(votes):
    lovers_votes = CatVsDog.max_views(CatVsDog.chunks(votes, 0))
    haters_votes = CatVsDog.max_views(CatVsDog.chunks(votes, 1))

    if lovers_votes > haters_votes:
      haters_votes = lovers_votes
    return haters_votes

  @staticmethod
  def chunks(votes, index):
    result = {}
    for vote in votes:
      if vote[index] in result:
        result[vote[index]].append(vote)
      else:
        result[vote[index]] = [vote]  
    return result

  @staticmethod
  def max_views(l):
    result = 0
    for elem in l:
      if len(l[elem]) > result: 
        result = len(l[elem])
    return result

def main():
  T = input()
  answers = []
  for t in xrange(0, int(T)):
    cats, dogs, voters = raw_input().split()
    votes = []
    for i in xrange(0, int(voters)):
      vote = raw_input().split()
      votes.append(vote)
    
    answers.append(CatVsDog.maximize_viewers(votes))
  
  for a in answers:
    print(a)

main()
