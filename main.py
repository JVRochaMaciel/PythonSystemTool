
import os
import platform
import getpass
import psutil
import socket


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_informacoes():
    print("\n=== INFORMACOES DO SISTEMA ===")
    print(f"Computador: {socket.gethostname()}")
    print(f"Usuario: {getpass.getuser()}")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print(f"Arquitetura: {platform.machine()}")
    print(f"Python: {platform.python_version()}")


def mostrar_ram():
    memoria = psutil.virtual_memory()

    print("\n=== MEMORIA RAM ===")
    print(f"Total: {memoria.total / (1024**3):.2f} GB")
    print(f"Em uso: {memoria.used / (1024**3):.2f} GB")
    print(f"Livre: {memoria.available / (1024**3):.2f} GB")
    print(f"Uso: {memoria.percent}%")


def mostrar_disco():
    disco = psutil.disk_usage(os.path.abspath(os.sep))

    print("\n=== DISCO PRINCIPAL ===")
    print(f"Total: {disco.total / (1024**3):.2f} GB")
    print(f"Usado: {disco.used / (1024**3):.2f} GB")
    print(f"Livre: {disco.free / (1024**3):.2f} GB")
    print(f"Uso: {disco.percent}%")


def menu():
    while True:
        limpar_tela()

        print("=" * 36)
        print("       PYTHON SYSTEM TOOL")
        print("=" * 36)
        print("[1] Informacoes do computador")
        print("[2] Verificar memoria RAM")
        print("[3] Verificar espaco em disco")
        print("[0] Sair")
        print("=" * 36)

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            mostrar_informacoes()
        elif opcao == "2":
            mostrar_ram()
        elif opcao == "3":
            mostrar_disco()
        elif opcao == "0":
            print("Encerrando ferramenta...")
            break
        else:
            print("Opcao invalida.")

        if opcao != "0":
            input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    menu()
