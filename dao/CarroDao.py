from model.Carro import Carro


class CarroDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarCarros(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM carro ORDER BY id'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            carro = Carro()
            carro.id = item[0]
            carro.modelo = item[1]
            carro.categoria = item[2]
            carro.valor = item[3]

            lista.append(carro)

        return lista

    def selecionarCarro(self, id) -> Carro:
        c = self.connection.cursor()
        c.execute(f"SELECT * FROM carro WHERE id = {id}")
        recset = c.fetchone()
        c.close()

        print(recset)

        carro = Carro()
        carro.id = recset[0]
        carro.modelo = recset[1]
        carro.categoria = recset[2]
        carro.valor = recset[3]

        return carro

    def excluirCarro(self, carro: Carro) -> Carro:
        c = self.connection.cursor()
        c.execute("""
            delete from carro
            where id = '{}'
        """.format(carro.id))
        self.connection.commit()

    def inserirCarro(self, carro: Carro) -> Carro:
        c = self.connection.cursor()
        c.execute("""
            insert into carro(id, modelo, categoria, valor)
            values('{}', '{}', '{}', '{}') RETURNING id
        """.format(carro.id, carro.modelo, carro.categoria, carro.valor))
        self.connection.commit()

    def alterarCarro(self, carro: Carro) -> Carro:
        c = self.connection.cursor()
        c.execute("""
            update carro
            SET modelo = '{}', categoria = '{}', valor = '{}'
            WHERE id = '{}';
        """.format(carro.modelo, carro.categoria, carro.valor, carro.id))

        self.connection.commit()


