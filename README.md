
# RNB - Random Number Generator

RNB (Random Number Generator) é uma aplicação web simples que permite gerar números aleatórios. Por padrão, a aplicação gera números aleatórios entre 1 e 100, mas você também pode escolher gerar números entre 1 e 18.

## Funcionalidades

- **Gerar Números Aleatórios:** Clique no botão "Gerar Número" para gerar um número aleatório.
- **Escolha do Intervalo:** Use o seletor para escolher entre gerar números de 1 a 100 ou de 1 a 18.

## Tecnologias Utilizadas

- **Flask:** Framework web usado para construir a aplicação backend.
- **HTMX:** Biblioteca para permitir interações dinâmicas sem a necessidade de escrever JavaScript personalizado.
- **Docker:** Ferramenta usada para criar contêineres que facilitam o empacotamento e a execução da aplicação.

## Como Executar a Aplicação

### Pré-requisitos

Certifique-se de que o Docker esteja instalado no seu sistema. Se ainda não tiver o Docker instalado, você pode baixá-lo [aqui](https://www.docker.com/products/docker-desktop).

### Passos para Rodar a Aplicação com Docker

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/rnb.git
   cd rnb
   ```

2. **Construir a imagem Docker:**

   Na raiz do projeto, execute o seguinte comando para construir a imagem Docker:

   ```bash
   docker build -t rnb-app .
   ```

3. **Rodar o contêiner:**

   Para rodar a aplicação, execute:

   ```bash
   docker run --name rnb-app-container -p 5000:5000 rnb-app
   ```

   Isso irá iniciar o contêiner e mapear a porta 5000 do contêiner para a porta 5000 do host.

4. **Acessar a aplicação:**

   Abra seu navegador e acesse `http://localhost:5000`. Você verá a interface do RNB para gerar números aleatórios.

### Gerenciamento do Contêiner

- **Parar o contêiner:**

  Para parar a aplicação, execute:

  ```bash
  docker stop rnb-app-container
  ```

- **Reiniciar o contêiner:**

  Para reiniciar o contêiner sem criar um novo, execute:

  ```bash
  docker start rnb-app-container
  ```

- **Remover o contêiner:**

  Se você quiser remover o contêiner, execute:

  ```bash
  docker rm rnb-app-container
  ```

### Usando Docker com Remoção Automática

Se preferir criar e remover automaticamente o contêiner a cada execução, use o seguinte comando:

```bash
docker run --rm -p 5000:5000 rnb-app
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e novas funcionalidades.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
