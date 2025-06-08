FROM python:3.9-slim

# Sistem paketleri
RUN apt-get update && apt-get install -y build-essential libpq-dev && apt-get clean

# Çalışma dizini
WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodları kopyala
COPY . .
EXPOSE 8001

# Sadece main.py'yi çalıştır
CMD ["python", "main.py"]