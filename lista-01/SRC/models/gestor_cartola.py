import json
from gerenciar_arquivos import gerenciar_arquivos
class Cartola:
    def __init__(self, forma_time, ano):
        if ano == "2021":
            with open("/home/pavao/Desktop/Estudos/arquivos/dados_cartola_fc/cartola_fc_2021.txt", "r",) as file:
                data = json.load(file)
                #AJUSTAR PARA CONSEGUIR LER EM OUTROS COMPUTADORES
                file.close()
        elif ano == "2022":
            with open("/home/pavao/Desktop/Estudos/arquivos/dados_cartola_fc/cartola_fc_2022.txt", "r", encoding="utf-8") as file:
                data = json.load(file)
                file.close()
        self.ano = ano
        self.__clubes = self.clubes(data)
        self.__posicoes = self.posicoes(data)
        self.__atletas = self.atletas(data)
        formacao = self.formacao(forma_time)
        time = self.montar_time(formacao)
        self.format_print(time)
    
    @property
    def all_clubes(self):
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
            lista_de_clubes.append({clube_id: {"nome": values["nome"], "url do escudo": values["escudos"]["60x60"]}})
        return lista_de_clubes

    #@staticmethod ????
    def posicoes(self, data):
        posicoes = data["posicoes"]
        lista_de_posicoes = {}
        for id_pos, values in posicoes.items():
            lista_de_posicoes[id_pos] = {"posição": values["nome"]}
        return lista_de_posicoes
    
    def atletas(self, data):
        atletas = data["atletas"]
        lista_de_atletas = []
        for i in atletas:
            lista_de_atletas.append({"time": i["clube_id"], 
                                     "posicao": i["posicao_id"],
                                     "foto": i["foto"],
                                     "nome": i["nome"],
                                     "nome_abreviado": i["apelido_abreviado"],
                                     "pontuação": float(i["media_num"])*float(i["jogos_num"])})
        lista_de_atletas = sorted(lista_de_atletas, key = lambda d: d['pontuação'], reverse=True)
        return lista_de_atletas
    
    def escolher_zagueiro(self, formacao: str, lista_de_atletas):
        formacao = formacao.split("-")
        formacao_defesa = int(formacao[0])
        if formacao_defesa == 3:
            lateral = False
            zagueiro = []
            max_zag = 3
        elif formacao_defesa == 4:
            lateral = True
            max_zag = 2
            max_lat = 2
        elif formacao_defesa == 5:
            lateral = True
            max_zag = 3
            max_lat = 2
        else:
            print('Você informou uma formação inválida')
        contador_lateral = 0
        contador_zagueiro = 0
        if lateral:
            linha_de_defesa = []
            for jogador in lista_de_atletas:
                if jogador['posicao'] == 3:
                    linha_de_defesa.append(jogador)
                    contador_zagueiro += 1
                    if contador_zagueiro == max_zag: break
            for jogador in lista_de_atletas:
                if jogador['posicao'] == 2:
                    linha_de_defesa.append(jogador)
                    contador_lateral += 1
                    if contador_lateral == max_lat: break
            return linha_de_defesa

        elif lateral is False:
            for jogador in lista_de_atletas:
                if jogador['posicao'] == 3:
                    zagueiro.append(jogador)
                    if len(zagueiro) == max_zag:
                        break
            return zagueiro
    
    def escolher_meio(self, formacao: str, lista_de_atletas):
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
        lista_de_atletas = self.all_atletas
        zag = self.escolher_zagueiro(formacao, lista_de_atletas)
        mei = self.escolher_meio(formacao, lista_de_atletas)
        atc = self.escolher_atacante(formacao, lista_de_atletas)
        gol = self.escolher_goleiro(lista_de_atletas)
        tec = self.escolher_tecnico(lista_de_atletas)
        time = [gol, zag, mei, atc, tec]
        time = self.ajuste_time(time)
        return time

    def formacao(self, formacao_inp):
        if formacao_inp == 1:
            formacao = "3-4-3"
        elif formacao_inp == 2:
            formacao = "3-5-2"
        elif formacao_inp == 3:
            formacao = "4-3-3"
        elif formacao_inp == 4:
            formacao = "4-4-2"
        elif formacao_inp == 5:
            formacao = "4-5-1"
        elif formacao_inp == 6:
            formacao = "5-3-2"
        elif formacao_inp == 7:
            formacao = "5-4-1"
        else:
            print('Você escolheu um número fora das opções')    
            exit()
        return formacao
    
    def ajuste_time(self, time):
        clubes = self.all_clubes
        posicoes = self.all_posicoes
        dados_times = {}
        for clube in clubes:
            for id_, data in clube.items():
                dados_times[id_] = {
                    'time': data['nome'],
                    'escudo': data['url do escudo']
                }
        time_with_teams = []
        for i in time:
            for atleta in i:    
                time_id = str(atleta['time'])
                aux = dados_times.get(time_id)
                if aux:
                    atleta_with_team = atleta.copy()
                    atleta_with_team.update(aux)
                    time_with_teams.append(atleta_with_team)
        print(time_with_teams)
        team = []
        for atleta in time_with_teams:
            posicao = str(atleta['posicao'])
            aux = posicoes.get(posicao)
            if aux:
                atleta_with_pos  = atleta.copy()
                atleta_with_pos.update(aux)
                team.append(atleta_with_pos)
        return team
    
    def format_print(self, time):
        jogadores = []
        for enum, i in enumerate(time):
            nome = i.get("nome_abreviado")
            posicao = i.get("posição")
            team = i.get("time")
            pontos = i.get("pontuação")
            jogador = f"""{enum+1} - Posição: {posicao}, 
                    Nome: {nome}, 
                    Time: {team}, 
                    Pontuação Total: {pontos}"""
            print(jogador)
            jogadores.append(jogador)
        while True:
            opcao_salvar = input('Você gostaria de salvar? (y/n)').lower()
            if opcao_salvar == "y":
                jogadores = self.format_save(time)
                gerenciar_arquivos.salvar_lista_em_txt(jogadores, self.ano)
                break
            elif opcao_salvar == "n":
                break
            else:
                print("Opção inválida")
            
    def format_save(self, time):
        jogadores = []
        for enum, i in enumerate(time):
            nome = i.get("nome_abreviado")
            posicao = i.get("posição")
            team = i.get("time")
            pontos = i.get("pontuação")
            foto = i.get("foto")
            escudo = i.get("escudo")
            jogador = f"""{enum+1} - Posição: {posicao}, 
                    Nome: {nome},
                    Url da foto: {foto},
                    Pontuação Total: {pontos}, 
                    Time: {team},
                    Escudo: {escudo}"""
            jogadores.append(jogador)
        return jogadores

        

if __name__ == "__main__":
    print('Olá, eu irei montar a sua seleção')