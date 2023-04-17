# PYTHON SCRAPPER



## Installation

``` sh ./rebuild.sh ```

Beware that this will delete all data in the database, and rebuild the image. Root access may be asked for.



### Helpful commands

- ``` docker system prune ``` -> deletes all containers and images
- ``` docker build --no-cache=true -t fm_scrapper_python . ``` -> builds image
- ``` docker-compose up -d ``` -> starts containers
- ``` docker container logs fm_scrapper_python ``` -> shows logs
- ``` docker exec -it fm_scrapper_python /bin/bash ``` -> opens bash in container
- ``` docker container stop fm_scrapper_python car_scrapper_mongodb && docker container rm fm_scrapper_python car_scrapper_mongodb ``` -> stops and deletes containers
- ``` docker rmi fm_scrapper ``` -> deletes image

- ``` sudo rm -rfd data/ ``` -> deletes data folder
- ``` docker-compose build --no-cache ``` -> rebuilds the image
