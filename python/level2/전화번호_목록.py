# 정렬을한 후 선정한 숫자가 그 다음 숫자의 접두어로 시작하는지 체크
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break

    return answer

# 다른 사람 풀이1
"""
zip을 이용하여 그 다음문자를 동시에 볼 수 있게 함
startswith 라는 함수는 어떤 문자로 시작하는지 확인하는 기능, return으로 True False 
"""
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

# 다른 사람 풀이2
"""
의도대로 해시로 풀기
1. 딕셔너리에 phone_book에 있는 모든 값을 넣어줌
2. 전화번호가 다른 번호의 접두어가 있는지 있는지 계속 비교, (이 때 전화번호가 비교하는 번호와 같으면 안된다)
윗 코드가 효율성면에선 더 좋긴함
"""
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer