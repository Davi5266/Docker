#### Rotas
###### client
<p>responsavel pelo registro de clientes e o fornecimento de autenticação</p>

- Register
```
/client/register
```
Gera o cadastro de usário á API, criptografando senha e armazenando ao banco de dados.

- Login
```
/client/login
```
Verifica se o cliente existe, caso o cliente exista e as credencias fornecidas são compativeis, retorna um token no qual permite o acesso de rotas privadas, no qual se encontra o registro de dados do DHT.
###### dht
<p>Rota responsavel por armazenar informações do sensor DHT fornecidos pelo cliente</p>
