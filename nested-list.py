if __name__ == '__main__':
    students = {}
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in students:
            students[score] = [name]
        else:
            students[score].append(name)
        if score not in scores:
            scores.append(score)

    for s in sorted(students[sorted(scores)[1]]):
        print(s)
