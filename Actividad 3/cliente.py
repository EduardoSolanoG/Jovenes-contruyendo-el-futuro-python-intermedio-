from usuario import Usuario
from decoradores import registrar_accion
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Cliente(Usuario):
