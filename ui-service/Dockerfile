FROM python:3.9-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gereken dosyaları kopyala
COPY requirements.txt .
COPY . .

# Gerekli Python paketlerini yükle
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit'in dışarıdan erişilebilmesi için port aç
EXPOSE 8501

# Uygulamayı çalıştır
CMD ["streamlit", "run", "src/ui_marketting.py", "--server.port=8501", "--server.address=0.0.0.0"]