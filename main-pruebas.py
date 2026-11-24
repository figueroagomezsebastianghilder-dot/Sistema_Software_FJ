#Ghilder Figueroa
#Programacion

import logging

from clientes import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reservas import Reserva
from excepciones import (
    ErrorSistema,
    DatosInvalidosError,
    ReservaInvalidaError,
    ServicioNoDisponibleError
)

# Configuración del archivo de registros
logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Listas internas del sistema
clientes = []
servicios = []
reservas = []

def registrar_cliente(identificador, nombre, correo, telefono):
    """Registra un cliente en el sistema."""

    try:
        cliente = Cliente(
            identificador, nombre, correo, telefono
        )

        clientes.append(cliente)

        logging.info(f"Cliente registrado: {identificador}")

        print("Cliente registrado correctamente.")
        return cliente

    except (ValueError, AttributeError) as error:
        logging.exception("Error al registrar cliente")
        raise DatosInvalidosError(str(error)) from error

    except Exception as error:
        logging.exception("Error inesperado al registrar cliente")
        raise ErrorSistema("No fue posible registrar el cliente.") from error


def registrar_servicio(servicio):
    """Agrega un servicio a la lista interna."""

    try:
        if not servicio.activo:
            raise ValueError("El servicio está inactivo.")

        servicios.append(servicio)

        logging.info(f"Servicio registrado: {servicio.nombre}")

        print("Servicio registrado correctamente.")

    except Exception:
        logging.exception("Error al registrar servicio")
        raise


def crear_reserva(identificador, cliente, servicio, duracion):
    """Crea una reserva para un cliente."""

    try:
        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion
        )

        reservas.append(reserva)

        logging.info(f"Reserva creada: {identificador}")

        print("Reserva creada correctamente.")
        return reserva

    except Exception:
        logging.exception("Error al crear reserva")
        raise


def mostrar_resumen():
    """Muestra el estado general del sistema."""

    print("\n========== RESUMEN DEL SISTEMA ==========")

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas realizadas: {len(reservas)}")

    for reserva in reservas:
        print("\n" + reserva.mostrar_informacion())

    print("\n=========================================")


def ejecutar_pruebas():
    """Ejecuta diez operaciones para comprobar el sistema."""

    print("\nINICIANDO PRUEBAS DE SOFTWARE FJ\n")

    # OPERACIÓN 1: Registrar cliente válido
    print("\nOPERACIÓN 1: Registrar cliente")

    try:
        cliente1 = registrar_cliente(
            "C001",
            "Carlos Ramirez",
            "carlos@gmail.com",
            "3001234567"
        )
    except ErrorSistema as error:
        print(error)
        cliente1 = None

    # OPERACIÓN 2: Registrar otro cliente válido
    print("\nOPERACIÓN 2: Registrar segundo cliente")

    try:
        cliente2 = registrar_cliente(
            "C002",
            "Maria Lopez",
            "maria@gmail.com",
            "3107654321"
        )
    except ErrorSistema as error:
        print(error)
        cliente2 = None

    # OPERACIÓN 3: Registrar cliente con correo inválido
    print("\nOPERACIÓN 3: Registrar cliente inválido")

    try:
        registrar_cliente(
            "C003",
            "Pedro Gomez",
            "pedrocorreo",
            "3151234567"
        )
    except DatosInvalidosError as error:
        print("Error controlado:", error)

    # OPERACIÓN 4: Registrar servicio de salas
    print("\nOPERACIÓN 4: Crear servicio de salas")

    try:
        sala = ReservaSala("S001", "Sala de reuniones", 50000)
        registrar_servicio(sala)
    except Exception as error:
        print("Error:", error)
        sala = None

    # OPERACIÓN 5: Registrar alquiler de equipos
    print("\nOPERACIÓN 5: Crear servicio de equipos")

    try:
        equipo = AlquilerEquipo("S002", "Computador", 30000)
        registrar_servicio(equipo)
    except Exception as error:
        print("Error:", error)
        equipo = None

    # OPERACIÓN 6: Registrar asesoría especializada
    print("\nOPERACIÓN 6: Crear servicio de asesoría")

    try:
        asesoria = AsesoriaEspecializada(
            "S003", "Asesoría tecnológica", 80000
        )
        registrar_servicio(asesoria)
    except Exception as error:
        print("Error:", error)
        asesoria = None

    # OPERACIÓN 7: Intentar crear servicio con precio inválido
    print("\nOPERACIÓN 7: Crear servicio inválido")

    try:
        servicio_invalido = ReservaSala(
            "S004", "Sala inválida", -10000
        )
        registrar_servicio(servicio_invalido)

    except Exception as error:
        logging.exception("Servicio inválido detectado")
        print("Error controlado:", error)

    # OPERACIÓN 8: Crear y confirmar una reserva
    print("\nOPERACIÓN 8: Crear reserva exitosa")

    try:
        if cliente1 is None or sala is None:
            raise ReservaInvalidaError(
                "No existen los datos necesarios."
            )

        reserva1 = crear_reserva(
            "R001", cliente1, sala, 2
        )

        reserva1.confirmar()

    except Exception as error:
        logging.exception("Error en reserva exitosa")
        print("Error:", error)

    # OPERACIÓN 9: Intentar una reserva inválida
    print("\nOPERACIÓN 9: Crear reserva inválida")

    try:
        crear_reserva(
            "R002", cliente1, sala, -3
        )

    except Exception as error:
        logging.exception("Reserva inválida detectada")
        print("Error controlado:", error)

    # OPERACIÓN 10: Cancelar una reserva
    print("\nOPERACIÓN 10: Cancelar reserva")

    try:
        if 'reserva1' in locals():
            reserva1.cancelar()
            logging.info("Reserva R001 cancelada.")
        else:
            print("No existe una reserva para cancelar.")

    except Exception as error:
        logging.exception("Error al cancelar reserva")
        print("Error:", error)

    else:
        print("Proceso de pruebas finalizado.")

    finally:
        logging.info("Finalización de las diez operaciones.")
        print("\nFIN DE LAS PRUEBAS")

    # PRUEBA ADICIONAL: Variantes de cálculo de costos
    print("\nPRUEBA ADICIONAL: Cálculo de costos")

    try:
        costo_normal = sala.calcular_costo_varios(2)

        costo_descuento = sala.calcular_costo_varios(
            2, 10
        )

        costo_completo = sala.calcular_costo_varios(
            2, 10, 19
        )

        print(f"Costo normal: ${costo_normal:,.2f}")
        print(f"Costo con descuento: ${costo_descuento:,.2f}")
        print(f"Costo con descuento e impuesto: ${costo_completo:,.2f}")

    except Exception as error:
        logging.exception("Error en cálculo de costos")
        print("Error:", error)

    # PRUEBA ADICIONAL: Servicio no disponible
    print("\nPRUEBA ADICIONAL: Servicio no disponible")

    try:
        sala.disponible = False

        sala.calcular_costo(1)

    except ServicioNoDisponibleError as error:
        logging.exception("Servicio no disponible detectado")
        print("Error controlado:", error)

    finally:
        sala.disponible = True
        print("Estado del servicio restaurado.")

if __name__ == "__main__":
    ejecutar_pruebas()
    mostrar_resumen()