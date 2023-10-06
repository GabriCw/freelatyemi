from ..controller.controller import Controller
from ..model.model import Model
from ..view.view import View

# Inicializando vetor users vazio
users = []

# Criando instâncias das classes MVC (model, view e controller)
model = Model(users)
controller = Controller(model)
view = View(model,controller)

# Inicializando Interface Gráfica com a janela1
view.abrir_janela1()