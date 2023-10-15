import Veiculo
class Aviao ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, capacidade, finalidade ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Aviao")
        self.capacidade = capacidade
        self.finalidade = finalidade
        self.marcha = 0
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 0
    def acelerar(self, valor):
        self.marcha += valor

""" Aqui comeca o teste """

Aeronave = Aviao

Aeronave = Aviao("Vascao", "Boeing", "747", 1998, 1000, "Comercial")

print(Aeronave.get_tipo())
print(Aeronave.capacidade)
print(Aeronave.finalidade)
print(Aeronave.ligar())

Aeronave.acelerar(777)
print(Aeronave.ligar())
