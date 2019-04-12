#!/usr/bin/env python
# coding: utf-8

import pycep_correios
from pycep_correios.excecoes import ExcecaoPyCEPCorreios

"""
Retornos possíveis da API dos Correios:

end: corresponde ao logradouro do endereço do CEP;
bairro: bairro referente ao CEP pesquisado;
cidade: cidade referente ao CEP pesquisado;
complemento2: semelhante ao complemento, pode indicar, por exemplo, 
o intervalo de números de residências ao qual o CEP pertence;
uf: a sigla do estado (SP para São Paulo, MG para Minas Gerais e etc) 
ao qual o CEP representa;
cep: o CEP consultado.

"""

try:
    print("Informe o número do seu CEP")
    cep = input("Digite seu CEP: ")
    new_cep = cep.replace("-", "")
    endereco = pycep_correios.consultar_cep(new_cep)

    print("\nResultado da Consulta")
    print(f"Endereço: {endereco['end']}")
    print(f"Bairro: {endereco['bairro']}")
    print(f"Cidade: {endereco['cidade']}")
    print(f"Complemento: {endereco['complemento2']}")
    print(f"CEP: {endereco['cep']}")

except ExcecaoPyCEPCorreios as exec:
    print(f"Erro ao formatar: {exec}")
