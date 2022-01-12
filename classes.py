from abc import ABC, abstractmethod


class Banco:
    def __init__(self):
        self.__contas = {}
        self.__clientes = []

    @property
    def conta(self) -> dict:
        return self.__contas

    def add_conta(self, num_conta: str, saldo: float):
        self.__contas[num_conta] = saldo

    def remove_conta(self, num_conta: str):
        if num_conta in self.__contas:
            del self.__contas[num_conta]

    @property
    def clientes(self):
        return self.__clientes

    def add_cliente(self, cliente):
        self.__clientes.append(cliente)

    def remove_cliente(self, cliente):
        self.__clientes.remove(cliente)




class Pessoa(ABC):
    def __init__(self, __nome, __idade):
        self.__nome = __nome
        self.__idade = __idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @idade.setter
    def idade(self, idade: int) -> None:
        self.__idade = idade


class Cliente(Pessoa):
    def __init__(self, __nome: str, __idade: int, __contas: dict):
        super().__init__(__nome, __idade)
        self.__contas = __contas

    @property
    def conta(self) -> dict:
        return self.__contas

    def add_conta(self, num_conta: str, saldo: float):
        self.__contas[num_conta] = saldo

    def remove_conta(self, num_conta: str):
        if num_conta in self.__contas:
            del self.__contas[num_conta]


class Conta:
    __num_agencia: str = "0001"

    def __init__(self, __num_conta: str, __saldo: float):
        self.__num_conta = __num_conta
        self.__saldo = __saldo

    @property
    def num_agencia(self):
        return self.__num_agencia

    @property
    def num_conta(self):
        return self.__num_conta

    @property
    def saldo(self):
        return self.__saldo

    @abstractmethod
    def sacar(self, quantia: float):
        pass

    def depositar(self, quantia: float):
        if quantia <= 0:
            return
        self.__saldo += quantia




class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass

