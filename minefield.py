from random import randint

campo_minado = [
    ["⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛"],
    ["⬛", "⬛", "⬛"],
]

def tem_bomba(campo):
    for linha in campo:
        if "💣" in linha:
            return True
    return False

jogadas = 0
linha_mina_errada = randint(0,2)
coluna_mina_errada = randint(0,2)

while True:
    for linha in campo_minado:
        for coluna in linha:
            print(coluna, end=" ")
        print()

    linha_pessoa = int(input(
        "Digite a linha que deseja [1-3]: "
        )) - 1
    
    coluna_pessoa = int(input(
        "Digite a coluna que deseja [1-3]: "
        )) - 1
    
    print (
        "\n◃───────────────────────────▹\n"
    )
    
    if campo_minado[linha_pessoa][coluna_pessoa] == "💎": 
        print (
            "Você já fez essa jogada. Tente Novamente.\n\n◃───────────────────────────▹\n\n"
        )
        continue 

    if not tem_bomba(campo_minado) and jogadas == 7: 
        print (
            "Você ganhou!!"
        )
        campo_minado[linha_pessoa][coluna_pessoa] = "💎"
        campo_minado[linha_mina_errada][coluna_mina_errada] = "💣"

    elif linha_pessoa == linha_mina_errada and coluna_pessoa == coluna_mina_errada:
        print(
            "Você perdeu!"
            )
        campo_minado[linha_pessoa][coluna_pessoa] = "💣"
        jogadas += 1
        break

    else:
        campo_minado[linha_pessoa][coluna_pessoa] = "💎"
        jogadas += 1

print (
    "\n===========\nCampo final: "
    )
for linha in campo_minado:
    for coluna in linha:
        print(coluna, end=" ")
    print()
