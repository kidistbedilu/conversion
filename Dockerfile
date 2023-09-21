FROM python:3.11

WORKDIR /app

RUN git clone https://github.com/kidistbedilu/conversion.git .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
