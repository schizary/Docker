# Docke
docker build -t meu_site 

docker run --name site-d -p 80:80 meu_site

docker ps

docker tag meu_site:latest rodrigovollo/aulafatec_2025:meu_site

docker run rodrigovollo/aulafatec_2025:meu_site
