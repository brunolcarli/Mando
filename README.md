<table align="center"><tr><td align="center" width="9999">

<img src="https://cnet1.cbsistatic.com/img/7M_ubOowKkJI8kGjiSPg32XDVOY=/1092x0/2019/11/11/c976fe6d-ed33-469a-8e64-b79794fcae45/mandalorian-disney-02.jpg" align="center" width="300" alt="Project icon">

# Mando

### Discord Bot

![](https://badgen.net/badge/icon/discord?icon=discord&label)
[![Wiki badge](https://badgen.net/badge/docs/github_wiki?icon=github)](https://github.com/brunolcarli/Mando/wiki)
![Generic badge](https://img.shields.io/badge/version-0.0.3-green.svg)
![Generic badge](https://img.shields.io/badge/docs_lang-PT_BR-darkgreen.svg)
![Generic badge](https://img.shields.io/badge/code_lang-English-darkgreen.svg)
[![Run on Repl.it](https://repl.it/badge/github/brunolcarli/Mando)](https://repl.it/github/brunolcarli/Mando)

</td></tr></table>

# Instalando e rodando

## Dependências mínimas:

```
Python >=3.4.3 || <=3.6.6
Conta no Discord
```

Crie uma aplicação no Discord, você precisará gerar um `token` para utilizar o seu bot nos servidores Discord.

Poderá seguir [este tutoral](https://medium.com/@moomooptas/how-to-make-a-simple-discord-bot-in-python-40ed991468b4) para fazer isto.

Assim que tiver gerado seu `token` e dado acesso ao bot via página do Discord Developers, crie na raiz deste projeto um arquivo chamado `.env` e nele insira seu token desta forma:


```
TOKEN=dgyausgdhuisegfdyuesnciosbedtyfvdsvufsuydtfcgjksgfdytsd
```


## Rodando Localmente

![Linux Badge](https://img.shields.io/badge/OS-Linux-black.svg)
![Apple badge](https://badgen.net/badge/OS/OSX/:color?icon=apple)

Crie um ambiente virtual ([virtualenv](https://docs.python-guide.org/dev/virtualenvs/)) para a instalação das dependências


- Instale os requirements executando:

    + Se for instalar em modo desenvolvedor:
        ```
        $ make dev_install
        ```

    + Se for somente rodar o bot:
        ```
        $ make install
        ```

Assim que as dependências tiverem sido instaladas execute:

```
$ make run
```

Uma mensagem `Ready!` será exibida informando que o bot está executando.

<hr />

<img src="https://badgen.net/badge/OS/Windows/:color?icon=windows">

Certifique-se de possuir o `pip` installado sobre uma das versões do Python apresentadas nas depndências do projeto:

```
$ pip --version
```

Instale os requirements:

- Se for instalar em modo desenvolvedor:

    ```
    $ pip install -r requirements/development.txt
    ```

- Se for somente rodar o bot:
    ```
    $ pip install -r requirements/common.txt
    ```

Execute o bot com:

```
$ python main.py
```

# Docker

`Em desenvolvimento`
