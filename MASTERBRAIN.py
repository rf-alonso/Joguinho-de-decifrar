import random
import sys

def main():
    ''' Jogo MASTERBRAIN
    '''
    print("\n   =============================    ")
    print("      Bem vindo ao MASTERBRAIN        ")
    print("   =============================  ")
    print('\nEste jogo foi inspirado no jogo MasterMind. O objetivo é')
    print('advinhar uma senha com "n" digitos variando de 0 até 9')
    print('(podendo haver repetições), com um determinado número de tentativas.')
    print('\nAntes de iniciar, defina algumas configurações.\n')
    
    maxchutes, tamanho, semente, debug = modo_de_jogo()
    
    print("\n   =============================    ")
    print("            MASTERBRAIN               ")
    print("   =============================\n  ")
    print(f"Você tem {maxchutes} chances para ")
    print(f"acertar uma senha formada por {tamanho} dígitos\n")
    
    senha = sorteie(tamanho, semente)
    if debug:
        print(f">>> A senha é: {senha}\n")
    maxchutes2 = 1
    controle = True
    while maxchutes2 <= maxchutes and controle:
        chute = int(input(f"Digite o seu chute [{maxchutes2}/{maxchutes}]: "))
        a = corretos_em_qualquer_posicao( senha, chute, tamanho)
        b = corretos_em_posicao( senha, chute, tamanho)
        print(f"\n === Dígitos corretos em qualquer posição: {a}")
        print(f" === Dígitos em posições corretas        : {b}\n")
        if b == tamanho:
            print("Parabéns!")
            print(f"Você acertou em {maxchutes2} chute(s)!")
            controle = False
        maxchutes2 += 1
    if controle:
        print(f"Que pena... a senha era {senha}")
           
def sorteie( n, semente):
    ''' (int, int) -> int
        Recebe um inteiro n que define o comprimento da senha
        e uma semente para o gerador de números pseudo aleatórios.
        Retorna um inteiro com até n dígitos.
    '''
    random.seed(semente)
    senha = random.randrange(10**n)
    return senha     

def corretos_em_posicao( senha, chute, tamanho):
    ''' (int, int, int) -> int ---
        Recebe três inteiros com tamanho dígitos, incluindo 
        zeros à esquerda e retorna o número de dígitos
        da senha que são iguais e estão na mesma posição que
        em chute.
    '''
    senhalist = transforma( senha, tamanho)
    chutelist = transforma( chute, tamanho)
    contador = 0
    for a in range(len(senhalist)):
        if senhalist[a] == chutelist[a]:
            contador += 1
    return contador

def corretos_em_qualquer_posicao ( senha, chute, tamanho):
    ''' (str, str, int) -> int ---
        Recebe duas strings, não necessariamente de mesmo tamanho, e um inteiro.
        Retorna o número de caracteres de senha em comum com chute, de acordo 
        com o tamanho e independentemente da posição relativa.
    '''
    senhalist = transforma( senha, tamanho)
    chutelist = transforma( chute, tamanho)
    cont = 0
    for a in range(len(senhalist)):
        continuar = True
        for b in range(len(chutelist)):
            if senhalist[a] == chutelist[b] and continuar:
                cont += 1
                continuar = False
                chutelist[b] = "Contado"
    return cont

def transforma( num, tamanho):
    '''
        (int, int) -> list ---
        Recebe dois inteiros
        e retorna uma lista com os números de num de determinado tamanho,
        respeitando a ordem original e quantia de zeros à esquerda.
    '''
    fill = 10**tamanho
    numreal = fill + num
    listagem = []
    b = (tamanho - 1)
    while b >= 0:
        ni = (numreal//10**b)%10
        listagem += [ni]
        b -= 1
    return listagem

def modo_de_jogo():
    '''
    () -> int, int, int, bool ---
    Função que determina algumas variáveis importantes para o jogo.
    '''  
    resposta = input('Deseja jogar um modo pré selecionado?(s/n): ')
    resposta = resposta.strip().lower()
    if resposta == 's':
        print('Escolha a dificuldade digitando o número: \n')
        print('0 - Fácil')
        print('1 - Médio')
        print('2 - Difícil\n')
        select = int(input(""))
        semente = None
        debug = False
        if select == 0:
            maxchutes = 10
            tamanho = 2
            return maxchutes, tamanho, semente, debug
        elif select == 1:
            maxchutes = 10
            tamanho = 3
            return maxchutes, tamanho, semente, debug
        elif select == 2:
            maxchutes = 12
            tamanho = 4
            return maxchutes, tamanho, semente, debug
            
    if resposta == 'n':
        debug = int(input('Digite 1 para mostrar a senha sorteada ou 0 para esconder: '))
        maxchutes = int(input("Digite o número máximo de chutes: "))
        tamanho = int(input("Digite o tamanho da senha: "))
        semente = input('Digite um número para ser uma seed de senha ou enter para aleatória: ')
        if debug == 1:
            debug = True
        elif debug == 0:
            debug = False
        return maxchutes, tamanho, semente, debug
    else:
        sys.exit("Resposta inválida!")

#-----------------------------------------------------------------------------#
# parte opcional
# chamada da função main e um input para não fechar automaticamente a janela

if __name__ == '__main__':
    main()
input("\nDigite qualquer tecla para sair: ")
