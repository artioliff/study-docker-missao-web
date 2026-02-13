# 1. BASE: Do que nossa nave é feita?
# Usamos Python novamente.
FROM python:3.9-slim

# 2. LOCAL: Onde vamos trabalhar dentro da nave?
WORKDIR /app

# 3. SUPRIMENTOS: O que precisamos levar?
# Primeiro copiamos a lista de compras (requirements.txt).
COPY requirements.txt .

# 4. PREPARAÇÃO: Instalando os equipamentos.
# O `pip` é o instalador do Python. Ele lê a lista e instala o Flask.
RUN pip install -r requirements.txt

# 5. CARGA: Colocando o resto das coisas na nave.
# Copiamos todo o resto (app.py e a pasta templates).
COPY . .

# 6. PORTA: Por onde a nave se comunica?
# O Flask usa a porta 5000. Estamos avisando o Docker sobre isso.
EXPOSE 5000

# 7. DECOLAR: O comando final.
CMD ["python", "app.py"]
