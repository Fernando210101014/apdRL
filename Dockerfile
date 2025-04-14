# Gunakan image dasar Python yang ringan
FROM python:3.12-slim

# Install dependency Linux yang dibutuhkan OpenCV dan lainnya
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy semua file ke dalam container
COPY . /app

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask (default 5000)
EXPOSE 5000

# Jalankan app Flask
CMD ["python", "app.py"]
