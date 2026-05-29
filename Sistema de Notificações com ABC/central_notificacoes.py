class CentralNotificacoes:
    def __init__(self):
        self.notificadores = []

    def adicionar_notificador(self, notificador):
        self.notificadores.append(notificador)
        print(f"Notificador {type(notificador).__name__} adicionado à central.")

    def enviar_para_todos(self, mensagem):
        print(f"\nEnviando Mensagem padrâo para todos os Clientes")
        for notificador in self.notificadores:
            notificador.notificar(mensagem)