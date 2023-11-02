#el principio de open closed se refiere a que el codigo debe estar abierto para expandir pero cerrado para modificar


class notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    
class notificador_email(notificador):
    def notificar(self):
        print(f"Enviando mensaje por Mail a {self.usuario.email}")

class notificador_twitter(notificador):
    def notificar(self):
        print(f"Enviando mensaje por Twitter a {self.usuario.email}")

class notificador_texto(notificador):
    def notificar(self):
        print(f"Enviando mensaje por Texto a {self.usuario.email}")
