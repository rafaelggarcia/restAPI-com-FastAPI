# Teste prático. 

**Instruções para executar a API: **

* Para rodar a API é necessário que tenha o Python instalado na sua máquina, caso ainda não tenha, você pode baixar por [aqui](https://www.python.org/downloads/).
* Faça o download da pasta completa e extraia os arquivos caso esteja compactada.
* Abra o terminal na pasta onde o projeto está instalado.
* Digite o comando `venv\Scripts\activate`
* Caso tenha problemas de permissão execute `Set-ExecutionPolicy Unrestricted -Scope Process` e depois o comando acima de ativação novamente.
* Caso não consiga acessar o ambiente virtual, pode executar o comando `pip install -r requirements.txt` 
* Logo em seguida podemos executar a API com o comando `uvicorn main:app --reload` 
* Clique no link gerado pelo terminal ou acesse `http://127.0.0.1:8000` no seu navegador.

**A partir desse momento, a API já está sendo executada na rota raiz, abaixo segue as instruções para utiliza-lá:**

**Instruções para utilizar a API:**

* Entre no link   `http://127.0.0.1:8000/docs` para realizar os testes de maneira mais simples.

* Primeiramente, você deve sempre criar a competição na qual irá inserir os dados. Há 2 competições com condições especiais, são elas *"corrida100m"*  e *"dardo"*. 

  *  **Condições para *"Dardo"* **

    * No momento em que for cadastrar o atleta na competição dardo, ele terá 3 tentativas e elas deverão ser inseridas no formato de lista no campo *"value"*  onde será pego apenas a melhor das tentativas (com o valor mais alto), por exemplo:     

      ``` 
        {
        "competicao": "dardo",
        "atleta": "José das Couves",
        "value": [70.8, 67.9, 74.2],
        "unidade": "string"
      }  					
      ```

  * **"Condição "corrida100m"**
    * A competição "corrida100m" é a única na qual será ordenado o ranking pelo menor valor, ou seja o campeão será oque tiver menor tempo. 

* Qualquer outra competição criada que não seja "corrida100m" o ranking será feito pelo maior valor. 
* A qualquer momento pode ser solicitado o ranking da competição, basta que aja atletas cadastrados nela.
* Para fechar a competição basta inserir o mesmo nome da competição que foi aberta.
* A competição só aceitará os dados caso já tenha sido criada e ainda esteja aberta.
* Não é possível abrir a competição novamente após fechada.
* Para iniciar uma nova competição que já foi encerrada como "dardo" ou "corrida100m" é necessário executar o arquivo *delete.py* para a base de dados seja limpa. 
* Em nenhum momento devem ser inseridos 2 atletas com o mesmo nome, isso causará duplicidade no ranking.

Quaisquer demais dúvidas podem ser tiradas comigo através do e-mail *rafael.garcia@luizalabs.com.br*.

Atenciosamente,

