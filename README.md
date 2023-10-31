# Removedor de Silêncio

Olá, fico feliz por estar utilizando meu programa para as suas edições
maravilhosas.
Neste readme, eu irei ensiná-los como utilizar o programa, embora ele seja
intuitivo.

Primeiramente, gostaria de pedir à vocês que compartilhem este programa com os
seus amigos, colegas e conhecidos que trabalham nessa área. Pois, o intuito
deste programa foi acelerar o trabalho de vocês na hora de editar os seus
vídeos. Além disso, gostaria que me seguissem no meu instagram e enviassem uma
mensagem para mim falando sobre a sua experiência com o programa e, claro, se
tiver algum problema, pode falar comigo.

Afinal, esses feedbacks são essenciais para os meus futuros aplicativos. Além
disso, como disse antes, eu crio esse aplicativos para facilitar a vida das
pessoas.

Seguimos com o tutorial, apesar de não precisar, rs.

# Como usar
Você pode usar o programa abrindo o executável pronto ou configurando o python
em seu computador, após isso:

1. Selecione o vídeo.

2. Selecione a pasta para onde você deseja exportar o vídeo.

3. Selecione a opção desejada.


# Para executar diretamente do código ou alterar o programa

## No linux é necessário instalar o tkinter dessa maneira
```bash
sudo apt install python3-tk
```

## Crie um ambiente virtual em uma pasta
```bash
python3 -m venv .venv
```

## Ative o ambiente virtual
### No Linux
```bash
source .venv/bin/activate
```
### No windows
```bash
source .venv/Scripts/activate
```
## Atualize o PIP que está instalado dentro desse novo ambiente virtual
```bash
python -m pip install --upgrade pip
```

## Instale as bibliotecas a partir do arquivo `requirements.txt`
```bash
pip install -r requirements.txt
```

## Se você chegou até aqui agora é só executar o programa
```bash
python RemovedorGUI.py
```
