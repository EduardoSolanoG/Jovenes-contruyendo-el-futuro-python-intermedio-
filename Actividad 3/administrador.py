from usuario import Usuario
from decoradores import registrar_accion
from dataclasses import dataclass, field
from typing import List

@dataclass
class Administrador(Usuario):
    """
    Clase Administrador que hereda de Usuario.
    Representa a un usuario con permisos administrativos.
    """
    permisos: List[str] = field(default_factory=lambda: ["agregar_producto", "ver_ventas", "gestionar_usuarios"])

    @registrar_accion("Se mostro la informaciode un administrador")
    def mostrar_info(self) -> str:
        """
        Implementacion del metodo abstracto de Usuario.
        Retorna la informacion del administrador
        """
        permisos_str = ", ".join(self.permisos) if self.permisos else "Sin permisos"
        return (
            f"---Administrador---\n"
            f"Nombre: {self.nombre}\n"
            f"Email: {self.email}\n"
            f"Permisos: {permisos_str}\n"
        )

    @registrar_accion("Administrador inicio sesion en el sistema")
    def autenticar(self, token: str) -> bool:
        """
        Autenticacion con token de administrador.
        Sobrescribe el metodo de Usuario para simular autenticacion mas estricta
        """
        return token == "ADMIN123"  # En un sistema real seria una contraseña en hash o DB

    @registrar_accion("Administrador actualizo permisos")
    def agregar_permiso(self, permiso: str) -> None:
        """
        Agrega un nuevo permiso al administrador.
        """
        if permiso not in self.permisos:
            self.permisos.append(permiso)
            print(f"Permiso ´{permiso}´agregado al administrador {self.nombre}.")
        else:
            print(f"El permiso ´{permiso}´ya existe para este administrador.")

    def to_dict(self) -> dict:
        """
        Extiende el metodo de Usuario para incluir permisos del administrador.
        """
        data = super().to_dict()
        data.update({"permisos": self.permisos})
        return data
