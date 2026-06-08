import time

# Base de datos simulada
BASE_DATOS = {
    "1342": {"nombre": "Juan Lopez", "dias_disponibles": 14},
    "1782": {"nombre": "Ana Díaz", "dias_disponibles": 7},
    "1068": {"nombre": "Carlos Gonzalez", "dias_disponibles": 0}
}

def iniciar_simulador():
    print("SISTEMA DE GESTIÓN DE VACACIONES")
    print("Legajos registrados para la prueba: 1342, 1782, 1068")
    print("Escriba salir para terminar el programa.\n")

    estado = "INICIO"
    legajo_activo = None

    while True:

        # Solicitar legajo
        if estado == "INICIO":
            print("[Bot]: ¡Hola! Bienvenido al asistente de Recursos Humanos. Por favor, ingrese su número de legajo para comenzar:")
            entrada = input("[Empleado]: ").strip()

            if entrada.lower() == "salir":
                break

            if entrada in BASE_DATOS:
                legajo_activo = entrada
                print(f"[Bot]: Legajo validado. Bienvenido/a {BASE_DATOS[legajo_activo]['nombre']}.")
                estado = "ESPERANDO_DIAS"
            else:
                print("[Bot]: El legajo no existe. Por favor, intente con 1068, 1342 o 1782.")

        # Solicitar días
        elif estado == "ESPERANDO_DIAS":
            saldo = BASE_DATOS[legajo_activo]["dias_disponibles"]

            if saldo == 0:
                print("[Bot]: No posee días disponibles para solicitar vacaciones.")
                estado = "INICIO"
                legajo_activo = None
                continue

            print(f"[Bot]: Usted tiene {saldo} días disponibles. ¿Cuántos días desea solicitar?")
            dias_entrada = input("[Empleado]: ").strip()

            if dias_entrada.lower() == "salir":
                break

            # Validar número entero positivo
            if not dias_entrada.isdigit():
                print("[Bot]: Por favor, ingrese solo números enteros positivos.")
                continue

            dias_solicitados = int(dias_entrada)

            if dias_solicitados <= 0:
                print("[Bot]: Debe solicitar al menos 1 día.")
                continue

            print("[Bot]: Verificando saldo...")
            time.sleep(1)

            # Aprobar o rechazar
            if dias_solicitados <= saldo:
                BASE_DATOS[legajo_activo]["dias_disponibles"] -= dias_solicitados
                print(f"[Bot]: SOLICITUD APROBADA. Su nuevo saldo es {BASE_DATOS[legajo_activo]['dias_disponibles']} días.")
            else:
                print(f"[Bot]: SOLICITUD RECHAZADA. No tiene saldo suficiente para pedir {dias_solicitados} días.")

            print("\n¿Desea realizar otra consulta?")
            estado = "INICIO"
            legajo_activo = None

if __name__ == "__main__":
    iniciar_simulador()