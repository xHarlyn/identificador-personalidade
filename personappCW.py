# Definidor de pessoa

def identificador_de_personalidade():
    print(str.upper('Identificador de Personalidade'))

    q1 = input('Digite seu nome: ')
    print(f'Okay {q1}, agora iremos começar!')
#Abertura
    a1 = int(input('Dentre estas 3 opções, como você descreveria sua pessoa?\n1- Humilde\n2- Especial\n3- Egoísta\n> '))
                                             #Caminho 1#
#Solução 1#                                             
    if a1 == 1:
        a3 = int(input('O que você faria se recebesse 10 mil reais por engano?\n1- Guardar, para caso o dono te procurasse.\n2- Gastar, não é culpa sua terem cometido este erro.\n3- Devolver, nunca se sabe quando pode acontecer com você.\n> '))
        if a3 == 1:
            a5 = int(input('Qual desses "Defeitos" é mais plausível de você ter?\n1- Perfeccionismo\n2- Bondade\n3- Empatia\n> '))
            if a5 == 1:
                a2 = int(input('Como você reagiria em caso de traição?\n1- Compreensivo\n2- Agressivo\n3- Apático\n> '))
                if a2 == 1:
                    print(f'Realmente, {q1}.\nVocê é uma pessoa muito boa, ou finge ser... A questão é: Para quem você está tentando se provar?')
                elif a2 == 2:
                    print(f'Então, violência é a única solução, {q1}?\nPensava que sua índole fosse levá-lo a decisões diferentes, mas quem estamos tentando enganar? kkkk')
                elif a2 == 3:
                    print(f'Admirável ou perturbador?\nA verdade é que ninguém é mais importante que nós mesmos, não é mesmo {q1}?')
            if a5 == 2:
                print(f'Parabéns, {q1}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.')
            if a5 == 3:
                a4 = int(input('Se pudesse realizar um desejo, qual seria?\n1- Fim da Pobreza.\n2- A Cura do Câncer.\n3- Mais 3 desejos.\n> '))
                if a4 == 1:
                    print(f'Parabéns, {q1}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.')
                elif a4 == 2:
                    print(f'{q1},\nFico me perguntando se todas essas perguntas fossem reais a ponto de sua vida depender disso, como você reagiria ao saber que existem pessoas iguais a você por aí?')
                elif a4 == 3:
                    print(f'Por que será que eu não esperava mais de você, {q1}?')
#Solução 2#                    
        elif a3 == 2:
            a2 = int(input('Como você reagiria em caso de traição?\n1- Compreensivo\n2- Agressivo\n3- Apático\n> '))
            if a2 == 1:
                print(f'Realmente, {q1}.\nVocê é uma pessoa muito boa, ou finge ser... A questão é: Para quem você está tentando se provar?')
            elif a2 == 2:
                print(f'Então, violência é a única solução, {q1}?\nPensava que sua índole fosse levá-lo a decisões diferentes, mas quem estamos tentando enganar? kkkk')
            elif a2 == 3:
                print(f'Admirável ou perturbador?\nA verdade é que ninguém é mais importante que nós mesmos, não é mesmo {q1}?')
#Solução 3#        
        elif a3 == 3:
            a4 = int(input('Se pudesse realizar um desejo, qual seria?\n1- Fim da Pobreza.\n2- A Cura do Câncer.\n3- Mais 3 desejos.\n> '))
            if a4 == 1:
                print(f'Parabéns, {q1}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.')
            elif a4 == 2:
                print(f'{q1},\nFico me perguntando se todas essas perguntas fossem reais a ponto de sua vida depender disso, como você reagiria ao saber que existem pessoas iguais a você por aí?')
            elif a4 == 3:
                print(f'Por que será que eu não esperava mais de você, {q1}?')

                                             #Caminho 2# 
