import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.caso_clinico import CasoClinico
from controllers.casos_controller import guardar_caso


# Criar um caso clínico 
caso = CasoClinico(
    id=1,
    titulo="Tumor raro",
    descricao="Paciente com sintomas incomuns associados a um tumor raro.",
    autor="Dra. Andreia Silva",
    data="2025-07-09"
)

print(caso)

# Guardar o caso 
guardar_caso(caso)
print("Caso clínico guardado com sucesso na base de dados!")
