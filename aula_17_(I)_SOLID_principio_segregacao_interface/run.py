"""
Este metodo de CLEAN CODE, tem como objetivo fazer com que todas as interfaces implementadas nas classes nunca sejam
genéricas, sempre sejam definidas conforme cada classe tenha seus metodos. Exemplo é do canario e pinguim
para cada ave existe suas caracteristicas, no caso do pinguim ele não obtêm a habilidade de voar, com isto existe uma
interface específica para ele que não tem o método de voar, ou seja, para cada ave criada que não detêm das mesmas
habilidades, o obetivo é criar uma interface própria para o animal.

"""

from aves import Pinguin, Canario

canario = Canario()
pinguin = Pinguin()

canario.comer()
pinguin.comer()

canario.gritar()
pinguin.gritar()

canario.voar()
