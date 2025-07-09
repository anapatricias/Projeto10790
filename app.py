from Models.Caso_Clinico import CasoClinico

# Exemplo de caso clínico
caso = CasoClinico(
    id=1,
    titulo="Tumor raro",
    descricao="Paciente com sintomas incomuns associados a um tumor raro.",
    autor="Dra. Andreia Silva",
    data="2025-07-09"
)

print(caso)
