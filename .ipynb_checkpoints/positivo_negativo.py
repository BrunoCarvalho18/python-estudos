# crie uma funcao que recebe um numero
# e retorna 'P' caso ele for positivo ou 'N'
# caso contrario

def positivo_negativo(numero):
        '''
        Recebe um inteiro e retorna:
           'P' - para numeros positivos
           'N' - para numeros negativos
        '''

        retorno = ''

        if numero > 0:
            retorno = 'P'
        else:
            retorno = 'N'
      
        return retorno

print(positivo_negativo(55))
print(positivo_negativo(-4))
        
