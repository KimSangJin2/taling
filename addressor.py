class addressor:
    def __init__(self):
        self.people = []

    def save(self, person):
        self.people.append(person)

    def getpeople(self):
        return self.people   # 여기에 print를 찍으면 안됨. 객체지향에 맞지 않는, 호환성이 없는 코드야.

    def delete(self, name):
        for i, p in enumerate(self.people):
            if name == p.name:
                del self.people[i]
                
    #수정 기능
    def change(self, firstName, changeName):
        for i, p in enumerate(self.people):
            if p.name == firstName:
                p.name = changeName
            if p.phone == firstName:
                p.phone = changeName
    #검색 기능
    def find(self, findwhat):
        for i, p in enumerate(self.people):
            if p.name == findwhat or p.phone == findwhat:
                print(p.name, p.phone)
