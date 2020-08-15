def person_lister(f):
    def inner(people):
        for i in range(len(people)):
            people[i][2] = int(people[i][2])
        people.sort(key=operator.itemgetter(2))
        return [f(p) for p in people]
    return inner
