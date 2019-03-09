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
