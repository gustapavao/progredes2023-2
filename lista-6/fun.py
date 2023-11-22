import ssl, os

dir_atual = os.path.dirname(os.path.realpath(__file__))


invalidos = [':','/','*','?','"','<','>','|',"'",'.']

buffer = 4096

def conection_https(url_imagem,url_arq,url_host,sockt):

    request = f"GET {url_imagem} HTTP/1.1\r\nHost: {url_host}\r\nConnection: close\r\n\r\n"

    context = ssl.create_default_context()

    context.check_hostname = False          
    context.verify_mode = ssl.CERT_NONE 

    socket_rss_wrap = context.wrap_socket(sockt, server_hostname=url_host)
    socket_rss_wrap.connect((url_host, 443))
 
    print('Enviando requisição ao Servidor!')
    socket_rss_wrap.send(request.encode())
    print('Recebendo requisição e processando os bytes... Aguarde!')

    retorno_bin = b''
    while True:
        resposta = socket_rss_wrap.recv(buffer)
        if not resposta: break
        retorno_bin += resposta
        
   
    delimiter_img = '\r\n\r\n'.encode()
    position  = retorno_bin.find(delimiter_img)
    image     = retorno_bin[position+4:]               
    headers   = retorno_bin[:position].decode('utf-8') 
    
 
    position_header = headers.find('Content-Type')
    tipo_extensao = headers[position_header:].split()[1] 
    extensao_str = tipo_extensao.split('/')[-1] 
    extensao = '.' + extensao_str 

    sem_extensao = url_arq.split('.')

    if len(sem_extensao) == 1:
        url_arq = url_arq + extensao
    
    url_arq_txt   = sem_extensao[0]


    try:
        file_output = open(f'{dir_atual}\{url_arq}', 'wb')
    except:

        delim = url_arq.find(sem_extensao[-1])
        url_arq = url_arq[:delim]
  
        for char_troca in invalidos:
            url_arq = url_arq.replace(char_troca,'-')

        url_arq = url_arq + extensao

        file_output = open(f'{dir_atual}\{url_arq}', 'wb')

    file_output.write(image)
    file_output.close()
    print('Imagem salva com sucesso!')


    try:
        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')
    except:
 
        for char_troca in invalidos:
            url_arq_txt = url_arq_txt.replace(char_troca,'-')

        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')

    file_header.write(headers)
    file_header.close()
    print('Arquivo texto criado com sucesso!')

def conection_http(url_imagem,url_arq,url_host,sockt):

    url_request = f"GET {url_imagem} HTTP/1.1\r\nHost: {url_host}\r\nConnection: close\r\n\r\n"

    sockt.connect((url_host, 80))

 
    sockt.sendall(url_request.encode())
    

    retorno_bin = b""
  
    while True:
        data = sockt.recv(buffer)
        if not data:
            break
        retorno_bin += data

    delimiter_img = '\r\n\r\n'.encode()
    position  = retorno_bin.find(delimiter_img)
    image     = retorno_bin[position+4:] 
    headers   = retorno_bin[:position].decode('utf-8')
 
    position_header = headers.find('Content-Type')
    tipo_extensao = headers[position_header:].split()[1] 
    extensao_str = tipo_extensao.split('/')[-1]          
    extensao = '.' + extensao_str
    print(f'EXTENSAO do header: \n{extensao}')

    sem_extensao = url_arq.split('.')
    if len(sem_extensao) == 1:
        url_arq = url_arq + extensao
    
    url_arq_txt   = sem_extensao[0]
    try:
        file_output = open(f'{dir_atual}\{url_arq}', 'wb')
    except:
        delim = url_arq.find(sem_extensao[-1])
        url_arq = url_arq[:delim]
        for char_troca in invalidos:
            url_arq = url_arq.replace(char_troca,'-')
        url_arq = url_arq + extensao
        file_output = open(f'{dir_atual}\{url_arq}', 'wb')

    file_output.write(image)
    file_output.close()
    print('Imagem salva com sucesso!')

    try:
        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')
    except:
        for char_troca in invalidos:
            url_arq_txt = url_arq_txt.replace(char_troca,'-')
        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')

    file_header.write(headers)
    file_header.close()
    print('Arquivo texto criado com sucesso!')