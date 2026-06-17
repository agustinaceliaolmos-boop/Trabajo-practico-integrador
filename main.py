import csv

ARCHIVO = "paises.csv"

# =========================
# CARGA Y GUARDADO DE DATOS
# =========================

def cargar_paises():
    paises = []
    try:
        with open(ARCHIVO, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except ValueError:
                    print("⚠ Error de formato en un registro.")
    except FileNotFoundError:
        print("⚠ Archivo CSV no encontrado. Se creará al guardar.")
    return paises


def guardar_paises(paises):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)


# =========================
# MOSTRAR PAÍS FORMATEADO
# =========================

def mostrar_pais(pais):
    print(f"""
País: {pais['nombre']}
  🌍 Continente: {pais['continente']}
  👥 Población: {pais['poblacion']}
  📐 Superficie: {pais['superficie']} km²
""")


# =========================
# FUNCIONALIDADES
# =========================

def agregar_pais(paises):
    nombre = input("Nombre: ").strip()
    continente = input("Continente: ").strip()

    if not nombre or not continente:
        print("❌ No se permiten campos vacíos.")
        return

    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie: "))
    except ValueError:
        print("❌ Datos numéricos inválidos.")
        return

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })

    print("✅ País agregado correctamente.")
    mostrar_pais(paises[-1])


def actualizar_pais(paises):
    nombre = input("Nombre del país a actualizar: ").lower()

    for pais in paises:
        if pais["nombre"].lower() == nombre:
            try:
                pais["poblacion"] = int(input("Nueva población: "))
                pais["superficie"] = int(input("Nueva superficie: "))
                print("✅ País actualizado:")
                mostrar_pais(pais)
                return
            except ValueError:
                print("❌ Valores inválidos.")
                return

    print("❌ País no encontrado.")


def buscar_pais(paises):
    termino = input("Buscar país: ").lower()
    resultados = [p for p in paises if termino in p["nombre"].lower()]

    if resultados:
        for p in resultados:
            mostrar_pais(p)
    else:
        print("❌ No se encontraron países.")


def filtrar_por_continente(paises):
    cont = input("Continente: ").lower()
    resultados = [p for p in paises if p["continente"].lower() == cont]

    if resultados:
        for p in resultados:
            mostrar_pais(p)
    else:
        print("❌ Sin resultados.")


def ordenar_paises(paises):
    print("""
1. Nombre
2. Población
3. Superficie
""")
    opcion = input("Elegir criterio: ")

    if opcion == "1":
        paises.sort(key=lambda x: x["nombre"])
    elif opcion == "2":
        paises.sort(key=lambda x: x["poblacion"])
    elif opcion == "3":
        paises.sort(key=lambda x: x["superficie"])
    else:
        print("❌ Opción inválida.")
        return

    for p in paises:
        mostrar_pais(p)


def estadisticas(paises):
    if not paises:
        print("❌ No hay datos.")
        return

    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])

    promedio_pob = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("📊 ESTADÍSTICAS GENERALES\n")

    print("🌍 País con mayor población:")
    mostrar_pais(mayor)

    print("🌍 País con menor población:")
    mostrar_pais(menor)

    print(f"📊 Promedio población: {round(promedio_pob, 2)}")
    print(f"📐 Promedio superficie: {round(promedio_sup, 2)} km²")

    conteo = {}
    for p in paises:
        cont = p["continente"]
        conteo[cont] = conteo.get(cont, 0) + 1

    print("\n📌 Países por continente:")
    for cont, cantidad in conteo.items():
        print(f"  {cont}: {cantidad}")


# =========================
# MENÚ PRINCIPAL
# =========================

def menu():
    paises = cargar_paises()

    while True:
        print("""
=========================
   GESTIÓN DE PAÍSES
=========================
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar por continente
5. Ordenar países
6. Estadísticas
7. Guardar y salir
""")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_por_continente(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            estadisticas(paises)
        elif opcion == "7":
            guardar_paises(paises)
            print("💾 Datos guardados. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")


menu()