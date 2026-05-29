from notificadores import NotificadorEmail, NotificadorSMS, NotificadorApp
from central_notificacoes import CentralNotificacoes

central = CentralNotificacoes()

n1 = NotificadorEmail("mar@email.com")
n2 = NotificadorSMS("(92) 99233-4501")
n3 = NotificadorApp("Marcelo_app")

central.adicionar_notificador(n1)
central.adicionar_notificador(n2)
central.adicionar_notificador(n3)

central.enviar_para_todos("Sua conta foi atualizada com sucesso.")

# Perguntas:
# Qual classe representa o contrato formal?
# R: Notificador, pois usa ABC e declara notificar() com @abstractmethod, obrigando todas as subclasses a implementá-lo.

# Onde há polimorfismo?
# R: Em enviar_para_todos(), onde o for chama notificar() em cada objeto da lista e cada subclasse executa sua versão específica do método.

# Por que faz sentido usar ABC nesse caso?
# R: Porque garante que qualquer novo tipo de notificador criado no futuro obrigatoriamente implemente notificar(), evitando notificadores incompletos no sistema.

# O que aconteceria se uma subclasse não implementasse notificar()?
# R: O Python lançaria um TypeError ao tentar instanciar o objeto, impedindo que a subclasse incompleta seja usada.
