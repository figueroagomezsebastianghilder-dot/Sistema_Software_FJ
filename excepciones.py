#Ghilder Figueroa
#Programacion

class ErrorSistema(Exception):
    """Excepción general del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se genera cuando los datos ingresados no son válidos."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva presenta errores."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando se intenta realizar una operación no permitida."""
    pass
