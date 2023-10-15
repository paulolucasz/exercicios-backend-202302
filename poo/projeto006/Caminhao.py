import Veiculo

class Caminhao(Veiculo.Veiculo):
    def __init__(self, chassi, marca, modelo, ano, carroceria, numero_rodas, capacidade_carga):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Caminhao")
        self.carroceria = carroceria
        self.numero_rodas = numero_rodas
        self.capacidade_carga = capacidade_carga
        self.marcha = 8
        self.combustivel = 0

    def ligar(self):
        return self.marcha

    def desligar(self):
        self.marcha = 8

    def abastecer(self, quantidade):
        self.combustivel += quantidade

    def acao(self):
        return "O caminhão está fazendo um som de motor do motor diesel."

""" Aqui começa o teste """

Veiculo_de_carga = Caminhao('888ABC123XYZ', 'Mercedes-Benz', 'Actros', '2023', 'Baú', 10, 25000)

print(Veiculo_de_carga.get_tipo())
print(Veiculo_de_carga.carroceria)
print(Veiculo_de_carga.numero_rodas)
print(Veiculo_de_carga.capacidade_carga)
print(Veiculo_de_carga.ligar())

Veiculo_de_carga.abastecer(100)
print(Veiculo_de_carga.combustivel)

