from peewee import *
import os

arq = 'universidade.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    nome = CharField()
    cpf = IntegerField()

    def __str__(self):
        return "O cliente " + self.nome + " possui CPF número: " + str(self.cpf)

class Agencia(BaseModel):
    nome = CharField()
    cnpj = IntegerField()

    def __str__(self):
        return "A agência " + self.nome + " possui CNPJ número: " + str(self.cnpj)

class Destino(BaseModel):
    nome = CharField()
    localizacao = CharField()

    def __str__(self):
        return "O destino será: " + self.nome + " localizado no país: " + self.localizacao

class Tipo_transporte(BaseModel):
    tipo = CharField()
    denominacao = CharField()

    def __str__(self):
        return "O tipo de transporte será: " + self.tipo + " e será: " + self.denominacao

class Hotel(BaseModel):
    nome = CharField()
    cnpj = IntegerField()

    def __str__(self):
        return "O hotel será: " + self.nome + " e possui CNPJ número: " + str(self.cnpj)

class Reserva(BaseModel):
    local = CharField()
    qtd_dias = IntegerField()

    def __str__(self):
        return "A reserva será feita no local: " + self.local + " e possuirá: " + str(self.qtd_dias) + "dia(s)"

class Tipo_viagem(BaseModel):
    tipo = CharField()

    def __str__(self):
        return "A viagem será: " + self.tipo

class Guia(BaseModel):
    nome = CharField()
    cpf = IntegerField()

    def __str__(self):
        return "O guia será: " + self.nome + " e possui CPF número: " + str(self.cpf)

class Pagamento(BaseModel):
    forma_pagamento = CharField()
    valor_final = FloatField()

    def __str__(self):
        return "A forma de pagamento será: " + self.forma_pagamento + " e tem como valor total: R$" + str(self.valor_final)

class Viagem(BaseModel):
    cliente = ForeignKeyField(Cliente)
    destino = ForeignKeyField(Destino)

    def __str__(self):
        return "O cliente: " + str(self.cliente) + " viajará para: " + str(self.destino)

if __name__ == "__main__":
    
    if os.path.exists(arq):
        os.remove(arq)
    
    try:
        db.connect()
        db.create_tables([Cliente,
                          Agencia,
                          Destino,
                          Tipo_transporte,
                          Hotel,
                          Reserva,
                          Tipo_viagem,
                          Guia,
                          Pagamento,
                          Viagem])

    except OperationalError as e:
        print('erros: ' + str(e))

    julia = Cliente.create(nome = "Júlia Theiss", cpf = 12708538993)
    poliana = Cliente.create(nome = "Poliana Zalasik", cpf = 19972926958)
    natalia = Cliente.create(nome = "Natália Weise", cpf = 12345696712)
    cvc = Agencia.create(nome = "CVC", cnpj = 12345678901)
    inglaterra = Destino.create(nome = "Londres", localizacao = "Inglaterra")
    aviao = Tipo_transporte.create(tipo = "Aéreo", denominacao = "Avião")
    mercure = Hotel.create(nome = "Mercure", cnpj = 59773839915)
    reserva = Reserva.create(local = "Mercure", qtd_dias = 14)
    internacional = Tipo_viagem.create(tipo = "Internacional")
    leandro_guia = Guia.create(nome = "Leandro Speckort", cpf = 12818557923)
    pagamento = Pagamento.create(forma_pagamento = "dinheiro", valor_final = 8000)
    viagem = Viagem.create(cliente = julia, destino = inglaterra)

    print(julia)
    print(cvc)
    print(inglaterra)
    print(aviao)
    print(mercure)
    print(reserva)
    print(internacional)
    print(leandro_guia)
    print(pagamento)
    