#Solução 4#                                             
    elif a1 == 2:
        a5 = int(input('Qual desses "Defeitos" é mais plausível de você ter?\n1- Perfeccionismo\n2- Bondade\n3- Empatia\n> '))
        if a5 == 1:
            a2 = int(input('Como você reagiria em caso de traição?\n1- Compreensivo\n2- Agressivo\n3- Apático\n> '))
            if a2 == 1:
                print(f'Realmente, {q1}.\nVocê é uma pessoa muito boa, ou finge ser... A questão é: Para quem você está tentando se provar?')
            elif a2 == 2:
                print(f'Então, violência é a única solução, {q1}?\nPensava que sua índole fosse levá-lo a decisões diferentes, mas quem estamos tentando enganar? kkkk')
            elif a2 == 3:
                print(f'Admirável ou perturbador?\nA verdade é que ninguém é mais importante que nós mesmos, não é mesmo {q1}?')
#Solução 5#
        if a5 == 2:
            a3 = int(input('O que você faria se recebesse 10 mil reais por engano?\n1- Guardar, para caso o dono te procurasse.\n2- Gastar, não é culpa sua terem cometido este erro.\n3- Devolver, nunca se sabe quando pode acontecer com você.\n> '))
            if a3 == 1:
                 print(f'Realmente, {q1}.\nVocê é uma pessoa muito boa, ou finge ser... A questão é: A quem você está tentando se enganar?')
            elif a3 == 2:
                a2 = int(input('Como você reagiria em caso de traição?\n1- Compreensivo\n2- Agressivo\n3- Apático\n> '))
                if a2 == 1:
                    print(f'Realmente, {q1}.\nVocê é uma pessoa muito boa, ou finge ser... A questão é: Para quem você está tentando se provar?')
                elif a2 == 2:
                    print(f'Então, violência é a única solução, {q1}?\nPensava que sua índole fosse levá-lo a decisões diferentes, mas quem estamos tentando enganar? kkkk')
                elif a2 == 3:
                    print(f'Admirável ou perturbador?\nA verdade é que ninguém é mais importante que nós mesmos, não é mesmo {q1}?')
            elif a3 == 3:
                a4 = int(input('Se pudesse realizar um desejo, qual seria?\n1- Fim da Pobreza.\n2- A Cura do Câncer.\n3- Mais 3 desejos.\n> '))
                if a4 == 1:
                    print(f'Parabéns, {q1}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.')
                elif a4 == 2:
                    print(f'{q1},\nFico me perguntando se todas essas perguntas fossem reais a ponto de sua vida depender disso, como você reagiria ao saber que existem pessoas iguais a você por aí?')
                elif a4 == 3:
                    print(f'Por que será que eu não esperava mais de você, {q1}?')
#Solução 6#        
        if a5 == 3:
            a4 = int(input('Se pudesse realizar um desejo, qual seria?\n1- Fim da Pobreza.\n2- A Cura do Câncer.\n3- Mais 3 desejos.\n> '))
            if a4 == 1:
                print(f'Parabéns, {q1}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.')
            elif a4 == 2:
                print(f'{q1},\nFico me perguntando se todas essas perguntas fossem reais a ponto de sua vida depender disso, como você reagiria ao saber que existem pessoas iguais a você por aí?')
            elif a4 == 3:
                print(f'Por que será que eu não esperava mais de você, {q1}?')
                
                                                 #Caminho 3#
#Solução 7#                                                 
    elif a1 == 3:
        a4 = int(input('Se pudesse realizar um desejo, qual seria?\n1- Fim da Pobreza.\n2- A Cura do Câncer.\n3- Mais 3 desejos.\n> '))
        if a4 == 1:
            print(f'Parabéns, {q1}.\nÉtica e empatia, embora distintos, estão intrinsecamente conectados e é bom saber que ambos fazem parte do seu caráter.')
#Solução 8#        
        elif a4 == 2:
            print(f'{q1},\nFico me perguntando se todas essas perguntas fossem reais a ponto de sua vida depender disso, como você reagiria ao saber que existem pessoas iguais a você por aí?')
#Solução 9#        
        elif a4 == 3:
            print(f'Por que será que eu não esperava mais de você, {q1}?')
            
    print('Eaí?\nSe divertiu?\nVamos tentar novamente?')


identificador_de_personalidade()
