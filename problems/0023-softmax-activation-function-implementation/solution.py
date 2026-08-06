import math

def softmax(scores: list[float]) -> list[float]:

    c = max(scores)

    result = []

    a = 0
    for j in range(len(scores)):
        a += math.exp(scores[j] - c)

    for i in range(len(scores)):
        result.append(round(math.exp(scores[i] - c) / a, 4))

    return result