
def solution(S):
    text1, text2 = S.split('|')
    result = ''
    
    for num1, num2 in zip(create_list(text1), create_list(text2)):
	    result+=str(num1 * num2)+' '

    result = result[0:len(result) - 1]
    return result

def create_list(text):
    result = []
    for character in text:
        if character != ' ':
            result.append(int(character))
    return result

print(solution('1 2 3 4 5|5 4 3 2 1'))