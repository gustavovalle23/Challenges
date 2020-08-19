# -*- coding: utf-8 -*-

if __name__ == '__main__':
    def pedido(pedidos):

        codigo = pedidos.split(' ')[0]
        quantidade = pedidos.split(' ')[1]

        codigo = float(codigo)
        quantidade = float(quantidade)

        if codigo == 1:
            return f'Total: R$ {(quantidade * 4):.2f}'
        elif codigo == 2:
            return f'Total: R$ {(quantidade * 4.5):.2f}'
        elif codigo == 3:
            return f'Total: R$ {(quantidade * 5):.2f}'
        elif codigo == 4:
            return f'Total: R$ {(quantidade * 2):.2f}'
        elif codigo == 5:
            return f'Total: R$ {(quantidade * 1.5):.2f}'

    pedidos = input()

    print(pedido(pedidos))
