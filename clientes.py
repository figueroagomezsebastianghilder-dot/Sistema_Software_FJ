#Ghilder figueroa
#Programacion

from entidades import Entidad


class Cliente(Entidad):
    """
    Representa un cliente registrado en Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):
        """Verifica que los datos del cliente sean correctos."""

        if not self.__nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if "@" not in self.__correo or "." not in self.__correo:
            raise ValueError("El correo electrónico no es válido.")

        if not self.__telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        if len(self.__telefono) < 7 or len(self.__telefono) > 15:
            raise ValueError("La longitud del teléfono no es válida.")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        """Muestra la información del cliente."""

        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}\n"
            f"Estado: {'Activo' if self.activo else 'Inactivo'}"
        )
