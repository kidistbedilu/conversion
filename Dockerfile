FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt install -y git 

RUN git clone https://github.com/kidistbedilu/conversion.git .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

# RUN
# docker build . -t app-name
# docker run -p 8080:8080 app-name
