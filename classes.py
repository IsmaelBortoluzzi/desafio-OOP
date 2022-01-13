from abc import ABC, abstractmethod


class Banco:
    def __init__(self, __contas, __clientes):
        self.__contas = __contas
        self.__clientes = __clientes

    @property
    def contas(self) -> dict:
        return self.__contas

    def add_conta(self, conta):
        self.__contas[conta.num_conta] = conta

    def remove_conta(self, num_conta: str):
        if num_conta in self.__contas:
            del self.__contas[num_conta]

    @property
    def clientes(self):
        return self.__clientes

    def add_cliente(self, cliente):
        self.__clientes[cliente.nome] = cliente

    def remove_cliente(self, cliente):
        del self.__clientes[cliente.nome]


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

    def add_conta(self, conta):
        self.__contas[conta.num_conta] = conta

    def remove_conta(self, num_conta: str):
        if num_conta in self.__contas:
            del self.__contas[num_conta]


class Conta(ABC):
    __num_agencia: str = "0001"

    def __init__(self, __num_conta: str, _saldo: float):
        self.__num_conta = __num_conta
        self._saldo = _saldo

    @property
    def num_agencia(self):
        return self.__num_agencia

    @property
    def num_conta(self):
        return self.__num_conta

    @property
    def saldo(self):
        return self._saldo

    @abstractmethod
    def sacar(self, quantia: float):
        pass

    def depositar(self, quantia: float):
        if quantia <= 0:
            return
        self._saldo += quantia


class ContaCorrente(Conta):
    def __init__(self, __num_conta: str, _saldo: float, __limite=500):
        super().__init__(__num_conta, _saldo)
        self.__limite = __limite

    def sacar(self, quantia: float):
        if quantia > (self._saldo + self.__limite):
            return
        self._saldo -= quantia


class ContaPoupanca(Conta):
    def __init__(self, __num_conta: str, _saldo: float):
        super().__init__(__num_conta, _saldo)

    def sacar(self, quantia: float):
        if quantia > self._saldo:
            return
        self._saldo -= quantia
