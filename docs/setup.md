# Ambiente de desenvolvimento

> Nesse arquivo deve ter informações adicionais para o preparo do ambiente
> de desenvolvimento

## Linter Autopep8

Esse projeto utiliza algumas ferramentas para facilitar o desenvolvimento. O [autopep8](https://pypi.org/project/autopep8/) é o linter que será utilizado no decorrer do projeto.
Para utilizá-lo é preciso ter rodado o comando que instala os requirements:

```sh
pip install -r requirements.txt
```
Para utilizar o linter (com _agressive_ nível 2) em um arquivo é preciso rodar o comando:

```sh
autopep8 --in-place --aggressive --aggressive <nomedoarquivo>
```

Quanto mais ```--aggressive``` existirem no comando, mais irá aumentar o nível de "agressividade", ou seja, o quão "agressivas" serão as mudanças no código (como encurtar linhas e mudar x == True para x is True)

[Aqui](https://pypi.org/project/autopep8/#features) é possível visualizar os erros que o [autopep8](https://pypi.org/project/autopep8/) corrige.

## Configuração VSCode (opcional)

Se você usa o VSCode como editor, instale a seguinte extensão:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Após ter instalado a extensão do Python pressione Ctrl + Shift + P e selecione o comando ```Python: Select Linter``` 

![image](https://user-images.githubusercontent.com/44625056/183500631-fd7abd33-6af8-40cb-951c-24b6795285e6.png)

Escolha o linter que será utilizado (sugestão: pylint)

![image](https://user-images.githubusercontent.com/44625056/183500479-5374a721-a446-4806-a195-0d075f4a7dcb.png)

[Aqui](https://code.visualstudio.com/docs/python/linting) é possível ler mais sobre as configurações de linters no VSCode.
