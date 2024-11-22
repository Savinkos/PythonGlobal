def vote(votes):
    vote_count = {}
    for candidate in votes:
        vote_count[candidate] = vote_count.get(candidate, 0) + 1
    
    # Ищем кандидата с наибольшим количеством голосов
    winner = max(vote_count, key=vote_count.get)
    return winner
if __name__ == '__main__':
    print(vote([1,1,1,2,3]))
    print(vote([1,2,3,2,2]))

