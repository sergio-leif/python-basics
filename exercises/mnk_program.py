
def solution(S):
    for line in S.split('\n'):
        M, N, K = line.split(' ')
        M, N, K = int(M), int(N), int(K)
        result = ''
        for i in list(range(1, K+1)):
            if (i % M) == 0 and (i % N) == 0:
                result+='FB'
            else:
                if i % M == 0:
                    result+='F'
                if i % N == 0:
                    result+='B'
                if (i % M) != 0 and (i % N) != 0:
                    result+=str(i)
            if i != K:
                result+=' '
            
        return result

# program_input = input('Write the input in format "M N K": \n')
print(solution('4 9 59\n3 2 60'))

# print(bool(6%3))