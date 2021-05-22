dic ={
    '1': lambda x,y : x + y,
    '2': lambda x,y : x - y,
    '3': lambda x,y : x * y,
    '4': lambda x,y : x / y,
    '5': lambda x,y : exit(),
}

while True:
    n1 = float(input('N1: '))
    n2 = float(input('N2: '))
    
    op = input(f'Digite a opção desejada \n'\
               f'1 - Soma \n'\
               f'2 - Subtracao \n'\
               f'3 - Multiplicacao \n'\
               f'4 - Divisao \n'\
               f'5 - Sair \n')
    try:
        res = dic[op](n1,n2)
    except ZeroDivisionError:
        print('Não dividirás por zero')
    except KeyError:
        print('Digite uma opção válida')
    except ValueError:
        print('Digite apenas números')
    except Exception as err:
        print('Erro da descrição',err)
    else:
        print(res)
    finally:
        print('terminou o programa')
               