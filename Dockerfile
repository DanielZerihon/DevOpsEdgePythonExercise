FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY details_library-0.3.1-py3-none-any.whl /app/

RUN apt-get update && apt-get install -y vim
RUN pip install -r requirements.txt
RUN pip install /app/details_library-0.4.1-py3-none-any.whl

COPY . .

EXPOSE 5000

CMD ["python", "bot.py"]