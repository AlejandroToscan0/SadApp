from core.interfaces.RecomendacionFactory import RecomendacionFactory
from productos.recomendaciones.RecomendacionNingunProblema import RecomendacionNingunProblema

class RecomendacionNingunProblemaFactory(RecomendacionFactory):
    def crear_recomendacion(self):
        return RecomendacionNingunProblema()
