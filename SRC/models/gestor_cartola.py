class Cartola:
    def __init__(self, data):
        self.clubes(data)
    
    
    
    def clubes(data):        
        clubes = data["clubes"]
        lista_de_clubes = []
        for clube_id, values in clubes.items():
            lista_de_clubes.append({f"{clube_id}":{"nome":{values["nome"]},"url do escudo": {values["escudos"]["60x60"]}}})
        return lista_de_clubes
    
    def posicoes(data):
        posicoes = data["posicoes"]
        lista_de_posicoes = []
        for id_pos, values in posicoes.items():
            lista_de_posicoes.append({id_pos:{"nome":values["nome"]}})
        return lista_de_posicoes
    
    def atletas(data):
        atletas = data["atletas"]
        lista_de_atletas = []
        for i in atletas:
            lista_de_atletas.append({i["atleta_id"]:{
                                           "id_clube": i["clube_id"], 
                                           "posicao":i["posicao_id"], 
                                           "foto_atleta":i["foto"],
                                           "nome":i["nome"], 
                                           "nome_abreviado":i["apelido_abreviado"],
                                           "pontuacao": float(i["media_num"])*float(i["jogos_num"])
                                           }}
                                           )
