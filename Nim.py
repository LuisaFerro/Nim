#preciso de:
#função "computador_escolhe_jogada" que tem como parametros n e m e devolve um numero inteiro e devolve quantas peças o pc deve tirar do tabuleiro
#função "usuario_escolhe_jogada" que tmb tem n e m como parâmetros e solicita que o jogador informe sua jogada e verifica se o valor é válido.
#   Se for, a função deve devolvê-lo, se não, "deve solicitar novamente ao usuário que informe uma jogada válida."
#função "partida" que não recebe parametro mas solicita o usuário que informe n e m e inicia o game, alternando entre jogadas do pc e do usuário
#   (ou seja, chema as duas funções anterioores)
#a cd jogada, deve ser impresso na tela o estado atual do game, "quantas peças foram removidas na última jogada e quantas restam na mesa. "
# com a última peça, imprime "O computador ganhou!" ou "Você ganhou!" conforme o caso
# função " campeonato" ssa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o
#   vencedor do campeonato. O placar deve ser impresso na forma:
#       Placar: Você ??? X ??? Computador
#repita até o valor digitado pelo usuário ser válido
#N = numero total de peças no tabuliero
#M = número máximo de peças que se pode tirar por jogada


def computador_escolhe_jogada(n,m):
    n0_pc = n
    if n%(m+1) == 0:
        if m == 1:
            print ('\nComputador tirou uma peça')
            n = n0_pc - 1
            print('Agora o tabuleiro tem {} peças'.format(int(n)))
            return int(n0_pc - n)
        else:
            print('\nComputador tirou {} peças'.format(int(m)))
            n = n0_pc - m
            print('Agora o tabuleiro tem {} peças'.format(int(n)))
            return int(n0_pc - n)
    else:
        while n%(m+1) != 0:
            n = n - 1
        if n == 0 and (n0_pc - n) == 1:
            print('\nO computador tirou uma peça.\nFim do jogo! O computador venceu!')
            return int(n0_pc - n)
        if n == 0 and (n0_pc - n) != 1:
            print('\nO computador tirou {} peças.\nFim do jogo! O computador venceu!'.format(int(n0_pc - n)))
            return int(n0_pc - n)
        if (n0_pc - n) == 1 and n == 1:
            print('\nO computador tirou uma peça.\nAgora tem uma peça no tabuleiro')
            return int(n0_pc - n)
        if (n0_pc - n) == 1 and n > 1:
            print('\nO computador tirou uma peça.\nAgora tem {} peças no tabuleiro'.format(int(n)))
            return int(n0_pc - n)
        if (n0_pc - n) > 1 and n > 1:
            print('\nO computador tirou {} peças.\nAgora tem {} peças no tabuleiro'.format(int(n0_pc - n),int(n)))
            return int(n0_pc - n)


def usuario_escolhe_jogada(n,m):
    n0_usuario = n
    jogada = float(input('\nQuantas peças você vai tirar? '))
    while n0_usuario == n:
        if jogada//1 == jogada/1 and jogada > 0:
            if jogada > m:
                print('\nOops! Jogada inválida! Tente de novo.')
                jogada = float(input('\nQuantas peças você quer tirar? '))
            else:
                n = n0_usuario - jogada
                if n == 0 and jogada != 0:
                    print('Você tirou {} peças.\nFim do jogo! Você venceu!'.format(int(jogada)))
                if n == 0 and jogada == 1:
                    print('Você tirou uma peça.\nFim do jogo! Você venceu!')
                if n != 0:
                    if jogada == 1 and n == 1 :
                        print('\nVocê tirou uma peça.\nAgora resta uma peça no tabuleiro.')
                        return jogada
                    if jogada == 1 and n != 1:
                        print('\nVocê tirou uma peça.\nAgora restam {} peças no tabuleiro.'.format(int(n)))
                        return jogada
                    if jogada != 1 and n == 1:
                        print('\nVocê tirou {} peças.\nAgora resta uma peça no tabuleiro.'.format(int(jogada)))
                        return jogada
                    if jogada != 1 and n != 1:
                        print('\nVocê tirou {} peças.\nAgora restam {} peças no tabuleiro.'.format(int(jogada),int(n)))
                        return jogada
        else:
            print('\nOops! Jogada inválida! Tente de novo.')
            jogada = float(input('\nQuantas peças você vai tirar? '))


def partida():
    n = int(input('\nQuantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    jogada_usuario = 1
    jogada_pc = 1
    n0 = n
    if n%(m+1) == 0:
        print('\nVocê começa!')
        while n != 0:
            jogada_usuario = usuario_escolhe_jogada(n,m)
            n = n - jogada_usuario
        
            if n != 0:
                jogada_pc = computador_escolhe_jogada(n,m)
                n = n - jogada_pc
                if n == 0:
                    return 1
            else:
                return 2
            
    if n%(m+1) != 0:
        print('\nComputador começa!')
        while n != 0:
            jogada_pc = computador_escolhe_jogada(n,m)
            n = n - jogada_pc
            if n != 0:
                jogada_usuario = usuario_escolhe_jogada (n,m)
                n = n - jogada_usuario
            else:
                return 1


def campeonato():
    print('\n===== Rodada 1 ========')
    pessoa_venceu_num = 0
    pc_venceu_num = 0
    
    if partida() == 1:
        pc_venceu_num = 1
    else:
        pessoa_venceu_num = 1

    print('\n===== Rodada 2 ========')
    if partida() == 1:
        pc_venceu_num = pc_venceu_num + 1
    else:
        pessoa_venceu_num = pessoa_venceu_num + 1
        
    print('\n===== Rodada 3 ========')
    if partida() == 1:
        pc_venceu_num = pc_venceu_num + 1
    else:
        pessoa_venceu_num = pessoa_venceu_num + 1
    
    print('\n=====Final  do campeonato ======')
    print('\n Placar: Você {} X Computador {}'.format(int(pessoa_venceu_num),int(pc_venceu_num)))
             

print('\nBem-vindo ao jogo do NIM! Escolha:')
escolha = int(input('\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato '))
if escolha == 1:
    print('\nVocê escolheu uma partida isolada!')
    print('\n=====================================')
    partida()
    
else:
    print('\nVocê escolheu um campeonato')
    campeonato()


    
    
