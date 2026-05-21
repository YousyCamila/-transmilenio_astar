import heapq
import math

# COORDENADAS GEOGRÁFICAS DE LAS ESTACIONES 

COORDENADAS = {
    # Troncal Norte (Autopista Norte)
    "Portal Norte":       (4.7562, -74.0452),
    "Toberín":            (4.7408, -74.0461),
    "Calle 161":          (4.7341, -74.0464),
    "Mazurén":            (4.7261, -74.0469),
    "Calle 146":          (4.7183, -74.0472),
    "Calle 142":          (4.7138, -74.0474),
    "Calle 134":          (4.7063, -74.0477),
    "Alcalá":             (4.6998, -74.0476),
    "Prado":              (4.6916, -74.0478),
    "Calle 127":          (4.6843, -74.0481),
    "Pepe Sierra":        (4.6762, -74.0484),
    "Calle 106":          (4.6740, -74.0515),  
    "Calle 100":          (4.6840, -74.0577),  
    "Virrey":             (4.6653, -74.0561),
    "Calle 85":           (4.6610, -74.0569),
    "Héroes":             (4.6572, -74.0571),
    
    # Troncal Caracas (Norte a Sur)
    "Calle 76":           (4.6511, -74.0573),
    "Calle 72":           (4.6492, -74.0572),
    "Flores":             (4.6413, -74.0581),
    "Calle 63":           (4.6342, -74.0583),
    "Calle 57":           (4.6288, -74.0628),  
    "Marly":              (4.6192, -74.0643),
    "Calle 45":           (4.6113, -74.0644),
    "Avenida 39":         (4.6053, -74.0648),
    "Profamilia":         (4.5993, -74.0651),
    "Calle 26":           (4.6166, -74.0721),  
    "Calle 22":           (4.6110, -74.0728),  
    "Calle 19":           (4.6048, -74.0741),  
    "Av. Jiménez":        (4.5991, -74.0752),
    "Tercer Milenio":     (4.5931, -74.0761),
    "Hospital":           (4.5862, -74.0772),
    "Hortúa":             (4.5783, -74.0781),
    
    # Troncal Caracas Sur / Usme
    "Santa Lucía":        (4.5701, -74.1011),
    "Calle 40 Sur":       (4.5615, -74.1030), 
    "Portal Usme":        (4.4991, -74.1143),
    
    # Troncal Calle 26 (Avenida Eldorado)
    "Avenida Eldorado":   (4.6410, -74.0832),  
    "CAN":                (4.6413, -74.1043),
    "El Tiempo / Maloka": (4.6302, -74.0992),
    
    # Troncal NQS / Autopista Sur
    "Sena":               (4.5956, -74.1123),  
    "NQS Calle 30 Sur":   (4.5892, -74.1165),  
    "NQS Calle 38 Sur":   (4.5810, -74.1221),  
    "General Santander":  (4.5873, -74.1081),
    "Portal Sur":         (4.5969, -74.1694), 
    
    # Troncal Américas / Zona Centro-Occidente
    "De La Sabana":       (4.6053, -74.0812),  
    "Ricaurte":           (4.6032, -74.0915),  
    "Paloquemao":         (4.6110, -74.0898), 
    "Banderas":           (4.6175, -74.1538),  
    "Portal Américas":    (4.6283, -74.1552)
}


