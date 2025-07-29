casos = []

def guardar_caso(caso):
    casos.append(caso)
    print(f"Caso {caso.id} guardado com sucesso!")

def listar_casos_por_autor(autor):
    return [caso for caso in casos if caso.autor == autor]
