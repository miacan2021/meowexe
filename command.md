pip freeze > requirements.txt
chmod +x ./entrypoint.sh
source venv/bin/activate  
docker-compose up -d --build
