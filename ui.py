from person import person
from addressor import addressor

class ui:
    def __init__(self):
        self.addressor = addressor()  #계속 실행이 되어야하는 객체 / person은 그때그때 만드는 객체라 따로 지정하지않음


    def uiprint(self):
        print("필요한 기능을 선택하세요.")
        print("1.입력")
        print("2.출력")

    def run(self):
        while 1:
            op = input()
            if op == "1":
                person = self.makePerson()
                self.addressor.save(person)
            elif op == "2":
                people = self.addressor.getpeople()
                for p in people:
                    print(p.name)
            elif op == "3":    
                inputName = input()
                self.addressor.delete(inputName)
            #수정 기능
            elif op == "4":
                inputName = input()
                changeName = input()
                self.addressor.change(inputName, changeName)
            #검색 기능
            elif op == "5":
                findwhat = input()
                self.addressor.find(findwhat)
            #종료 기능
            elif op == "6":
                print("주소록 프로그램이 종료되었습니다")
                break
    
    #추가입력 기능
    def makePerson(self):
        inputName = input("이름:")
        inputPhone = input("번호:")
        return person(inputName, inputPhone)
    

