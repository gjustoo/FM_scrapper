docker container stop fm_scrapper_python car_scrapper_mongodb && docker container rm fm_scrapper_python car_scrapper_mongodb

docker rmi fm_scrapper_fm_scrapper:latest 
docker rmi fm_scrapper_python:latest

sudo rm -rfd data/

docker-compose up -d --force-recreate

echo rebuilt
