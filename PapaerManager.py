#
#  PapaerManager
#  ver 0.1
#
#  crafted by DDing
# 

"""
개요

# 구현하고 싶은 개요
1. 엑셀파일 읽고 쓰기
2. 각 셀의 내용 탐색, 갯수 새기 (키워드, 저자)
3. 

# 각 셀에 저장할 paper 정보
이름, 키워드, 저자, 날짜, pdf 링크
+ 개인 요약 ## 이거는 제일 마지막에 구현하자

# 메인 메뉴
1. 검색하기
2. 수정하기
3. 전체조회
4. 등록하기
5. 삭제하기
6. 정렬하기

# 계획
1. 각 논문에 대하여 class 화 한 후 그것을 list 로 관리할 것
2. 각 기능을 class 화 하여 관리할 것

# 작업하던 것
파일 로드에 있어서 파일의 존재에 대한 판단을 어떻게 할까?
"""

import openpyxl

# def load_xlsx(file_name):
    # wb = openpyxl.load_workbook(filename)
def err():
    print('ERR// 아직 구현하지 않음')

# def display_certain_data(data, i):
#     print(str(i+1) + '번째 논문 ' + data[i].paper_name + '\t' + str(data[i].keyWords))
#     print(data[i].author + '\t' + data[i].date)

class certainData:
    def __init__(self):
        self.paper_name = None
        self.keyWords = None
        self.author = None
        self.date = None
        self.link = None

class menu:  
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

# list 로 받아온 키워드를 문자열로 변환
def keyWords2string(keyWords):
    string = ''
    for i in range(len(keyWords)):
        string += keyWords[i] + ', '
    return string

class search_menu:
    def search(data, cmd):
        what2search = input('검색어를 입력하세요: ')

        result_num = []
        if cmd == '1':
            for i in range(len(data)):
                if what2search in str(data[i].paper_name):
                    menu.display_certain_data(data[i], i)
                    result_num.append(i)
        elif cmd == '2':
            for i in range(len(data)):
                if what2search in data[i].keyWords:
                    menu.display_certain_data(data[i], i)
                    result_num.append(i)
        elif cmd == '3':
            for i in range(len(data)):
                if what2search in data[i].author:
                    menu.display_certain_data(data[i], i)
                    result_num.append(i)
        elif cmd == '4':
            for i in range(len(data)):
                if what2search in str(data[i].date):
                    menu.display_certain_data(data[i], i)
                    result_num.append(i)

        print('검색 종료')

class edit_menu:
    def edit(data, cmd):
        if cmd == '1':
            data.name = input('변경할 이름을 입력하세요: ')
        elif cmd == '2':
            err()
            # data.
        elif cmd == '3':
            data.author = input('변경할 이름을 입력하세요: ')
        elif cmd == '4':
            data.date = input('변경할 날짜를 입력하세요: ')

class register_menu:
    def register():
        tmp = certainData()
        tmp.paper_name = input('등록할 눈문의 이름을 입력하세요: ')
        tmp.keyWords = input('입력할 키워드를 입력하세요 (각 키워드 사이 \', \' 입력 필수): ')
        tmp.author = input('등록할 논문의 저자의 이름을 입력하세요: ')
        tmp.date = int(input('등록할 논문이 게제된 년도를 입력하세요: '))
        tmp.link = input('등록할 논문의 link 를 입력하세요: ')
        return tmp

# 삭제는 굳이 클래스화 안해도 될거같다
# class delete_menu:
#     def delete():

# 정렬 구현 해야함
# class line_menu:   

if __name__ == "__main__":
    # 메뉴로 쓸 클래스 선언,, 이거 이렇게 하는거 맞나?
    menu()
    search_menu()
    register_menu()

    xlsx_name = 'test_sheet.xlsx'
    # xlsx_name = input('불러올 파일을 입력하세요: ')
    # if (파일이 없다는 조건문):
    #     print("파일이 존재하지 않습니다")
    #     cmd = input('새로 만들겠습니까? (y/n): ')
    #     if cmd == 'y':
    #             xlsx_name = input('파일명을 입력하세요: ')
    #             wb = openpyxl.load_workbook()

    # load file
    # load_xlsx(xlsx_name)
    wb = openpyxl.load_workbook(xlsx_name)
    ws = wb.get_sheet_by_name('main_sheet') # 해당 sheet 의 이름을 알아야 한다

    # data 로드
    # 최대 행, 열 크기 구하기
    for i in range(100): # 일단 100 으로 두었다
        if ws['A' + str(i + 1)].value == None:
            max_row = i
            break

    data = []
    for i in range(max_row):
        tmp = certainData()

        tmp_keyWords = str(ws['B' + str(i + 1)].value)
        print(type(tmp_keyWords))
        tmp.paper_name = ws['A' + str(i + 1)].value
        # 본래 list 로 나눌까 했는데 필요시에만 하면 될거같아
        # tmp.keyWords = tmp_keyWords.split(', ')
        tmp.keyWords = tmp_keyWords
        tmp.author = ws['C' + str(i + 1)].value
        tmp.date = ws['D' + str(i + 1)].value 
        tmp.link = ws['E' + str(i + 1)].value
        data.append(tmp)

    # 이제부터 실제 메뉴 display
    while(1): 
        menu.display_menu()
        cmd = input('시작할 작업을 선택하세요: ')

        if cmd == '1':
            print('논문 검색하기 시작')

            menu.display_menu_search()
            cmd = input('무엇으로 검색하시겠습니까?: ')

            search_menu.search(data, cmd)

        elif cmd == '2':
            print('논문 수정하기 시작')
            
            menu.display_menu_search()
            cmd = input('무엇으로 수정하겠습니까?: ')

            edit_menu.edit(data[i], cmd)

        elif cmd == '3':
            print('\n저장된 전체 논문 조회')
            for i in range(len(data)):
                menu.display_certain_data(data[i], i)
            print('전체 논문 조회 종료\n')

        elif cmd == '4':
            print('새로운 논문 저장')
            tmp = certainData()
            tmp = register_menu.register()
            data.append(tmp)

        elif cmd == '5':
            print('등록된 논문 삭제')
            
            cmd = input('삭제할 논문의 번호를 입력하세요: ')
            del data[int(cmd)-1]

        elif cmd == '6':
            print('논문 정렬하기')
            err()

        elif cmd == '0':
            print('작업을 종료합니다')

            cmd = input('저장할건가요? (y/n): ')
            if cmd == 'y':
                # data 저장
                for i in range(len(data)):
                    ws['A' + str(i + 1)] = data[i].paper_name
                    ws['B' + str(i + 1)] = data[i].keyWords
                    ws['C' + str(i + 1)] = data[i].author
                    ws['D' + str(i + 1)] = data[i].date
                    ws['E' + str(i + 1)] = data[i].link
                
                cmd = input('저장될 파일의 이름을 변경하겠습니까? (y/n): ')
                if cmd == 'y':
                    save_name = input('저장될 이름을 입력하세요 (.xlsx 포함): ')
                    wb.save(save_name)
                    print(save_name + ' 으로 저장되었습니다')
                else:
                    wb.save(xlsx_name)
                    print(xlsx_name + ' 으로 저장되었습니다')

                print('프로그램 종료' + '\n')

            exit()


            

