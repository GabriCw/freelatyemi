import copy

class Projeto():
    
    def __init__(self,users) -> None:
        self.users = users
        self.transactions = []

    def realizar_calculo(self):
        
        # Calcula o total e a média dos saldos
        total = sum(list(user.values())[0] for user in self.users)
        average = total / len(self.users)
        balances = [copy.deepcopy(user) for user in self.users]
        
        # Calcula a diferença entre os saldos e a média
        for balance in balances:
            for key, value in balance.items():
                difference = value - average
                balance[key] = difference

        # Cria uma lista de transações
        transactions = []

        # Encontra as transações necessárias para equalizar os saldos (Mínimos Quadrados)
        while any(balance[key] > 0 for balance in balances for key in balance.keys()):
            payer = None
            receiver = None
            max_payment = 0
            found_transaction = False

            for i, balance1 in enumerate(balances):
                for j, balance2 in enumerate(balances):
                    if i != j:
                        for key1, value1 in balance1.items():
                            for key2, value2 in balance2.items():
                                if value1 > 0 and value2 < 0:
                                    payment = min(value1, -value2)
                                    if payment > max_payment:
                                        max_payment = payment
                                        payer = key1
                                        receiver = key2
                                        found_transaction = True

            if not found_transaction:
                break

            if payer is not None and receiver is not None:
                transactions.append((payer, receiver, max_payment))
                for balance in balances:
                    if payer in balance:
                        balance[payer] -= max_payment
                    if receiver in balance:
                        balance[receiver] += max_payment
        self.transactions = transactions
        return transactions

    def nova_conta(self,pagador,valor):
        for user in self.users:
            for name in user.keys():
                if str(name).upper() == str(pagador).upper():
                    user[name] += valor
                    
        self.realizar_calculo()
        pass
        
    def pagar_divida(self, pagador, receptor):
        
        transactions = self.get_transactions()
        
        if any(str(pagador).upper() in str(transaction[1]).upper() for transaction in transactions) and any(str(receptor).upper() in str(transaction[0]).upper() for transaction in transactions):
            print(f'É Possivel realizar o pagamento, pois o pagador descrito deve pro receptor descrito')

            ##################### Pagamento da divida #####################
            
            for index, user in enumerate(self.users):
                for name in user.keys():
                    if str(name).upper() == str(pagador).upper():
                        self.users[index][name] += 10
                        # pass
            
            for index, user in enumerate(self.users):
                for name in user.keys():
                    if str(name).upper() == str(receptor).upper():
                        self.users[index][name] -= 10
                        # pass
                        
            ###############################################################
            
            self.realizar_calculo()
            
        elif any(str(pagador).upper() in str(transaction).upper() for transaction in transactions) and any(str(receptor).upper() in str(transaction).upper() for transaction in transactions):
            print(f'O pagador e receptor descritos estão de alguma forma posicionados na lista de devedores e pagadores, mas o pagador nã deve diretamente ao receptor')
            
        else:
            print('Um, dois, ou nenhum dos nomes informados (de pagador e receptor) estão na lista de devedores e pagadores')
    
    def new_user(self,user):
        self.users.append({user:0})
        
    def get_users(self):
        return self.users        
    
    def get_transactions(self):
        return self.transactions    

    def get_transactions_string(self):
        # imprimir string bo
        pass
    
############################################ Criando uma instancia da classe Projeto para rodar os códigos ############################################

users = [{'Gabriel': 5}, {'Felipe': 10}, {'Davi': 5}, {'Jonathan': 7}, {'Gabriel P': 10}, {'Matheus': 20}]

projeto = Projeto(users)

projeto.new_user('Couto')
projeto.nova_conta('Couto',100)

transactions = projeto.realizar_calculo()

print(transactions)

usuarios = projeto.get_users()

# testando se o nome está na lista de transaçoes
projeto.pagar_divida('Gabriel','Couto')
print(usuarios)


