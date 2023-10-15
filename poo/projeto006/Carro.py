import Veiculo
class Carro ( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoCarro ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Carro")
        self.potencia = potencia
        self.tipoCarro = tipoCarro
        self.marcha = 5
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 5
    def acelerar(self, velocidade):
        if self.marcha == 0:
            return "O carro está desligado. Ligue-o primeiro."
        else:
            return f"Acelerando o carro a {velocidade} km/h."

    def acao(self):
        return "O carro está fazendo um som de motor."

""" Aqui comeca o teste """
CarroNovo = Carro('8885AZKG01Z12A33921312', 'JAC', 'J3', '2022', 2.0, 'HATCH')
print(CarroNovo.get_tipo())
print(CarroNovo.potencia)
print(CarroNovo.tipoCarro)
print(CarroNovo.ligar())
print(CarroNovo.acelerar(60))