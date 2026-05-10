import re

class DispositivoRed:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip

    def validar_ip(self):
        patron_ipv4 = r"^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$"

        if re.match(patron_ipv4, self.ip):
            print(f"Dispositivo: {self.nombre}")
            print(f"IP: {self.ip}")
            print("Resultado: La dirección IP ingresada es válida.")
        else:
            print(f"Dispositivo: {self.nombre}")
            print(f"IP: {self.ip}")
            print("Resultado: La dirección IP ingresada NO es válida.")

router = DispositivoRed("Router-Core", "192.168.1.1")
router.validar_ip()

print("-------------------------")

switch = DispositivoRed("Switch-Acceso", "300.168.1.1")
switch.validar_ip()
