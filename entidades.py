#Ghilder Figueroa
#Programacion

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.
    """

    def __init__(self, identificador):
        self._identificador = identificador
        self._activo = True

    @property
    def identificador(self):
        return self._identificador

    @property
    def activo(self):
        return self._activo

    def desactivar(self):
        """Desactiva una entidad del sistema."""
        self._activo = False

    @abstractmethod
    def mostrar_informacion(self):
        """Método que deben implementar las clases hijas."""
        pass
