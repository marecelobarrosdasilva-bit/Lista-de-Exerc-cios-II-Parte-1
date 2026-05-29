from notificador import Notificador

class NotificadorEmail(Notificador):
    def __init__(self, email):
        self.email = email

    def notificar(self, mensagem):
        print(f"[E-mail] Para: {self.email} | Mensagem: {mensagem}")


class NotificadorSMS(Notificador):
    def __init__(self, telefone):
        self.telefone = telefone

    def notificar(self, mensagem):
        print(f"[SMS] Para: {self.telefone} | Mensagem: {mensagem}")


class NotificadorApp(Notificador):
    def __init__(self, usuario):
        self.usuario = usuario

    def notificar(self, mensagem):
        print(f"[App] Para: {self.usuario} | Mensagem: {mensagem}")