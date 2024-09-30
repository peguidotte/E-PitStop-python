# Projeto de Simulação de Rede Social

Este projeto é uma simulação de uma rede social onde os usuários podem se cadastrar, fazer login, postar mensagens, curtir posts, comentar em posts, criar comunidades, entrar em comunidades e sair de comunidades.

## Instalação

Para configurar o ambiente e executar o projeto, siga os passos abaixo:

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd seu-repositorio
    ```
3. (Opcional) Crie um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```
4. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```

## Navegação pelo Projeto

A estrutura do projeto é a seguinte:


- [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Flabsfiap%2FDocuments%2FGitHub%2FE-PitStop-python%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%225a3b28f7-07a0-4224-b720-3c1942153b3c%22%5D "c:\Users\labsfiap\Documents\GitHub\E-PitStop-python\main.py"): Contém todas as funções principais para a simulação da rede social, incluindo cadastro de usuários, login, postagem de mensagens, curtidas, comentários, criação de comunidades, entrada e saída de comunidades.

## Simulação

### Cadastro de Usuário

Para cadastrar um usuário, utilize a função `cadastrar_usuario` que recebe `username`, `email`, `senha`, `celular` e `time_preferido`.

### Login de Usuário

Para fazer login, utilize a função `login_usuario` que recebe `email` e `senha`.

### Postagem de Mensagens

Para postar uma mensagem, utilize a função `postar_mensagem` que recebe uma `mensagem`.

### Curtir Posts

Para curtir um post, utilize a função `curtir_post` que recebe o `post_id`.

### Comentar em Posts

Para comentar em um post, utilize a função `comentar_post` que recebe o `post_id` e um `comentario`.

### Criação de Comunidades

Para criar uma comunidade, utilize a função `criar_comunidade` que recebe `nome` e `tema`.

### Entrar em Comunidades

Para entrar em uma comunidade, utilize a função `entrar_comunidade` que recebe `nome_comunidade` e `nome_usuario`.

### Sair de Comunidades

Para sair de uma comunidade, utilize a função `sair_comunidade` que recebe `nome_comunidade` e `nome_usuario`.

### Criador do código
[Pedro Guidotte](https://github.com/peguidotte/)