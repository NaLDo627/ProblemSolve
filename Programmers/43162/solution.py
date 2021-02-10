def solution(n, computers):
    answer = 0
    checked = [0] * n
    queue = []

    for i in range(n):
        if checked[i] != 0:
            continue

        checked[i] = 1
        answer += 1

        for j in range(n):
            if i == j:
                continue

            if checked[j] != 0:
                continue

            if computers[i][j] == 0:
                continue

            queue.append(j)

        while len(queue) != 0:
            start = queue[0]
            del queue[0]
            checked[start] = 1

            for end in range(n):
                if start == end:
                    continue

                if checked[end] != 0:
                    continue

                if computers[start][end] == 0:
                    continue

                queue.append(end)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
