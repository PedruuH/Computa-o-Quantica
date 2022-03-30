# Proposta para isolar o token dos outros programas
# É necessário rodar apenas uma vez, ou quando não tiver conexão com a IBM
from qiskit import IBMQ

apitoken = "957a5cbcbafe6ead2d4e74a4b9fdff4ee4ceb8ef1113d224380af290fdc7660bb19e224256fda83e80d129347614f6b9915f6688adfe8d15f8719817bf904c85"

if __name__ == "__main__":
    IBMQ.save_account(apitoken)
