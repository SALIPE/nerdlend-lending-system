#!/bin/sh
STAGE=$2
USER=$3
#Remove old content
ssh $USER@$1 "rm -r dts/$STAGE"
ssh -o StrictHostKeyChecking=no $USER@$1 "mkdir -p dts/$STAGE"

# Copiar o docker-compose.yml para o servidor remoto via SCP
scp docker-compose.$STAGE.yml a61491@$1:/home/$USER/dts/$STAGE/
scp docker-compose.yml a61491@$1:/home/$USER/dts/$STAGE/

scp .env $USER@$1:/home/$USER/dts/$STAGE/
scp db.sql $USER@$1:/home/$USER/dts/$STAGE/

# Executar o deploy no servidor remoto via SSH
# ssh echo "$3" | docker login $REGISTRY -u student --password-stdin
ssh $USER@$1 "cd dts/$STAGE && docker compose -f docker-compose.yml -f docker-compose.$STAGE.yml pull"
ssh $USER@$1 "cd dts/$STAGE && docker compose -f docker-compose.yml -f docker-compose.$STAGE.yml up --build -d"

