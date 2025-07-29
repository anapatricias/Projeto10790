import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.caso_clinico import CasoClinico
from controllers.casos_controller import guardar_caso, listar_casos_por_autor

def menu_investigador():
    nome = input("🔐 Nome do Investigador: ").strip()

    while True:
        print(f"\nBem-vindo, {nome}!")
        print("1. Criar novo caso clínico")
        print("2. Ver os meus casos clínicos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_caso(nome)
        elif opcao == "2":
            ver_casos(nome)
        elif opcao == "3":
            print("🔚 A terminar sessão...\n")
            break
        else:
            print("❌ Opção inválida.")

def criar_caso(autor):
    try:
        id = int(input("ID: "))
    except ValueError:
        print("ID tem de ser um número inteiro!")
        return
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data = input("Data (YYYY-MM-DD): ")

    caso = CasoClinico(id, titulo, descricao, autor, data)
    guardar_caso(caso)

def ver_casos(autor):
    casos = listar_casos_por_autor(autor)
    if not casos:
        print("⚠️ Nenhum caso encontrado.")
    else:
        for caso in casos:
            print(caso)

if __name__ == "__main__":
    menu_investigador()
