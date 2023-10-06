import copy

class Controller():
    
    def __init__(self,model) -> None:
        self.model = model

    def realizar_calculo(self):
        return self.model.realizar_calculo()
        
    def nova_conta(self,pagador,valor):
        self.model.nova_conta(pagador, valor)
       
    def get_nova_conta_status(self):
        return self.model.get_nova_conta_status()
    
    def pagar_divida(self, pagador, receptor):
        self.model.pagar_divida(pagador, receptor)
        
    def get_pagar_divida_status(self):
        return self.model.get_pagar_divida_status()
    
    def new_user(self,user):
        self.model.new_user(user)
        
    def get_users(self):
        return self.model.get_users()
         
    def get_transactions_string(self):
        return self.model.get_transactions_string()