class VotacionConfig:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(VotacionConfig, cls).__new__(cls)
            # Configuración global y parámetros de seguridad del proceso electoral
            cls._instancia.eleccion_activa = "Elecciones Presidenciales 2026"
            cls._instancia.intentos_maximos_login = 3
            cls._instancia.sistema_cifrado_activo = True
        return cls._instancia

    def get_eleccion_activa(self) -> str:
        return self._instancia.eleccion_activa

    def get_intentos_maximos(self) -> int:
        return self._instancia.intentos_maximos_login

    def is_cifrado_activo(self) -> bool:
        return self._instancia.sistema_cifrado_activo


class SistemaLogin:
    def __init__(self):
        # Base de datos simulada de usuarios habilitados en el censo electoral
        self.censados = {
            "brayan.pabon": "uts2026*",
            "johan.jaimes": "voto_seguro*"
        }
        # Acceso a la instancia única del Singleton
        self.config = VotacionConfig() 

    def autenticar(self, usuario: str, contrasena: str) -> bool:
        print(f"--- [Proceso: {self.config.get_eleccion_activa()}] ---")
        print(f"Protocolo de cifrado activo: {self.config.is_cifrado_activo()}")
        
        if usuario in self.censados and self.censados[usuario] == contrasena:
            print(f"Acceso concedido. Bienvenido al sistema, votante: {usuario}\n")
            return True
        else:
            print(f"Acceso denegado. Credenciales inválidas (Límite de intentos permitidos: {self.config.get_intentos_maximos()}).\n")
            return False


# --- PRUEBA DE EJECUCIÓN ---
if __name__ == "__main__":
    # Inicializamos el sistema de login
    login_sistema = SistemaLogin()
    
    # Intento fallido de inicio de sesión
    login_sistema.autenticar("brayan.pabon", "clave_incorrecta")
    
    # Intento exitoso de inicio de sesión
    login_sistema.autenticar("brayan.pabon", "uts2026*")
    
    # Verificación de que el Singleton mantiene la misma instancia global en otros componentes
    otra_configuracion = VotacionConfig()
    print("--- Verificación del Patrón Singleton ---")
    print(f"¿Es la misma instancia en memoria?: {login_sistema.config is otra_configuracion}")
    print(f"Elección consultada desde otra referencia: {otra_configuracion.get_eleccion_activa()}")