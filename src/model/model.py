import copy

class Model():
    
    def __init__(self,users) -> None:
        self.users = users
        self.transactions = []
        self.nova_conta_status = ''
        self.pagar_divida_status = ''

    def realizar_calculo(self):
        
        # Calcula o total e a média dos saldos
        total = sum(list(user.values())[0] for user in self.users)
        try:
            average = total / len(self.users)
        except ZeroDivisionError:
            average = 0
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
        n_existe = True
        try:
            self.set_nova_conta_status('')
            for user in self.users:
                for name in user.keys():
                    if str(name).upper() == str(pagador).upper():
                        user[name] += float(valor)
                        n_existe = False
                        self.set_nova_conta_status(f'{pagador} pagou uma conta de {valor} reais!')
            if n_existe == True:
                self.set_nova_conta_status('Usuário não está presente no grupo')

        except:
            self.set_nova_conta_status('Campos não preenchidos corretamente')
            
        self.realizar_calculo()
    
    def set_nova_conta_status(self,status):
        self.nova_conta_status = status
    
    def get_nova_conta_status(self):
        print(self.nova_conta_status)
        return self.nova_conta_status
    
    def pagar_divida(self, pagador, receptor):
        
        transactions = self.get_transactions()
        
        if any(str(pagador).upper() in str(transaction[1]).upper() for transaction in transactions) and any(str(receptor).upper() in str(transaction[0]).upper() for transaction in transactions):

            ##################### Pagamento da divida #####################
            
            for index, user in enumerate(self.users):
                for name in user.keys():
                    if str(name).upper() == str(pagador).upper():
                        
                        for transacao in transactions:
                            if str(transacao[1]).upper() == str(pagador).upper():
                                self.users[index][name] += transacao[2]
                        # pass
            
            for index, user in enumerate(self.users):
                for name in user.keys():
                    if str(name).upper() == str(receptor).upper():
                        
                        for transacao in transactions:
                            if str(transacao[1]).upper() == str(pagador).upper():
                                self.users[index][name] -= transacao[2]
                        # pass
                        
            self.set_pagar_divida_status(f'Pagamento realizado de {pagador} para {receptor}!')
            ###############################################################
            
            self.realizar_calculo()
            
        elif any(str(pagador).upper() in str(transaction).upper() for transaction in transactions) and any(str(receptor).upper() in str(transaction).upper() for transaction in transactions):
            
            self.set_pagar_divida_status(f'O pagador e receptor descritos estão \nde alguma forma posicionados na lista de \ndevedores e pagadores, mas o pagador não deve \ndiretamente ao receptor')
            
        else:
            self.set_pagar_divida_status('Um, dois, ou nenhum dos nomes informados\n (de pagador e receptor) estão na lista de \ndevedores e pagadores')
    
    def set_pagar_divida_status(self,status):
        self.pagar_divida_status = status
    
    def get_pagar_divida_status(self):
        return self.pagar_divida_status
    
    def new_user(self,user):
        self.users.append({user:0})
        
    def get_users(self):
        string2 = ''
        for user in self.users:
            for name, value in user.items():
                string2 += f'{name} gastou R${value:.2f}' + '\n'
        if string2 == '':
            string2 = 'Não há usuários cadastrados no grupo!'
        return string2      
    
    def get_transactions(self):
        return self.transactions    

    def get_transactions_string(self):
        self.realizar_calculo()
        string = ''
        for transaction in self.transactions:
            payer, receiver, amount = transaction
            amount_rounded = round(amount, 2)
            string += f'{receiver} deve pagar R${amount_rounded:.2f} para {payer}' + '\n'
        if string == '':
            string = 'Não há transações pendentes!'
        return string