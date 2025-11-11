def sort_leaderboard(leaderboard):
    prepared = []
    for name, score in leaderboard:
        prepared.append((-score, name))
    
    prepared.sort()

    result = []
    for neg_score, name in prepared:
        original_score = -neg_score
        result.append((name, original_score))

    return result

leaderboard = [
	('Alice', 88),
	('Bob', 92),
	('Charlie', 92),
	('David', 85)
]
print(sort_leaderboard(leaderboard))    