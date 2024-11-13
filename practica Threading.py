import threading
import time
import random

# Constantes
NUMERO_MESAS = 5
NUMERO_CAMAREROS = 3
TIEMPO_PREPARACION_MIN = 3  # Tiempo mínimo de preparación en segundos
TIEMPO_PREPARACION_MAX = 7  # Tiempo máximo de preparación en segundos
PLATOS = ["pizza", "tacos","hamburguesa", "molletes", "arroz", "pasta", "sopa", "ensalada"]

# Colas de pedidos
pedidos = []
lock_pedidos = threading.Lock()

# Función para simular una mesa
def mesa(num_mesa):
    pedido = random.choice(PLATOS)
    with lock_pedidos:
        pedidos.append((num_mesa, pedido))
    print(f"Mesa {num_mesa}: Pedido de {pedido}")

# Función para simular un camarero
def camarero(num_camarero):
    while True:
        with lock_pedidos:
            if not pedidos:
                break
            num_mesa, pedido = pedidos.pop(0)
        print(f"Camarero {num_camarero}: Preparando pedido de {pedido} para la mesa {num_mesa}")
        tiempo_preparacion = random.randint(TIEMPO_PREPARACION_MIN, TIEMPO_PREPARACION_MAX)
        time.sleep(tiempo_preparacion)
        print(f"Camarero {num_camarero}: Entregando pedido de {pedido} a la mesa {num_mesa} en: {tiempo_preparacion} minutos")

# Crear hilos para mesas
hilos_mesas = [threading.Thread(target=mesa, args=(i + 1,)) for i in range(NUMERO_MESAS)]

# Crear hilos para camareros
hilos_camareros = [threading.Thread(target=camarero, args=(i + 1,)) for i in range(NUMERO_CAMAREROS)]

# Iniciar hilos de mesas
for hilo in hilos_mesas:
    hilo.start()

# Esperar a que todas las mesas hayan hecho sus pedidos
for hilo in hilos_mesas:
    hilo.join()

# Iniciar hilos de camareros
for hilo in hilos_camareros:
    hilo.start()

# Esperar a que todos los camareros hayan terminado
for hilo in hilos_camareros:
    hilo.join()

print("Todos los pedidos han sido entregados.")