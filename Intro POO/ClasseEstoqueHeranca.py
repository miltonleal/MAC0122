class EstoqueProdutos: #define a classe Estoque

    #construtor da classe

    def __init__(self, nome, codigo, preco, quantidade):
        #criando as instâncias
        self._nome = nome
        self._codigo = codigo
        self._preco = preco
        self._quantidade = quantidade

    #métodos que obtêm os atributos

    def obtem_nome(self):
        return self._nome

    def obtem_codigo(self):
        return self._codigo

    def obtem_preco(self):
        return self._preco

    def obtem_quantidade(self):
        return self._quantidade

    #método que altera o preço

    def altera_preco(self, novo_preco):
        preco_atual = self._preco
        self._preco = novo_preco
        if novo_preco > preco_atual: return True
        return False

    #método que altera quantidade no estoque

    def altera_quantidade(self, novo_pedido):
        if novo_pedido > self._quantidade: return False
        self._quantidade -= novo_pedido
        return True

class EstoqueProdutosCriticos(EstoqueProdutos):

    def __init__(self, nome, codigo, preco, quantidade, estoque_min):
        super().__init__(nome, codigo, preco, quantidade)
        self.estoque_min = estoque_min

    def altera_quantidade(self, novo_pedido):
        if novo_pedido + self.estoque_min > self._quantidade:
            return False
        return super().altera_quantidade(novo_pedido)

    def altera_preco(self, novo_preco):
        preco_atual = self._preco
        if novo_preco > 1.1 * preco_atual or novo_preco < 0.9 * preco_atual:
            return False
        preco_atualizado = super().altera_preco(novo_preco)
        return True

produto1 = EstoqueProdutosCriticos("Camisa", 1, 10, 100, 10)

print(produto1.altera_preco(10.5))
print(produto1.altera_quantidade(3))