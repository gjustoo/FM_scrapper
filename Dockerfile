FROM python:3.10.0

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get update -y && apt-get install -y wget

# chromedriver FOR AMD64
# RUN wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip
# RUN unzip chromedriver_linux64.zip

# chromedriver FOR ARM64
RUN wget https://github.com/electron/electron/releases/download/v18.2.1/chromedriver-v18.2.1-linux-arm64.zip
RUN unzip chromedriver-v18.2.1-linux-arm64.zip

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

RUN sh ./scripts/installChromium.sh

