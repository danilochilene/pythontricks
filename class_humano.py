# coding: utf-8
'''
Uma classe simples demonstrando atributos
'''

class Humano(object):
    fulano    = 'Fulano'

    
    def __init__(self, nome, sexo='M'):
        assert sexo in ('M', 'F'), u'SEXO INVÁLIDO %s escolha M ou F' % sexo
        self.nome = nome
        self.sexo = sexo
        self.bipede    = True
        self.carnivoro = False
        self.profissao = None
       

    def sexo(self):
        return "Macho" if self.sexo == 'M' else u'Femêa' 
    
    def dieta(self, carnivoro):
        if carnivoro == True:
            print self.nome, u'É carnivoro'
        else:
            print self.nome, u'É vegetariano'

    def profissao(self, profissao):
        if self.profissao is None:
            return u'Não informado'
        return self.profissao
    
    def carreira(self, profissao):
        self.profissao = profissao
        
    def __str__(self):
        return 'Nome:\t%s \nSexo:\t%s \nProfissao:\t%s\n' % (self.nome, self.sexo, self.profissao)

if __name__ == "__main__":
    Humano1 = Humano('Juca')
    Humano1.carreira('Peao')
    Humano2 = Humano('Pedro')
    Humano2.carreira('Medico')
    
    for object_ in (Humano1, Humano2):
        print object_
