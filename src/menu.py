def display_menu():
    print('=== MAIN MENU ===')
    print('1. 논문 검색하기')
    print('2. 논문 수정하기')
    print('3. 전체 조회하기')
    print('4. 새로운 논문 저장하기')
    print('5. 논문 삭제하기')
    print('6. 논문 정렬하기')
    print('0. 작업 종료 & 저장\n')

def display_menu_search():
    print('1. 논문이름')
    print('2. 키워드') 
    print('3. 저자')
    print('4. 요약')
    print('5. 날짜')

def display_certain_data(data, i):  
    print('\033[34m' + str(i+1) + '번째 논문' + '\033[0m')
    # print(data.paper_name)
    # print(data.keyWords)
    # print(data.author)
    # print(str(data.date))
    print(data.paper_name)
    print('\033[95m' + data.keyWords + '\033[0m')
    print(data.author + '\t' + str(data.date))
    print(data.summary)