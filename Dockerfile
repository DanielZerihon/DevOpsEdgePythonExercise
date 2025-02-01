FROM python:3.9

WORKDIR /app

COPY requirements.txt wheel/dist/details_library-0.5.1-py3-none-any.whl .

RUN apt-get update && apt-get install -y vim
RUN pip install -r requirements.txt
RUN pip install /app/details_library-0.5.1-py3-none-any.whl

COPY . .

EXPOSE 5000

CMD ["python", "bot.py"]
