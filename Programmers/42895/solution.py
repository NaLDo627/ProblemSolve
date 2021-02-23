def solution(N, number):
    answer = 0
    candidate = [0, {N}]
    if number == N:
        return 1
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i // 2 + 1):
            for x in candidate[i_half]:
                for y in candidate[i - i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y // x)
                    if y != 0:
                        case_set.add(x // y)
        if number in case_set:
            return i
        candidate.append(case_set)
    return -1


print(solution(5, 12))  # 4
print(solution(2, 11))  # 3
