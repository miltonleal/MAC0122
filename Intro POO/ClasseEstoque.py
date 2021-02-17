class EstoqueProdutos: #define a classe Estoque

    #construtor da classe

    def __init__(self, _nome, _codigo, _preco, _quantidade):
        #criando as instâncias
        self._nome = _nome
        self._codigo = _codigo
        self._preco = _preco
        self._quantidade = _quantidade

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

# TESTES

if __name__ == "__main__":
    produto_1 = EstoqueProdutos("Bermuda", 1, 50, 100)
    produto_2 = EstoqueProdutos("Camisa", 2, 30, 100)
    produto_3 = EstoqueProdutos("Meia", 3, 20, 200)

    print("Oferta do dia:", produto_1.obtem_nome())
    print("Oferta da semana:", produto_2.obtem_nome())

    #altera preço

    if produto_1.altera_preco(60):
        print("Preço alterado com sucesso para:", produto_1.obtem_preco())
    else: print("Atenção: o preço baixou")

    #verifica se pode efetuar uma venda

    if produto_2.altera_quantidade(90):
        print("Estoque atualizado. Número de itens disponível =", produto_2.obtem_quantidade())
        print("Venda autorizada. Total da venda =", produto_2.obtem_preco() * 90)
    else: "Estoque insuficiente"

