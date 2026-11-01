
import os
import platform
import getpass
import socket
import psutil
from datetime import datetime


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def formatar_bytes(valor):
    gb = valor / (1024 ** 3)
    return f"{gb:.2f} GB"


def obter_informacoes_sistema():
    return {
        "Computador": socket.gethostname(),
        "Usuario": getpass.getuser(),
        "Sistema operacional": platform.system(),
        "Versao": platform.version(),
        "Arquitetura": platform.machine(),
        "Processador": platform.processor(),
        "Python": platform.python_version()
    }


def mostrar_informacoes():
    print("\n=== INFORMACOES DO SISTEMA ===\n")

    informacoes = obter_informacoes_sistema()

    for nome, valor in informacoes.items():
        print(f"{nome}: {valor}")


def obter_informacoes_ram():
    memoria = psutil.virtual_memory()

    return {
        "Total": formatar_bytes(memoria.total),
        "Utilizada": formatar_bytes(memoria.used),
        "Disponivel": formatar_bytes(memoria.available),
        "Uso": f"{memoria.percent}%"
    }


def mostrar_ram():
    print("\n=== MEMORIA RAM ===\n")

    memoria = obter_informacoes_ram()

    for nome, valor in memoria.items():
        print(f"{nome}: {valor}")


def obter_informacoes_disco():
    unidades = []

    for particao in psutil.disk_partitions():
        try:
            uso = psutil.disk_usage(particao.mountpoint)

            unidades.append({
                "Unidade": particao.device,
                "Ponto de montagem": particao.mountpoint,
                "Total": formatar_bytes(uso.total),
                "Utilizado": formatar_bytes(uso.used),
                "Livre": formatar_bytes(uso.free),
                "Uso": f"{uso.percent}%"
            })

        except (PermissionError, OSError):
            continue

    return unidades


def mostrar_disco():
    print("\n=== ARMAZENAMENTO ===\n")

    unidades = obter_informacoes_disco()

    if not unidades:
        print("Nenhuma unidade disponivel para consulta.")
        return

    for unidade in unidades:
        for nome, valor in unidade.items():
            print(f"{nome}: {valor}")

        print("-" * 35)


def mostrar_cpu():
    print("\n=== MONITORAMENTO DA CPU ===\n")
    print("Coletando informacoes...")

    uso = psutil.cpu_percent(interval=1)
    nucleos = psutil.cpu_count(logical=True)

    print(f"Uso atual: {uso}%")
    print(f"Nucleos logicos: {nucleos}")


def obter_processos():
    processos = []

    for processo in psutil.process_iter(
        ["pid", "name", "memory_info"]
    ):
        try:
            memoria = processo.info["memory_info"]

            if memoria is None:
                continue

            processos.append({
                "PID": processo.info["pid"],
                "Nome": processo.info["name"] or "Desconhecido",
                "Memoria": memoria.rss
            })

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            continue

    processos.sort(
        key=lambda processo: processo["Memoria"],
        reverse=True
    )

    return processos[:10]


def mostrar_processos():
    print("\n=== PROCESSOS COM MAIOR USO DE MEMORIA ===\n")

    processos = obter_processos()

    if not processos:
        print("Nenhum processo encontrado.")
        return

    print(f"{'PID':<10}{'PROCESSO':<35}{'MEMORIA':>12}")
    print("-" * 57)

    for processo in processos:
        print(
            f"{processo['PID']:<10}"
            f"{processo['Nome'][:33]:<35}"
            f"{formatar_bytes(processo['Memoria']):>12}"
        )


def gerar_relatorio():
    print("\nGerando relatorio do sistema...")

    caminho = "relatorios"

    os.makedirs(caminho, exist_ok=True)

    horario = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    arquivo = os.path.join(caminho, f"relatorio_{horario}.txt")

    with open(arquivo, "w", encoding="utf-8") as relatorio:

        relatorio.write("PYTHON SYSTEM TOOL\n")
        relatorio.write("RELATORIO DE DIAGNOSTICO\n")
        relatorio.write("=" * 45 + "\n\n")

        relatorio.write("INFORMACOES DO SISTEMA\n")

        for nome, valor in obter_informacoes_sistema().items():
            relatorio.write(f"{nome}: {valor}\n")

        relatorio.write("\nMEMORIA RAM\n")

        for nome, valor in obter_informacoes_ram().items():
            relatorio.write(f"{nome}: {valor}\n")

        relatorio.write("\nARMAZENAMENTO\n")

        for unidade in obter_informacoes_disco():
            for nome, valor in unidade.items():
                relatorio.write(f"{nome}: {valor}\n")

            relatorio.write("-" * 35 + "\n")

        relatorio.write("\nMONITORAMENTO DA CPU\n")
        relatorio.write(
            f"Uso atual: {psutil.cpu_percent(interval=1)}%\n"
        )
        relatorio.write(
            f"Nucleos logicos: {psutil.cpu_count(logical=True)}\n"
        )

        relatorio.write("\nPROCESSOS COM MAIOR USO DE MEMORIA\n")

        for processo in obter_processos():
            relatorio.write(
                f"PID: {processo['PID']} | "
                f"Nome: {processo['Nome']} | "
                f"Memoria: {formatar_bytes(processo['Memoria'])}\n"
            )

        relatorio.write("\n")
        relatorio.write(
            f"Relatorio gerado em: {datetime.now()}\n"
        )

    print(f"\nRelatorio salvo em: {arquivo}")


def menu():
    while True:
        limpar_tela()

        print("=" * 48)
        print("              PYTHON SYSTEM TOOL")
        print("=" * 48)

        print("[1] Informacoes do computador")
        print("[2] Monitoramento da memoria RAM")
        print("[3] Informacoes de armazenamento")
        print("[4] Monitoramento da CPU")
        print("[5] Listar processos")
        print("[6] Gerar relatorio do sistema")
        print("[0] Sair")

        print("=" * 48)

        opcao = input("Selecione uma opcao: ").strip()

        if opcao == "1":
            mostrar_informacoes()

        elif opcao == "2":
            mostrar_ram()

        elif opcao == "3":
            mostrar_disco()

        elif opcao == "4":
            mostrar_cpu()

        elif opcao == "5":
            mostrar_processos()

        elif opcao == "6":
            gerar_relatorio()

        elif opcao == "0":
            print("\nEncerrando Python System Tool...")
            break

        else:
            print("\nOpcao invalida.")

        if opcao != "0":
            pausar()


if __name__ == "__main__":
    menu()
