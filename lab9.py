#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Copa do Mundo de Futebol
# Nome: Jackeline Leme Gregório
# RA: 173678
#####################################################

# Leitura da lista de seleções

selecoes = []
dic = {}
for i in range(16):
    selecao = input()
    selecoes.append(selecao)
    dic[selecao] = {"partidas": 0,
                    "vitorias": 0,
                    "derrotas": 0,
                    "penaltis": 0,
                    "normal": 0,
                    "marcados": 0,
                    "sofridos": 0}

# Leitura das partidas e processamento dos dados
for i in range(16):
    resultado = input()

    if "(" not in resultado:
        pais1 = resultado.split(" ")[0]
        gols1 = int(resultado.split(" ")[1])
        pais2 = resultado.split(" ")[4]
        gols2 = int(resultado.split(" ")[3])

        if (gols1 > gols2):
            dic[pais1]["vitorias"] = dic[pais1]["vitorias"] + 1
            dic[pais2]["derrotas"] = dic[pais2]["derrotas"] + 1
        else:
            dic[pais2]["vitorias"] = dic[pais2]["vitorias"] + 1
            dic[pais1]["derrotas"] = dic[pais1]["derrotas"] + 1

        dic[pais1]["normal"] = dic[pais1]["normal"] + 1
        dic[pais2]["normal"] = dic[pais2]["normal"] + 1
        dic[pais1]["partidas"] = dic[pais1]["partidas"] + 1
        dic[pais1]["marcados"] = dic[pais1]["marcados"] + gols1
        dic[pais1]["sofridos"] = dic[pais1]["sofridos"] + gols2
        dic[pais2]["partidas"] = dic[pais2]["partidas"] + 1
        dic[pais2]["marcados"] = dic[pais2]["marcados"] + gols2
        dic[pais2]["sofridos"] = dic[pais2]["sofridos"] + gols1

    else:
        pais1 = resultado.split(" ")[0]
        gols1 = int(resultado.split(" ")[1])
        pais2 = resultado.split(" ")[7]

        gols1_penalti = int(resultado.split(" ")[4].split("(")[1])
        gols2_penalti = int(resultado.split(" ")[6].split(")")[0])

        dic[pais1]["penaltis"] = dic[pais1]["penaltis"] + 1
        dic[pais2]["penaltis"] = dic[pais2]["penaltis"] + 1
        dic[pais1]["partidas"] = dic[pais1]["partidas"] + 1
        dic[pais1]["marcados"] = dic[pais1]["marcados"] + gols1
        dic[pais1]["sofridos"] = dic[pais1]["sofridos"] + gols1
        dic[pais2]["partidas"] = dic[pais2]["partidas"] + 1
        dic[pais2]["marcados"] = dic[pais2]["marcados"] + gols1
        dic[pais2]["sofridos"] = dic[pais2]["sofridos"] + gols1

        if gols1_penalti > gols2_penalti:
            dic[pais1]["vitorias"] = dic[pais1]["vitorias"] + 1
            dic[pais2]["derrotas"] = dic[pais2]["derrotas"] + 1
        else:
            dic[pais2]["vitorias"] = dic[pais2]["vitorias"] + 1
            dic[pais1]["derrotas"] = dic[pais1]["derrotas"] + 1

for selecao in selecoes:
    print("-" * 50)
    print("Pais:", selecao)
    print("Partidas:", dic[selecao]["partidas"])
    print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
    print("Partidas decididas nos penaltis:", dic[selecao]["penaltis"])
    print("Vitorias:", dic[selecao]["vitorias"])
    print("Derrotas:", dic[selecao]["derrotas"])
    print("Gols marcados:", dic[selecao]["marcados"])
    print("Gols sofridos:", dic[selecao]["sofridos"])

vitorias = 0
campeao = ""

for pais in dic:
    if dic[pais]["vitorias"] > vitorias:
        vitorias = dic[pais]["vitorias"]
        campeao = pais