REGLAS_CONEXION = [
    # TRONCAL NORTE (Portal Norte → Héroes)
    ("Portal Norte",       "Toberín",             1.50),
    ("Toberín",            "Calle 161",           0.65),
    ("Calle 161",          "Mazurén",             0.90),
    ("Mazurén",            "Calle 146",           0.75),
    ("Calle 146",          "Calle 142",           0.50),
    ("Calle 142",          "Calle 134",           1.00),
    ("Calle 134",          "Alcalá",              0.60),
    ("Alcalá",             "Prado",               0.85),
    ("Prado",              "Calle 127",           0.70),
    ("Calle 127",          "Pepe Sierra",         0.90),
    ("Pepe Sierra",        "Calle 106",           1.10),
    ("Calle 106",          "Calle 100",           0.75),
    ("Calle 100",          "Virrey",              1.20),
    ("Virrey",             "Calle 85",            0.70),
    ("Calle 85",           "Héroes",              0.65),

    # TRONCAL CARACAS (Héroes → Tercer Milenio)
    ("Héroes",             "Calle 76",            0.85),
    ("Calle 76",           "Calle 72",            0.45),
    ("Calle 72",           "Flores",              0.65),
    ("Flores",             "Calle 63",            0.60),
    ("Calle 63",           "Calle 57",            0.55),
    ("Calle 57",           "Marly",               0.65),
    ("Marly",              "Calle 45",            0.60),
    ("Calle 45",           "Avenida 39",          0.55),
    ("Avenida 39",         "Profamilia",          0.65),
    ("Profamilia",         "Calle 26",            0.60),
    ("Calle 26",           "Calle 22",            0.45),
    ("Calle 22",           "Calle 19",            0.40),
    ("Calle 19",           "Av. Jiménez",         0.50),
    ("Av. Jiménez",        "Tercer Milenio",      0.65),

    # TRONCAL CARACAS SUR (Tercer Milenio → Portal Usme)
    ("Tercer Milenio",     "Hospital",            0.75),
    ("Hospital",           "Hortúa",              0.80),
    ("Hortúa",             "Santa Lucía",         3.20), 
    ("Santa Lucía",        "Calle 40 Sur",        0.90),
    ("Calle 40 Sur",       "Portal Usme",         6.10),

    # TRONCAL CALLE 26 / ELDORADO (Centro → Occidente)
    ("Calle 26",           "Avenida Eldorado",    1.30), 
    ("Avenida Eldorado",   "CAN",                 2.40),
    ("CAN",                "El Tiempo / Maloka",  1.90),

    # TRONCAL NQS CENTRAL Y SUR (Conexión Norte a Sur)
    ("Calle 76",           "Paloquemao",          4.20), 
    ("Paloquemao",         "Ricaurte",            1.10), 
    ("Ricaurte",           "Sena",                2.10), 
    ("Sena",               "NQS Calle 30 Sur",    1.10),
    ("NQS Calle 30 Sur",   "NQS Calle 38 Sur",    1.00),
    ("NQS Calle 38 Sur",   "General Santander",   1.30),
    ("General Santander",  "Portal Sur",          4.80),

    # TRONCAL AMÉRICAS (Oriente → Occidente)
    ("Av. Jiménez",        "De La Sabana",        0.75),
    ("De La Sabana",       "Ricaurte",            0.95), 
    ("Ricaurte",           "Banderas",            6.20),
    ("Banderas",           "Portal Américas",     3.90),

    # INTERCAMBIADORES DE TRONCAL (Estaciones de transferencia)
    ("Avenida Eldorado",   "Paloquemao",          1.80), 
    ("Ricaurte",           "Paloquemao",          1.10)  
]

RUTAS_DISPONIBLES = {
    ("Portal Norte", "Portal Sur"): [
        {
            "codigo":       "Ruta Fácil 4",
            "tipo":         "corriente",
            "paradas":      "todas las estaciones del trayecto",
            "descripcion":  "Ideal si necesitas bajarte en alguna estación intermedia.",
        },
        {
            "codigo":       "Expreso G12",
            "tipo":         "expreso",
            "paradas":      "14 estaciones clave",
            "descripcion":  "Opción más rápida si tu destino es directamente Portal Sur.",
        },
    ],
    ("Portal Norte", "Portal Usme"): [
        {
            "codigo":       "Expreso H75",
            "tipo":         "expreso",
            "paradas":      "16 estaciones",
            "descripcion":  "Conecta directamente el norte con Usme optimizando el tiempo.",
        },
        {
            "codigo":       "Expreso H27",
            "tipo":         "expreso",
            "paradas":      "13 estaciones estratégicas",
            "descripcion":  "Opera en horarios específicos, más rápido pero menos frecuente.",
        },
    ],
    ("Calle 100", "Av. Jiménez"): [
        {
            "codigo":       "Expreso J74",
            "tipo":         "expreso",
            "paradas":      "7 paradas",
            "descripcion":  "Lleva directo desde Calle 100 hasta Aguas/Universidades (contigua a Av. Jiménez).",
        },
        {
            "codigo":       "Ruta Fácil 8",
            "tipo":         "corriente",
            "paradas":      "todas las estaciones de la Troncal Caracas",
            "descripcion":  "Útil si necesitas bajarte en algún punto intermedio.",
        },
    ],
    ("Héroes", "Portal Américas"): [
        {
            "codigo":       "Expreso F28",
            "tipo":         "expreso",
            "paradas":      "11 paradas",
            "descripcion":  "Ruta directa de norte a suroccidente por la NQS y las Américas.",
        },
    ],
    ("Toberín", "General Santander"): [
        {
            "codigo":       "Expreso G11",
            "tipo":         "expreso",
            "paradas":      "16 paradas estratégicas",
            "descripcion":  "Conecta el extremo norte con la NQS sur de forma directa.",
        },
    ],
}


# HEURÍSTICA: distancia Haversine (admisible)


def haversine_km(est_a, est_b):
    if est_a not in COORDENADAS or est_b not in COORDENADAS:
        return 0.0
    lat1, lon1 = COORDENADAS[est_a]
    lat2, lon2 = COORDENADAS[est_b]
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat/2)**2
         + math.cos(math.radians(lat1))
         * math.cos(math.radians(lat2))
         * math.sin(dlon/2)**2)
    return R * 2 * math.asin(math.sqrt(a))


# CONSTRUCCIÓN DEL GRAFO

def construir_grafo(reglas):
    grafo = {}
    for origen, destino, costo in reglas:
        grafo.setdefault(origen, {})[destino] = costo
        grafo.setdefault(destino, {})[origen] = costo
    return grafo

