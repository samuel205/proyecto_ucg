from strategies.stress_strategy import EstrategiaStress
from strategies.academic_strategy import EstrategiaAcademica
from strategies.attendance_strategy import EstrategiaAsistencia


class FabricaAnalisis:

    @staticmethod
    def crear(tipo):

        if tipo == "stress":
            return EstrategiaStress()

        elif tipo == "academico":
            return EstrategiaAcademica()

        elif tipo == "asistencia":
            return EstrategiaAsistencia()

        else:
            raise ValueError("Tipo de análisis no válido")
