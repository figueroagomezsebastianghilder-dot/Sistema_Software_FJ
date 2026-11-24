#Ghilder Figueroa
#Programacion

from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

    def __init__(self, identificador, cliente, servicio, duracion):
        if cliente is None:
            raise ReservaInvalidaError("Debe seleccionar un cliente.")

        if servicio is None:
            raise ReservaInvalidaError("Debe seleccionar un servicio.")

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaInvalidaError("La duración debe ser mayor que cero.")

        self.__identificador = identificador
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0

    @property
    def identificador(self):
        return self.__identificador

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            self.__costo = self.__servicio.calcular_costo(
                self.__duracion
            )

            self.__estado = "Confirmada"

            print(f"Reserva {self.__identificador} confirmada.")

        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible confirmar la reserva."
            ) from error

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya se encuentra cancelada."
            )

        self.__estado = "Cancelada"
        print(f"Reserva {self.__identificador} cancelada.")

    def procesar(self):
        """Procesa la reserva y controla posibles errores."""

        try:
            self.confirmar()

        except ReservaInvalidaError as error:
            print(f"Error al procesar la reserva: {error}")
            raise

        finally:
            print(
                f"Finalizó el procesamiento de la reserva "
                f"{self.__identificador}."
            )

    def mostrar_informacion(self):
        """Presenta los datos de la reserva."""

        return (
            f"Reserva: {self.__identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.2f}"
        )
