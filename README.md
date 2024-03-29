# 2022.1_G4_FluxoAgil-server

<br />
<div align="center">
  <a href="#">
    <img src="docs/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h2 align="center">Fluxo Ágil Web</h2>

  <p align="center">
    Saiba qual é o fluxo de disciplinas mais rápido para você se formar na UnB!
    <br />
    <a href="#">Veja funcionando!</a>
    ·
    <a href="fluxoagil.herokuapp.com">Veja a documentação</a>
    ·
    <a href="https://github.com/UnBArqDsw2022-1/2022.1_G4_FluxoAgil-web/issues/new/">
      Reporte um bug</a>
  </p>
</div>

## Sobre o Fluxo Ágil

Fluxo Ágil é um aplicativo que recomenda um fluxo de disciplinas 
para estudantes de graduação da Universidade de Brasília baseado
em seu histórico acadêmico.

Esse é o repositório que hospeda o servidor da aplicação Fluxo Ágil.

## Montar ambiente de desenvolvimento

Clone o repositório e entre nele.

```sh
git clone https://github.com/UnBArqDsw2022-1/2022.1_G4_FluxoAgil-server
cd 2022.1_G4_FluxoAgil-server
```

Copie o arquivo `.env.dev`:

```sh
cp .env .env.dev
```

### Com Docker

Para subir o ambiente de desenvolvimento utilizando o docker, voce precisa ter o
[Docker](https://www.docker.com/) e o 
[Docker Compose](https://docs.docker.com/compose/install/) instalados em seu 
computador.

Então, para subir o servidor e o banco de dados, execute o comando abaixo:

```sh
docker-compose up --build -d
```

`-d` é flag para executar o container em modo dettached, ou seja, o terminal
vai voltar para o seu controle logo em seguida.

Se deu tudo certo, a API está disponível em http://localhost:5000.

Para derrubar os containeres execute:

```sh
docker-compose down
```

Se alguma coisa deu errado, verifique os logs:

```sh
docker logs fluxoagil-server
# ou
docker logs fluxoagil-db
```

### Sem Docker

Para subir o ambiente de desenvolvimento, você precisa ter
[Python](https://www.python.org/) na versão 3.10 instalado
em seu computador.

Instale os requirements

```sh
pip install -r requirements.txt
```

Inicie o servidor

```sh
python3 main.py
```

Veja se a API está funcionando executando o seguinte comando:

```sh
curl http://localhost:5000
```

Em seguida, siga o restante das [instruções](docs/setup.md) para completar a
configuração do seu ambiente de desenvolvimento.