from src.menu import *

class certainData:
    def __init__(self):
        self.paper_name = None
        self.keyWords = None
        self.author = None
        self.date = None
        self.summary = None
        self.link = None

# list 로 받아온 키워드를 문자열로 변환
def keyWords2string(keyWords):
    string = ''
    for i in range(len(keyWords)):
        string += keyWords[i] + ', '
    return string

def search(data, cmd):
    select_cmd = cmd
    what2search = input('검색어를 입력하세요: ')
    print('\n')
    print('=== 검색 시작 ===')
    result_num = []
    if cmd == '1':
        for i in range(len(data)):
            if what2search in str(data[i].paper_name):
                display_certain_data(data[i], i)
                result_num.append(i)
    elif cmd == '2':
        for i in range(len(data)):
            if what2search in data[i].keyWords:
                display_certain_data(data[i], i)
                result_num.append(i)
    elif cmd == '3':
        for i in range(len(data)):
            if what2search in data[i].author:
                display_certain_data(data[i], i)
                result_num.append(i)
    elif cmd == '4':
        for i in range(len(data)):
            if what2search in str(data[i].date):
                display_certain_data(data[i], i)
                result_num.append(i)
    elif cmd == '4':
        for i in range(len(data)):
            if what2search in str(data[i].date):
                display_certain_data(data[i], i)
                result_num.append(i)
    elif cmd == '5':
        for i in range(len(data)):
            if what2search in str(data[i].summary):
                display_certain_data(data[i], i)
                result_num.append(i)
    else:
        print('ERR// 잘못된 명령어')
        search(data, select_cmd)

    print('=== 검색 종료 ===')

def edit(data, cmd):
    if cmd == '1':
        data.name = input('변경할 이름을 입력하세요: ')
    elif cmd == '2':
        pass
        # data.
    elif cmd == '3':
        data.author = input('변경할 이름을 입력하세요: ')
    elif cmd == '4':
        data.date = input('변경할 날짜를 입력하세요: ')

def register():
    tmp = certainData()
    tmp.paper_name = input('등록할 눈문의 이름을 입력하세요: ')
    tmp.keyWords = input('입력할 키워드를 입력하세요 (각 키워드 사이 \', \' 입력 필수): ')
    tmp.author = input('등록할 논문의 저자의 이름을 입력하세요: ')
    tmp.date = int(input('등록할 논문이 게제된 년도를 입력하세요: '))
    tmp.summary = input('논문의 내용을 요약해주세요: ')
    tmp.link = input('등록할 논문의 link 를 입력하세요: ')
    return tmp

# 삭제는 굳이 클래스화 안해도 될거같다

# def delete():

# 정렬 구현 해야함
