# Use a imagem base do Node.js para compilar a aplicação
FROM node:16 AS builder

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie apenas os arquivos de dependência
COPY package.json package-lock.json ./

# Instale as dependências
RUN npm install

# Copie o restante do código da aplicação
COPY . .

# Compile a aplicação para produção
RUN npm run build

# Use uma imagem leve para o servidor
FROM nginx:1.21

# Copie os arquivos estáticos compilados para o diretório do Nginx
COPY --from=builder /app/build /usr/share/nginx/html

# Copie a configuração personalizada do Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000
# Comando padrão para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]
