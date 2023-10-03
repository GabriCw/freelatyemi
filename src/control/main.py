class Projeto():
    
    def __init__(self,users) -> None:
        self.users = users

    def realizar_calculo(self):
        # Calcula o total e a média dos saldos
        total = sum(list(user.values())[0] for user in self.users)
        average = total / len(self.users)
        balances = self.users
        
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
        return transactions


    # def nova_conta(self,usuario,valor):
    #     self.realizar_calculo()
    #     if usuario in self.usuarios:
    #         return True
    #     pass
  

users = [{'Gabriel': 8.08}, {'Felipe': 8.09}, {'Davi': 8.08}, {'Jonathan': 8.09}, {'Gabriel P': 8.08}, {'Matheus': 8.08}]

projeto = Projeto(users)

transactions = projeto.realizar_calculo()
print(transactions)

# # Imprime as transações com valores arredondados e invertidos
# for transaction in transactions:
#     payer, receiver, amount = transaction
#     amount_rounded = round(amount, 2)
#     print(f'{receiver} deve pagar R${amount_rounded:.2f} para {payer}')


# # Calcula o total e a média dos saldos
# total = sum(list(user.values())[0] for user in users)
# average = total / len(users)

# # Calcula a diferença entre os saldos e a média
# for balance in balances:
#     for key, value in balance.items():
#         difference = value - average
#         balance[key] = difference

# # Cria uma lista de transações
# transactions = []

# # Encontra as transações necessárias para equalizar os saldos (Mínimos Quadrados)
# while any(balance[key] > 0 for balance in balances for key in balance.keys()):
#     payer = None
#     receiver = None
#     max_payment = 0
#     found_transaction = False

#     for i, balance1 in enumerate(balances):
#         for j, balance2 in enumerate(balances):
#             if i != j:
#                 for key1, value1 in balance1.items():
#                     for key2, value2 in balance2.items():
#                         if value1 > 0 and value2 < 0:
#                             payment = min(value1, -value2)
#                             if payment > max_payment:
#                                 max_payment = payment
#                                 payer = key1
#                                 receiver = key2
#                                 found_transaction = True

#     if not found_transaction:
#         break

#     if payer is not None and receiver is not None:
#         transactions.append((payer, receiver, max_payment))
#         for balance in balances:
#             if payer in balance:
#                 balance[payer] -= max_payment
#             if receiver in balance:
#                 balance[receiver] += max_payment

