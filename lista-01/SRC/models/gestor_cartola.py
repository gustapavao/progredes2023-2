from gerenciar_arquivos import gerenciar_arquivos
class Cartola:
    def __init__(self, data,forma_time):
        self.__clubes= self.clubes(data)
        self.__posicoes = self.posicoes(data)
        self.__atletas = self.atletas(data)
        formacao = self.formacao(forma_time)
        time = self.montar_time(formacao)
        print(time)
    
    @property
    def all_Clubes(self):
        return self.__clubes
    
    @property
    def all_posicoes(self):
        return self.__posicoes
    
    @property
    def all_atletas(self):
        return self.__atletas
    
    def clubes(self, data):        
        clubes = data["clubes"]
        lista_de_clubes = []
        for clube_id, values in clubes.items():
            lista_de_clubes.append({clube_id:{"nome":values["nome"],"url do escudo": values["escudos"]["60x60"]}})
        return lista_de_clubes
    
    def posicoes(self, data):
        posicoes = data["posicoes"]
        lista_de_posicoes = []
        for id_pos, values in posicoes.items():
            lista_de_posicoes.append({id_pos:{"nome":values["nome"]}})
        return lista_de_posicoes
    
    def atletas(self, data):
        atletas = data["atletas"]
        lista_de_atletas = []
        for i in atletas:
            lista_de_atletas.append({"id_clube": i["clube_id"], 
                                     "posicao":i["posicao_id"], 
                                     "foto_atleta":i["foto"],
                                     "nome":i["nome"],
                                     "nome_abreviado":i["apelido_abreviado"],
                                     "pontuacao": float(i["media_num"])*float(i["jogos_num"])})
        lista_de_atletas = sorted(lista_de_atletas, key= lambda d : d['pontuacao'], reverse=True)
        return lista_de_atletas
    
    def escolher_zagueiro(self, formacao:str, lista_de_atletas):
        formacao = formacao.split("-")
        formacao_defesa = int(formacao[0])
        if formacao_defesa == 3:
            lateral = False
            zagueiro = []
            max = 3
        elif formacao_defesa == 4:
            lateral = True
            linha_de_defesa = list()
            max_zag = 2
            max_lat = 2
        elif formacao_defesa == 5:
            lateral = True
            linha_de_defesa = list()
            max_zag = 3
            max_lat = 2
        else:
            print('Você informou uma formação inválida')
        if lateral:
            for jogador in lista_de_atletas:
                if jogador['posicao'] == 3:
                    linha_de_defesa.append(jogador)
                    if len(linha_de_defesa) == max_zag:
                        break
            for jogador in lista_de_atletas:
                if jogador['posicao'] == 2:
                    linha_de_defesa.append(jogador)
                    if len(linha_de_defesa) == max_lat:
                        break
            return linha_de_defesa

        elif lateral is False:
            for jogador in lista_de_atletas:
                if jogador['posicao'] == 3:
                    zagueiro.append(jogador)
                    if len(zagueiro) == max:
                        break
            return zagueiro
    
    def escolher_meio(self, formacao:str, lista_de_atletas):
        formacao = formacao.split("-")
        max = int(formacao[1])
        meio_campo = []
        for jogador in lista_de_atletas:
            if jogador['posicao'] == 4:
                meio_campo.append(jogador)
                if len(meio_campo) == max:
                    break
        return meio_campo
    def escolher_atacante(self, formacao:str, lista_de_atletas):
        formacao = formacao.split("-")
        max = int(formacao[2])
        atacante = []
        for jogador in lista_de_atletas:
            if jogador['posicao'] == 5:
                atacante.append(jogador)
                if len(atacante) == max:
                    break
        return atacante
    def escolher_goleiro(self, lista_de_atletas):
        goleiro = []
        for jogador in lista_de_atletas:
            if jogador['posicao'] == 1:
                goleiro.append(jogador)
                if len(goleiro) == 1:
                    break
        return goleiro  
    def escolher_tecnico(self, lista_de_atletas):
        tecnico = []
        for jogador in lista_de_atletas:
            if jogador['posicao'] == 6:
                tecnico.append(jogador)
                if len(tecnico) == 1:
                    break
        return tecnico
    
    def montar_time(self, formacao):
        formacao = formacao
        lista_de_atletas= self.all_atletas
        zag = self.escolher_zagueiro(formacao, lista_de_atletas)
        mei = self.escolher_meio(formacao, lista_de_atletas)
        atc = self.escolher_atacante(formacao, lista_de_atletas)
        gol = self.escolher_goleiro(lista_de_atletas)
        tec = self.escolher_tecnico(lista_de_atletas)
        time = [gol, zag, mei, atc, tec]
        time = self.formatar_time(time)
        time = self.ajuste_time(time)
        return time

    def formatar_time(self, time):
        time_formato = []
        for i in time:
            for jogador in i:
                dados = {
                    "posição": jogador['posicao'],
                    "nome": jogador['nome'],
                    "foto": jogador['foto_atleta'],
                    "pontuação":jogador['pontuacao'],
                    "time": jogador['id_clube'],
                    "escudo": jogador['id_clube'],
                    "nome_abreviado": jogador['nome_abreviado']
                }
            time_formato.append(dados)
        return time_formato
    
    def formacao(self, formacao_inp):
        if formacao_inp == 1:
            formacao ="3-4-3"
        elif formacao_inp == 2:
            formacao ="3-5-2"
        elif formacao_inp == 3:
            formacao ="4-3-3"
        elif formacao_inp == 4:
            formacao ="4-4-2"
        elif formacao_inp == 5:
            formacao ="4-5-1"
        elif formacao_inp == 6:
            formacao ="5-3-2"
        elif formacao_inp == 7:
            formacao ="5-4-1"
        else:
            print('Você escolheu um número fora das opções')    
            exit()
        return formacao
    #FALTA APENAS ESTA
    def ajuste_time(self, time):
        clubes = self.all_Clubes
        dados = {}
        for clube in clubes:
            for id, data in clube.items():
                dados[id] = {
                    'name': data['nome'],
                    'url': data['url do escudo']
                }
        print(dados)
        for atleta in time:
            time_id = str(atleta['time'])
            print(time_id)
            if time_id in dados.keys():

                #MUDAR AQUI PQ N SUPORTA
                time_id['time'] = dados[time_id]['name']
                time_id['escudo'] = dados[time_id]['url']
                print('bububu')
            else:
                print('nada')
        

        

if __name__ == "__main__":
    pass