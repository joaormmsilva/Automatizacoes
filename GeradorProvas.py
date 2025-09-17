import random

capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}


for prova_num in range(30):
    arquivo_prova = open(f'prova_geografia - {prova_num + 1}.txt,', 'w',encoding='utf8')
    arquivo_resposta = open(f'prova_geografia_reposta - ({prova_num+1}.txt)', 'w',encoding='utf8')

    arquivo_prova.write('Nome:\n\nData:\n\nPeriodo:\n\n')
    arquivo_prova.write((' ' * 20) + f'Prova Capitais Brasileiras (Questionario {prova_num + 1})\n\n')

    estados = list(capitais.keys())
    random.shuffle(estados)

    for questao_num  in range(26):
        resposta_correta = capitais[estados[questao_num]]
        respostas_erradas = list(capitais.values())
        del respostas_erradas[respostas_erradas.index(resposta_correta)]
        respostas_erradas = random.sample(respostas_erradas, 3)
        respostas = respostas_erradas + [resposta_correta]
        random.shuffle(respostas)
        arquivo_prova.write(f'{questao_num + 1}. Qual é a caputal de {estados[questao_num]}?\n')
        for i in range(4):      
            arquivo_prova.write(f"      {'ABCD'[i]}. {respostas[i]}\n")
        arquivo_prova.write("\n")

        arquivo_resposta.write(f"{questao_num}. {'ABCD'[respostas.index(resposta_correta)]}\n")

    arquivo_prova.close()
    arquivo_resposta.close()