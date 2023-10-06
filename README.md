-----------------------------------------------------------
----------- Rodando o Software com o arquivo view.py ------
-----------------------------------------------------------

para rodar o arquivo e consequentemente o software, basta abrir na raiz do projeto um terminal e digitar o seguinte comando:

``` python -m src.view.view ```


-----------------------------------------------------------
----------- POO -------------------------------------------
-----------------------------------------------------------

A Orientação a objetos foi implementada utilizando MVC (model, view e controller).

Na classe Model estão implementados e definidos os métodos lógicos que fazem o software funcionar

A classe Controller gerencia o acesso aos métodos da classe model

A classe View é responsável pela interface gráfica e tem acesso as duas classes Model e Controller para poder integrar os métodos lógicos com os métodos que viabilizam a interface gráfica


-----------------------------------------------------------
----------- explicar os principais métodos ----------------
-----------------------------------------------------------

Começar pela lógica do algoritmo que faz a divisão de contas ser possível, que é implementado no método 'realizar_calculo' na classe model. Explicar que ele foi desenvolvido inteligentemente para otimizar a quantidade e a qualidade das transações que se responsabilizam por equalizar as dividas de todos do grupo, de maneira justa.


-----------------------------------------------------------
----------- Futura Integração com Banco de Dados ----------
-----------------------------------------------------------

- Dizer que vai ser escolhida a integração com banco de dados das três opções possíveis (integração com BD, integração web, integração hardware externo).

- Explicar que essa arquitetura MVC com o padrão de projeto DAO (Data Access Object), vai permitir a integração com o banco de dados de forma a respeitar a orientação a objetos

- Dizer que esse banco de dados vai ser feito utilizando MySql


-----------------------------------------------------------
----------- Recursos a Serem Adicionados Futuramente ------
-----------------------------------------------------------

- Um botão para mostrar todas as contas e quem pagou (get_all_contas)
  - Nome da conta paga (ex: mercado do dia 17/09, aluguel casa, pizzas, etc...) + Nome do Usuario

- Mais de um grupo permitido, tendo seus participantes individuais (integração com BD)


-----------------------------------------------------------