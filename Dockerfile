FROM python:3

workdir /app

COPY . .

run pip install -r requirements.txt 

run comando do S.O 

CMD{"python", "imc.py"} -- executa x comandos quando o container roda

expose 80 -- expoe a porta