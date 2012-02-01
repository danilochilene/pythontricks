# coding: utf-8

class Humano(object):
    bipede    = True
    carnivoro = False
    profissao = None
    
    def __init__(self, nome, sexo='M'):
        self.nome = nome
        self.sexo = sexo
        assert sexo in ('M', 'F'), u'SEXO INVÁLIDO %s escolha M ou F' % sexo
        
    def sexo(self):
        return "Macho" if self.sexo=='M' else u'Femêa' 
        
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
        return u'Nome:\t%s \nSexo:\t%s \nProfissao:\t%s\n' % (self.nome, self.sexo, self.profissao)
        
    def __repr__(self):
        return u'Humano({0!r})'.format(self.nome, self.sexo, self.profissao)

if __name__ == "__main__":
    Humano1 = Humano('Juca')
    Humano1.carreira('Peao')
    Humano2 = Humano('Pedro')
    Humano2.carreira('Medico')
    
    for object_ in (Humano1, Humano2):
        print object_