# ALGORITMO A*

def buscar_ruta_astar(grafo, inicio, objetivo):
    if inicio not in grafo or objetivo not in grafo:
        return None, None, []

    cola = [(0.0, 0.0, inicio, [inicio])]
    visitados = {}
    nodos_explorados = []

    while cola:
        f, g, actual, camino = heapq.heappop(cola)
        nodos_explorados.append(actual)

        if actual == objetivo:
            return round(g, 3), camino, nodos_explorados

        if actual in visitados and visitados[actual] <= g:
            continue
        visitados[actual] = g

        for vecino, dist in grafo[actual].items():
            g_nuevo = g + dist
            h_nuevo = haversine_km(vecino, objetivo)
            heapq.heappush(cola, (g_nuevo + h_nuevo, g_nuevo, vecino, camino + [vecino]))

    return None, None, nodos_explorados


# INTERFAZ


def mostrar_ruta(inicio, objetivo, grafo):
    print("\n" + "=" * 65)
    print(f"  RUTA: {inicio}  →  {objetivo}")
    print("=" * 65)

    dist, camino, explorados = buscar_ruta_astar(grafo, inicio, objetivo)

    if camino is None:
        print("  ✗ No se encontró ruta.")
        return None, None

    print(f"\n  Estaciones recorridas ({len(camino)}):")
    for i, est in enumerate(camino):
        if i == 0:
            print(f"     INICIO  → {est}")
        elif i == len(camino) - 1:
            print(f"     DESTINO → {est}")
        else:
            print(f"    {i:>2}.       {est}")

    print(f"\n   Distancia total      : {dist} km")
    print(f"   Nodos explorados A* : {len(explorados)}")

    # Mostrar rutas disponibles si existen en la base de conocimiento
    clave = (inicio, objetivo)
    if clave in RUTAS_DISPONIBLES:
        rutas = RUTAS_DISPONIBLES[clave]
        print(f"\n    Rutas disponibles para este trayecto:")
        recomendada = True
        for r in rutas:
            etiqueta = " RECOMENDADA" if recomendada else " ALTERNATIVA"
            print(f"\n    {etiqueta}: {r['codigo']} ({r['tipo'].upper()})")
            print(f"    Paradas : {r['paradas']}")
            print(f"    Nota    : {r['descripcion']}")
            recomendada = False
    else:
        print("\n  ℹ  Rutas específicas no registradas para este trayecto.")
        print("     Consulta el sistema SITP o la app de TransMilenio.")

    print("=" * 65)
    return dist, camino


def listar_estaciones(grafo):
    estaciones = sorted(grafo.keys())
    print("\n📍 Estaciones disponibles:")
    for i, est in enumerate(estaciones, 1):
        print(f"   {i:>2}. {est}")
    return estaciones


def modo_interactivo(grafo):
    print("\n" + "=" * 65)
    print("  SISTEMA DE RUTAS TRANSMILENIO — Algoritmo A*")
    print("=" * 65)
    estaciones = listar_estaciones(grafo)

    while True:
        print("\nNúmero de estación ORIGEN (0 para salir):")
        try:
            op_o = int(input("  > "))
        except ValueError:
            continue
        if op_o == 0:
            break
        print("Número de estación DESTINO:")
        try:
            op_d = int(input("  > "))
        except ValueError:
            continue
        if not (1 <= op_o <= len(estaciones) and 1 <= op_d <= len(estaciones)):
            print("  Número fuera de rango.")
            continue
        mostrar_ruta(estaciones[op_o - 1], estaciones[op_d - 1], grafo)
        print("\n¿Otra ruta? (s/n): ", end="")
        if input().strip().lower() != "s":
            break


def ejecutar_pruebas(grafo):
    pruebas = [
        ("Portal Norte",  "Portal Sur"),
        ("Portal Norte",  "Portal Usme"),
        ("Calle 100",     "Av. Jiménez"),
        ("Héroes",        "Portal Américas"),
        ("Toberín",       "General Santander"),
    ]
    print("\n" + "=" * 65)
    print("  PRUEBAS PREDEFINIDAS")
    print("=" * 65)
    resultados = []
    for inicio, objetivo in pruebas:
        dist, camino = mostrar_ruta(inicio, objetivo, grafo)[:2]
        resultados.append({
            "origen": inicio, "destino": objetivo,
            "distancia_km": dist,
            "paradas": len(camino) if camino else 0,
            "ruta": camino or []
        })
    return resultados

# MAIN
if __name__ == "__main__":
    grafo = construir_grafo(REGLAS_CONEXION)

    print("\n¿Qué desea hacer?")
    print("  1. Ejecutar pruebas predefinidas")
    print("  2. Modo interactivo")
    opcion = input("\n  Opción (1/2): ").strip()

    if opcion == "1":
        ejecutar_pruebas(grafo)
    else:
        modo_interactivo(grafo)