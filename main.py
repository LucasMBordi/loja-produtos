from produto import Produto
from log import registrar_log
def main():
    produto1 = Produto("Mouse", 80, estoque=10)
    produto2 = Produto("Teclado", 250, estoque=5)
    print(produto1)
    print(produto2)
    
    if produto2.vender(2):
        print("Sucesso")
        registrar_log("Venda de dois teclados")
    
if __name__ == "__main__":
    main()