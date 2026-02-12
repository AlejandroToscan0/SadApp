"""
PATRÓN DE COMPORTAMIENTO: OBSERVER

Define una relación uno-a-muchos entre objetos tales que cuando uno de ellos 
cambia de estado, notifica este cambio a todos los dependientes automáticamente.

Permite que múltiples observadores se suscriban a eventos del sistema de análisis.
"""

from abc import ABC, abstractmethod


class ObservadorAnalisis(ABC):
    """
    Interfaz abstracta para observadores del sistema de análisis.
    Define el contrato que deben cumplir todos los observadores.
    """
    
    @abstractmethod
    def actualizar(self, evento: str, resultado: dict) -> None:
        """
        Llamado cuando ocurre un evento en el sistema.
        
        Args:
            evento: Tipo de evento ('analisis_completado', 'riesgo_detectado', etc.)
            resultado: Diccionario con datos del resultado del análisis
        """
        pass


class GestorObservadores:
    """
    Gestor centralizado de observadores.
    Permite registrar/desregistrar observadores y notificarlos de eventos.
    """
    
    def __init__(self):
        self._observadores = []
    
    def registrar(self, observador: ObservadorAnalisis) -> None:
        """Registra un nuevo observador."""
        if observador not in self._observadores:
            self._observadores.append(observador)
            print(f"✓ Observador registrado: {observador.__class__.__name__}")
    
    def desregistrar(self, observador: ObservadorAnalisis) -> None:
        """Desregistra un observador."""
        if observador in self._observadores:
            self._observadores.remove(observador)
            print(f"✗ Observador desregistrado: {observador.__class__.__name__}")
    
    def notificar(self, evento: str, resultado: dict) -> None:
        """
        Notifica a todos los observadores registrados.
        
        Args:
            evento: Tipo de evento
            resultado: Datos del resultado
        """
        for observador in self._observadores:
            try:
                observador.actualizar(evento, resultado)
            except Exception as e:
                print(f"⚠️ Error notificando {observador.__class__.__name__}: {e}")
    
    def limpiar(self) -> None:
        """Limpia todos los observadores registrados."""
        self._observadores.clear()
