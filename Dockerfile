FROM python:3.10.0

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get update -y && apt-get install -y wget
RUN wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt update -y
RUN apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
RUN apt install -y google-chrome-stable


COPY . .

ENV PYTHONPATH=/app


# Install cron
RUN apt-get update && apt-get -y install cron

# Add cron job
RUN echo '0 */2 * * * python /app/logic/FM_bot.py' > /etc/cron.d/my-cron
RUN chmod 0644 /etc/cron.d/my-cron
RUN crontab /etc/cron.d/my-cron
RUN touch /var/log/cron.log

# Start cron and the Python script
CMD cron && tail -f /var/log/cron.log && python logic/FM_bot.py
