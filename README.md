
# RNB - Random Number Generator

RNB (Random Number Generator) é uma aplicação web minimalista desenvolvida para gerar números aleatórios. Por padrão, a aplicação gera números aleatórios entre 1 e 18, mas você pode escolher qualquer intervalo desejado através dos campos de entrada.

## Funcionalidades

- **Gerar Números Aleatórios:** Clique no botão "Gerar Número" para gerar um número aleatório.
- **Escolha do Intervalo:** Use os campos de texto para definir o intervalo desejado.

## Tecnologias Utilizadas

- **Streamlit:** Framework usado para construir a aplicação frontend e backend.
- **Docker:** Ferramenta usada para criar contêineres que facilitam o empacotamento e a execução da aplicação.
- **Docker Compose:** Ferramenta para definir e gerenciar aplicativos Docker multi-contêiner.

## Como Executar a Aplicação

### Pré-requisitos

Certifique-se de que o Docker e o Docker Compose estejam instalados no seu sistema. Se ainda não tiver o Docker instalado, você pode baixá-lo [aqui](https://www.docker.com/products/docker-desktop).

### Passos para Rodar a Aplicação com Docker Compose

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/rnb.git
   cd rnb
   ```

2. **Construir e rodar o contêiner:**

   Para construir a imagem e rodar o contêiner, execute:

   ```bash
   docker-compose up --build
   ```

   Isso irá construir a imagem nomeada como `rnb-app:latest` e iniciar o contêiner. A porta 8000 do contêiner será mapeada para a porta 8000 do host, mas você pode alterar essa porta no arquivo `docker-compose.yml` se necessário.

3. **Acessar a aplicação:**

   Abra seu navegador e acesse `http://localhost:8000`. Você verá a interface do RNB para gerar números aleatórios.

### Gerenciamento do Contêiner com Docker Compose

- **Parar o contêiner:**

  Para parar a aplicação, execute:

  ```bash
  docker-compose down
  ```

  Isso irá parar e remover o contêiner.

- **Rodar novamente sem reconstruir:**

  Se você não fez alterações significativas que exigem a reconstrução da imagem, pode rodar a aplicação novamente com:

  ```bash
  docker-compose up
  ```

- **Rebuildar a imagem:**

  Se fizer alterações no Dockerfile ou em arquivos fora do diretório `src`, será necessário rebuildar a imagem:

  ```bash
  docker-compose up --build
  ```

## Contribuições

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:
- Faça um fork deste repositório.
- Crie uma branch para sua feature ou correção (`git checkout -b feature/nome-da-feature`).
- Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
- Faça o push para a branch (`git push origin feature/nome-da-feature`).
- Abra um Pull Request.

Sinta-se à vontade para abrir issues e pull requests para melhorias e novas funcionalidades.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
