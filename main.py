import re

# Lista global para armazenar os usuários cadastrados

usuarios = []

def validar_username(username):
    if len(username) < 3:
        return False, "Username deve ter pelo menos 3 caracteres."
    return True, ""

def validar_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.match(regex, email):
        return False, "Email inválido."
    return True, ""

def validar_senha(senha):
    if len(senha) < 6:
        return False, "Senha deve ter pelo menos 6 caracteres."
    return True, ""

def validar_celular(celular):
    regex = r'^\+?1?\d{9,15}$'
    if not re.match(regex, celular):
        return False, "Número de celular inválido."
    return True, ""

def validar_time_preferido(time_preferido):
    if not time_preferido:
        return False, "Time preferido não pode ser vazio."
    return True, ""

def cadastrar_usuario(username, email, senha, celular, time_preferido):
    validadores = [
        validar_username(username),
        validar_email(email),
        validar_senha(senha),
        validar_celular(celular),
        validar_time_preferido(time_preferido)
    ]
    
    for valido, mensagem in validadores:
        if not valido:
            return f"Erro no cadastro: {mensagem}"
    
    usuarios.append({
        "username": username,
        "email": email,
        "senha": senha,
        "celular": celular,
        "time_preferido": time_preferido
    })
    
    return "Cadastro realizado com sucesso!"

def login_usuario(email, senha):
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return "Login realizado com sucesso!"
    return "Email ou senha incorretos."

# Exemplo de uso
"""print("\nTestes de cadastro e login de usuários:\n")
resultado_cadastro = cadastrar_usuario("user123", "email@exemplo.com", "senha123", "+5511999999999", "Time X")
print(resultado_cadastro)

resultado_login = login_usuario("email@exemplo.com", "senha123")
print(resultado_login)

resultado_login_falha = login_usuario("email@exemplo.com", "senha_errada")
print(resultado_login_falha)"""

# Posts

# Lista global para armazenar os posts
posts = []

# Variável global para rastrear o ID dos posts
post_id = 1

def postar_mensagem(mensagem):
    global post_id
    post = {
        "id": post_id,
        "mensagem": mensagem,
        "likes": 0,
        "comentarios": []
    }
    posts.append(post)
    post_id += 1
    return post

def curtir_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            post["likes"] += 1
            return f"Post {post_id} curtido com sucesso! Total de likes: {post['likes']}"
    return "Post não encontrado."

def comentar_post(post_id, comentario):
    for post in posts:
        if post["id"] == post_id:
            post["comentarios"].append(comentario)
            return f"Comentário adicionado ao post {post_id} com sucesso! Comentários: {post['comentarios']}"
    return "Post não encontrado."

# Exemplo de uso

"""print("\nTestes de posts:\n")
post1 = postar_mensagem("Esta é a minha primeira mensagem.")
print(post1)

post2 = postar_mensagem("Esta é a minha segunda mensagem.")
print(post2)

resultado_curtir = curtir_post(1)
print(resultado_curtir)

resultado_comentar = comentar_post(1, "Este é o meu primeiro comentário.")
print(resultado_comentar)

resultado_comentar = comentar_post(1, "Este é o meu segundo comentário.")
print(resultado_comentar)

resultado_comentar = comentar_post(2, "Comentário no segundo post.")
print(resultado_comentar)

resultado_comentar = comentar_post(3, "Comentário em um post não existente.")  # Post não existente
print(resultado_comentar)"""

# Comunidade

# Lista global para armazenar as comunidades
comunidades = []

# Variável global para rastrear o ID das comunidades
comunidade_id = 1

def criar_comunidade(nome, tema):
    global comunidade_id
    
    for comunidade in comunidades:
        if comunidade["nome"] == nome:
            return "Erro: Já existe uma comunidade com esse nome."
    
    nova_comunidade = {
        "id": comunidade_id,
        "nome": nome,
        "tema": tema,
        "users": []
    }
    comunidades.append(nova_comunidade)
    comunidade_id += 1
    return f"Comunidade '{nome}' criada com sucesso! ID: {nova_comunidade['id']}"

def entrar_comunidade(nome_comunidade, nome_usuario):
    for comunidade in comunidades:
        if comunidade["nome"] == nome_comunidade:
            if nome_usuario in comunidade["users"]:
                return f"Erro: Usuário '{nome_usuario}' já está na comunidade '{nome_comunidade}'."
            comunidade["users"].append(nome_usuario)
            return f"Usuário '{nome_usuario}' entrou na comunidade '{nome_comunidade}' com sucesso!"
    return f"Erro: Comunidade '{nome_comunidade}' não encontrada."

def sair_comunidade(nome_comunidade, nome_usuario):
    for comunidade in comunidades:
        if comunidade["nome"] == nome_comunidade:
            if nome_usuario not in comunidade["users"]:
                return f"Erro: Usuário '{nome_usuario}' não está na comunidade '{nome_comunidade}'."
            comunidade["users"].remove(nome_usuario)
            return f"Usuário '{nome_usuario}' saiu da comunidade '{nome_comunidade}' com sucesso!"
    return f"Erro: Comunidade '{nome_comunidade}' não encontrada."

# Exemplo de uso
"""print("\nTestes de comunidades:\n")
resultado_comunidade1 = criar_comunidade("Comunidade da Mahindra", "Equipes de Fórmula E")
print(resultado_comunidade1)

resultado_comunidade2 = criar_comunidade("Acelerados", "Apaixonados por velocidade")
print(resultado_comunidade2)

resultado_comunidade3 = criar_comunidade("Comunidade da Mahindra", "Equipes de Fórmula E")  # Nome duplicado
print(resultado_comunidade3)

resultado_entrar1 = entrar_comunidade("Comunidade da Mahindra", "user1")
print(resultado_entrar1)

resultado_entrar2 = entrar_comunidade("Comunidade da Mahindra", "user2")
print(resultado_entrar2)

resultado_entrar3 = entrar_comunidade("Comunidade da Mahindra", "user1")  # Usuário duplicado
print(resultado_entrar3)

resultado_entrar4 = entrar_comunidade("Comunidade Inexistente", "user1")  # Comunidade não existente
print(resultado_entrar4)

resultado_sair1 = sair_comunidade("Comunidade da Mahindra", "user1")
print(resultado_sair1)

resultado_sair2 = sair_comunidade("Comunidade da Mahindra", "user1")  # Usuário não está na comunidade
print(resultado_sair2)

resultado_sair3 = sair_comunidade("Comunidade Inexistente", "user1")  # Comunidade não existente
print(resultado_sair3)"""