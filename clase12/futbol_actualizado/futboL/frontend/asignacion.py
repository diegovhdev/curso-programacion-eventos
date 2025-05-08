equipos = [
    {"nombre": "Equipo A", "ocupado": 6, "maximo": 10},
    {"nombre": "Equipo B", "ocupado": 4, "maximo": 10},
    {"nombre": "Equipo C", "ocupado": 9, "maximo": 10},
]

ultimo_indice = [0]  # Para Next Fit

def first_fit(jugadores):
    for equipo in equipos:
        if equipo["maximo"] - equipo["ocupado"] >= jugadores:
            equipo["ocupado"] += jugadores
            return f"{jugadores} jugadores asignados a {equipo['nombre']} (First Fit)"
    return "No hay espacio disponible"

def best_fit(jugadores):
    mejor = None
    for equipo in equipos:
        libre = equipo["maximo"] - equipo["ocupado"]
        if libre >= jugadores:
            if mejor is None or libre < (mejor["maximo"] - mejor["ocupado"]):
                mejor = equipo
    if mejor:
        mejor["ocupado"] += jugadores
        return f"{jugadores} jugadores asignados a {mejor['nombre']} (Best Fit)"
    return "No hay espacio disponible"

def worst_fit(jugadores):
    peor = None
    for equipo in equipos:
        libre = equipo["maximo"] - equipo["ocupado"]
        if libre >= jugadores:
            if peor is None or libre > (peor["maximo"] - peor["ocupado"]):
                peor = equipo
    if peor:
        peor["ocupado"] += jugadores
        return f"{jugadores} jugadores asignados a {peor['nombre']} (Worst Fit)"
    return "No hay espacio disponible"

def next_fit(jugadores):
    n = len(equipos)
    start = ultimo_indice[0]
    for i in range(n):
        idx = (start + i) % n
        equipo = equipos[idx]
        if equipo["maximo"] - equipo["ocupado"] >= jugadores:
            equipo["ocupado"] += jugadores
            ultimo_indice[0] = idx
            return f"{jugadores} jugadores asignados a {equipo['nombre']} (Next Fit)"
    return "No hay espacio disponible"

def mostrar_equipos():
    return "\n".join([f"{e['nombre']}: {e['ocupado']}/{e['maximo']}" for e in equipos])
