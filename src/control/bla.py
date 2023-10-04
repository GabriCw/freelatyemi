class Projeto:
    def __init__(self, users):
        self.users = users

users = [{'Gabriel': 5}, {'Felipe': 10}, {'Davi': 5}, {'Jonathan': 7}, {'Gabriel P': 10}, {'Matheus': 20}]

projeto = Projeto(users)

print(projeto.users)
