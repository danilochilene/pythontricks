#! /usr/bin/env python
# coding: utf-8
'''
Uma classe simples demonstrando atributos
'''
CONTADOR = 0

class Humano(object):
    
    def __init__(self, nome, sexo='M'):
        global CONTADOR
        assert sexo in ('M', 'F'), 'SEXO INVALIDO %s escolha M ou F' % sexo
        CONTADOR += 1
        self.id = CONTADOR
        self.nome = nome
        self._sexo = sexo
        self.bipede    = True
        self.carnivoro = False
        self.profissao = None

    @property   
    def sexo(self):
        return "Macho" if self._sexo == 'M' else 'Femea' 
    
    @property
    def dieta(self, carnivoro):
        if carnivoro == True:
            print self.nome, 'Eh carnivoro'
        else:
            print self.nome, 'Eh vegetariano'

    def profissao(self, profissao):
        if self.profissao is None:
            return 'Nao informado'
        return self.profissao
    
    def carreira(self, profissao):
        self.profissao = profissao
        
    def __str__(self):
        return 'ID:\t\t%s \nNome:\t\t%s \nSexo:\t\t%s \nProfissao:\t%s\n' % (self.id, self.nome, self.sexo, self.profissao)

if __name__ == "__main__":
    Humano1 = Humano('Juca')
    Humano1.carreira('Peao')
    Humano2 = Humano('Maria', 'F')
    Humano2.carreira('Dona de casa')
    Humano3 = Humano('Lucas')
    Humano3.carreira('Advogado')
    
    for object_ in (Humano1, Humano2, Humano3):
        print object_
