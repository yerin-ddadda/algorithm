import collections

def solution(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys())[0])
    return list(answer.keys())[0]

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])