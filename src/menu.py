def display_menu():
    print('1. 논문 검색하기')
    print('2. 논문 수정하기')
    print('3. 전체 조회하기')
    print('4. 새로운 논문 저장하기')
    print('5. 논문 삭제하기')
    print('6. 논문 정렬하기')
    print('0. 작업 종료 & 저장')

def display_menu_search():
    print('1. 논문이름')
    print('2. 키워드') 
    print('3. 저자')
    print('4. 날짜')

def display_certain_data(data, i):  
    print(str(i+1) + '번째 논문')
    # print(data.paper_name)
    # print(data.keyWords)
    # print(data.author)
    # print(str(data.date))
    print(data.paper_name + '\t' + data.keyWords)
    print(data.author + '\t' + str(data.date))