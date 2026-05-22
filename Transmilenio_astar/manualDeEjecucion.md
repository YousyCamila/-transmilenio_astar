# Instrucciones de Ejecución — Sistema de Rutas TransMilenio (Algoritmo A*)

## Requisitos previos

- Python 3.7 o superior instalado.
- Verificar la versión abriendo una terminal y escribiendo:

```bash
python --version
```

- No se requieren librerías externas. El programa usa únicamente `heapq` y `math`, incluidas por defecto en Python.

---

## Pasos para ejecutar

1. Guarda el archivo con extensión `.py`, por ejemplo: `transmilenio_astar.py`

2. Abre una terminal y navega hasta la carpeta donde lo guardaste:

```bash
cd ruta/a/tu/carpeta
```

3. Ejecuta el programa con:

```bash
python transmilenio_astar.py
```

4. El programa te preguntará qué deseas hacer:

- **Opción 1 — Pruebas predefinidas:** ejecuta automáticamente 5 rutas de ejemplo y muestra los resultados.
- **Opción 2 — Modo interactivo:** muestra la lista de estaciones disponibles y permite ingresar origen y destino manualmente.

---

## Ejemplo de uso en modo interactivo

```bash
Opción (1/2): 2

Número de estación ORIGEN (0 para salir):
  > 12
Número de estación DESTINO:
  > 35
```

El sistema devuelve:
- La ruta óptima calculada con A*
- La distancia total en kilómetros
- Las rutas de bus disponibles para ese trayecto (si están registradas)