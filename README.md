# HVL
DESKTOP FIREBASE

#

Como baixar o projeto:

Vai baixar Git dps volta. Se tiver dúvidas, leia o glossário ou chama o vitor no teams ou disc.

  Windows: 
  obs.: evita espaço, números, acentos e sinais, se tiver que dar espaço usa underscore ["_"], e se possível minusculo.

  Crie uma pasta no desktop

  abra o terminal
  vamos para dentro dela, digite:

    cd ~/Desktop/NomeDaPasta

  seu prompt deve ficar parecido com isso

    < C:\Users\NomeDoUsuario\Desktop\NomeDaPasta>

  se não funcionar vc pode usar o comando ls (list) pra ver o que tem na pasta atual ou "cd .." pra voltar uma pasta

  Linux: 

  abra o terminal e digite:

    cd ~/Desktop
    mkdir NomeDaPasta
    cd NomeDaPasta

Agora dentro da pasta, digite:

  git clone https://github.com/GabrielOliveiraSousa/HVL.git .

  (o ponto extra no final é pra clonar o projeto na pasta atual, caso contrário ele cria outra pasta dentro dessa).

Vamos criar uma branch separada pra não ter como fazer besteira kkkk

  git checkout -b NomeDaBranch (escolhe um nome ai)

exemplo:

  git checkout -b branchLucas

agora coda a vontade, pra subir depois pelo terminal (pode usar no vscode msm se preferir, isso aqui é alternativa):

  git add .
  git commit -m "Descrição das mudanças"
  git push -u origin NomeDaBranch

os proximos pushs podem ser só:
  git push origin NomeDaBranch




Pra rodar o DB:

Abre o vscode e o terminal do vscode. Olha o prompt, se você não estiver na pasta, chega nela usando cd e digite:

vamos criar um ambiente virtual pra não termos problemas de versão mais tarde:

  python -m venv NomeDoAmbiente
  (nomes comuns: venv, env, myenv, .venv(linux, pasta inv))

com ele criado, vamos usá-lo:

  WINDOWS:

    .\env\Scripts\activate

  ou

    .\env\Scripts\Activate.ps1

  Linux:

  source env/bin/activate

Atrás do prompt deve ter aparecido o nome da pasta do env, ex.:

(myenv) vitor@vitorlinux:~/Desktop$    ---

(caso precise usar o terminal de novo, é possível sair do venv escrevendo "deactivate")

pra instalar os pacotes necessários:

  pip install -r requirements.txt

Para criar uma secretAccountKey e acessar o Firebase:

Acesse https://console.firebase.google.com/u/1/project/hvlgg1/overview?hl=pt-br

No canto superior esquerdo, logo abaixo do ícone do firebase, clique na Engrenagem e em "Configurações do Projeto".

Em "Contas de serviço", você tem a opção de gerar uma nova chave.
Selecione a Linguagem "Python", clique em "Gerar nova chave privada".
Renomeie esse arquivo para "secretAccountKey.json".

Agora é só trocar a secretAccountKey que você tem no projeto pela que você acabou de gerar.

Com pacotes instalados e sua própria secretAccountKey, rode o programa:

  python3 firebaseDBTEST.py

  (obs.: eu ainda não tenho certeza de como usar todos os comandos, toda vez que alguém roda isso, cria-se dois usuários no firebase com IDs únicos. fica à vontade pra deletar por código ou manualmente no site.)



CUSTOMTKINTER
Para instalar o custom tkinter precisa apenas executar este comando
  pip install customtkinter
E pronto, agora será possíver ver as telas criadas

Glossário

cd:
change directory ou mudar de pasta. Pode se usar:
"cd .." pra voltar uma pasta,
"cd ../.." para voltar duas pastas,
"cd /" para voltar ao root do pc,
"cd ~" para ir até a pasta do usuário atual.

ls:
list. lista o conteúdo da pasta atual. Pode se usar:
"ls -a" para ver pastas invisíveis.

prompt:
A linha atrás do que vc ta digitando no terminal. É a interface pra executar comandos via texto.

-r:
Instalar a partir de um arquivo.

-m:
roda o modulo como um script (não tenho a menor ideia do que seja, atualizar mais tarde).

-u:
(--set-upstream): git vai lembrar da branch remota e você não vai precisar especificar toda vez que usar git push/pull (atualizar mais tarde). 

venv:
Ambiente virtual(Virtual Environment): ambiente isolado para evitar conflitos e gerenciar depedências específicas de projetos.
