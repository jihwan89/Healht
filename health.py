import random
class Health:
    def __init__(self, name = "", phonenumber = 0, in_day = 0, term = 0, id = 0):
        self.__name = name
        self.__phonenumber = phonenumber
        self.__in_day = in_day
        self.__term = term
        self.__id = id

    def getName(self): return self.__name
    def setName(self, name): self.__name = name

    def getPhonenumber(self): return self.__phonenumber
    def setPhonenumber(self, phonenumber): self.__phonenumber = phonenumber

    def getIn_Day(self): return self.__in_day
    def setIn_Day(self, in_day): self.__in_day = in_day

    def getTerm(self): return self.__term
    def setTerm(self, term): self.__term = term

    def getId(self): return self.__id
    def setId(self): self.__id = id

    client_data_list = []

    class Health_Manager:

        @classmethod
        def start_ui(cls):
            return f"""
    -----------------------------------------
                1. 관리자 | 2. 회원 
    ------------------------------------------
    입력> """

        @classmethod
        def login(cls):
            return """관리자 ID (4자리): """

        @classmethod
        def manager_ui(cls):
            return f'''
    --------------------------작업하실 번호를 입력하세요.----------------------
    1. 회원등록 | 2. 정보 수정 | 3. 회원 검색 | 4. 전체 회원 검색 | 5. 삭제 | 6. 종료
    --------------------------------------------------------------------
    입력> '''

        @classmethod
        def client_ui(cls):
            return f"""
        ----------------------작업하실 번호를 입력하세요.-----------------
                        1. 본인정보 조회 | 2. 종료 | 
        -----------------------------------------------------------
        입력> """



        @classmethod
        def add_menber(cls):
            print("-" * 5 + "회원 정보" + "-" * 5)
            name = input("회원 이름 : ")
            phonenumber = int(input("핸드폰 번호 : "))
            in_day = int(input("등록 날짜 : "))
            term = int(input("등록기간 : "))
            id = int(random.randint(1112,9999))
            print('-'*20)
            Health.client_data_list.append(name)
            Health.client_data_list.append(phonenumber)
            Health.client_data_list.append(in_day)
            Health.client_data_list.append(term)
            Health.client_data_list.append(id)
            print("저장 되었습니다.")

        @classmethod
        def modify(cls):
            name = input("수정할 회원의 이름을 입력하세요 : ")
            for i in Health.client_data_list:
                if name == i.name:
                    print("-" * 5 + "수정 할 회원 정보를 입력하세요" + "-" * 5)
                    m_name = input("회원 이름 : ")
                    m_phonenumber = int(input("핸드폰 번호 : "))
                    m_in_day = int(input("등록 날짜 : "))
                    m_term = int(input("등록기간 : "))
                    print("-" * 20)
                    Health.client_data_list[i.name] = m_name
                    Health.client_data_list[i.phonenumber] = m_phonenumber
                    Health.client_data_list[i.in_day] = m_in_day
                    Health.client_data_list[i.trem] = m_term
                    print(f"수정 결과 : 회원 이름 : {i.name}, 핸드폰 번호: {i.phonenumber}, 등록 날짜 : {i.in_day}, "
                          f"등록 기간: {i.trem}, 등록 번호: {i.id}")
                else:
                    print("등록 회원이 아닙니다.")

        @classmethod
        def search(cls):
            name = input("검색할 회원의 이름을 입력하세요 : ")
            if name in Health.client_data_list:
                for i in Health.client_data_list:
                    print(f"검색 결과 : 회원 이름 : {Health.client_data_list[i.name]}, 핸드폰 번호: {Health.client_data_list[i.phonenumber]}, "
                          f"등록 날짜 : {Health.client_data_list[i.in_day]}, 등록 기간: {Health.client_data_list[i.trem]}, 등록 번호: {Health.client_data_list[i.id]}")
            else:
                print("등록 회원이 아닙니다.")


        @classmethod
        def all_show(cls):
            for i in Health.client_data_list:
                print(f"전체검색 결과 : 회원 이름 : {i.name}, 핸드폰 번호: {i.phonenumber}, 등록 날짜 : {i.in_day}, "
                      f"등록 기간: {i.trem}, 등록 번호: {i.id}")

        @classmethod
        def delete(cls):
            name = input("삭제할 회원의 이름을 입력하세요 : ")
            for i in Health.client_data_list:
                if name == i.name:
                    Health.client_data_list[i].clear()
                else:
                    print("등록 회원이 아닙니다.")
            else:
                cls.all_show()

run = True
while (run):
    pick = int(input(Health.Health_Manager.start_ui()))
    if pick == 1:
        pick1 = int(input(Health.Health_Manager.login()))
        if pick1 == 1111 or pick1 == 0000:
            pick2 = int(input(Health.Health_Manager.manager_ui()))
            if pick2 == 1:
                Health.Health_Manager.add_menber()
            elif pick2 == 2:
                Health.Health_Manager.modify()
            elif pick2 == 3:
                Health.Health_Manager.search()
            elif pick2 == 4:
                Health.Health_Manager.all_show()
            elif pick2 == 5:
                Health.Health_Manager.delete()
            elif pick2 == 6:
                print("프로그램을 종료합니다.")
                run = False
            else:
                print("잘못된 입력입니다.")
        else:
            print("관리자가 아닙니다.")
    elif pick == 2:
        pick3 = int(input(Health.Health_Manager.client_ui()))
        if pick3 == 1:
            Health.Health_Manager.search()
        elif pick3 == 2:
            print("프로그램을 종료합니다.")
            run = False
        else:
            print("잘못된 입력입니다.")


