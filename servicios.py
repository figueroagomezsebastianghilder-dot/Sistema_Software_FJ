#Ghilder Figueroa
#Programacion

from abc import abstractmethod
from entidades import Entidad
from excepciones import ServicioNoDisponibleError


class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios
    ofrecidos por Software FJ.
    """

    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = True

    def validar_parametros(self, duracion):
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        if not self.disponible or not self.activo:
            raise ServicioNoDisponibleError(
                f"El servicio {self.nombre} no está disponible."
            )

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir(self):
        pass

    def mostrar_informacion(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Identificador: {self.identificador}\n"
            f"Precio base: ${self.precio_base}\n"
            f"Disponible: {self.disponible}"
        )

    def calcular_costo_varios(self, duracion, *parametros):
        """
        Calcula costos utilizando diferentes parámetros:
        sin descuento, con descuento o con descuento e impuesto.
        """

        if len(parametros) == 0:
            return self.calcular_costo(duracion)

        elif len(parametros) == 1:
            return self.calcular_costo(
                duracion, descuento=parametros[0]
            )

        elif len(parametros) == 2:
            return self.calcular_costo(
                duracion,
                descuento=parametros[0],
                impuesto=parametros[1]
            )

        else:
            raise ValueError("Cantidad de parámetros no válida.")

class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise ValueError("Descuento e impuesto deben estar entre 0 y 100.")

        subtotal = self.precio_base * duracion
        valor_descuento = subtotal * descuento / 100
        valor_impuesto = (subtotal - valor_descuento) * impuesto / 100

        return subtotal - valor_descuento + valor_impuesto

    def describir(self):
        return "Reserva de salas para reuniones y eventos empresariales."


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnológicos."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise ValueError("Descuento e impuesto deben estar entre 0 y 100.")

        subtotal = self.precio_base * duracion
        valor_descuento = subtotal * descuento / 100
        valor_impuesto = (subtotal - valor_descuento) * impuesto / 100

        return subtotal - valor_descuento + valor_impuesto

    def describir(self):
        return "Alquiler de computadores y equipos tecnológicos."


class AsesoriaEspecializada(Servicio):
    """Servicio de asesorías especializadas."""

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise ValueError("Descuento e impuesto deben estar entre 0 y 100.")

        subtotal = self.precio_base * duracion
        valor_descuento = subtotal * descuento / 100
        valor_impuesto = (subtotal - valor_descuento) * impuesto / 100

        return subtotal - valor_descuento + valor_impuesto

    def describir(self):
        return "Asesorías profesionales en tecnología y sistemas."
