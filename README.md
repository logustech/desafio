## Regras

- Faça um código em <strong>NodeJS</strong> ou
  <strong>Python3</strong> que deverá consumir os dados do <i>[SGBD MySQL](#acesso-ao-banco-de-dados)</i>, formatar os dados e enviar um <i>POST </i> para:
  <a>http://desafio.logus.tech/desafio</a>
  
- Este é um exemplo da formatação do POST a ser enviado:


{
  "data": [{
    "date": "06/08/2019 19:15",
    "teams": "Sport Recife x Santa Cruz",
    "away": "5.8",
    "home": "1.90"
  }], // Dados formatados
  "email": "email@email.com" // Seu email
}

Se tudo ocorreu bem, você pode conferir o seu resultado e de outros participantes [neste link](http://desafio.logus.tech)

- No campo email do POST deverá ser colocacado o mesmo email que
  usará para enviar o seu currículo.

- Após finalizar o código e testar o POST, não é necessário emitir mais testes. Você deverá fazer um fork e dar um pull request para este repositório

- Agora envie seu currículo para o email <strong>ti@logus.tech</strong>
## Acesso ao banco de dados
  ```
  host: desafio.logus.tech

  usuário: desafio
  senha: desafio
  porta: 3306
 ```
