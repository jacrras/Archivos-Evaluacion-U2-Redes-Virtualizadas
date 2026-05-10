import json

nodos = [
    {
        "nombre": "Router-Core",
        "pais": "Chile",
        "tipo_dispositivo": "Router"
    },
    {
        "nombre": "Switch-Distribucion",
        "pais": "Chile",
        "tipo_dispositivo": "Switch"
    },
    {
        "nombre": "Firewall-Perimetral",
        "pais": "Chile",
        "tipo_dispositivo": "Firewall"
    }
]

with open("nodos.json", "w") as archivo:
    json.dump(nodos, archivo, indent=4, ensure_ascii=False)

print("El archivo nodos.json fue creado correctamente.")
