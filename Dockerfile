FROM python:3

RUN mkdir /home/bot
RUN mkdir /home/bot/log

COPY wildegans-bot.py /home/bot/wildegans-bot.py
COPY crawler.py /home/bot/crawler.py
COPY requirements.txt /home/bot/requirements.txt

RUN cd /home/bot && pip3 install --no-cache-dir -r requirements.txt

CMD cd /home/bot \
  &&  python3 wildegans-bot.py
