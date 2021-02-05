FROM ubuntu:trusty
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libgconf2-4 libnss3-1d libxss1
RUN apt-get install -y fonts-liberation libappindicator1 xdg-utils
RUN apt-get install -y software-properties-common
RUN apt-get install -y curl unzip wget
RUN apt-get install -y xvfb

# install chromedriver and chrome

RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \

    wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip

RUN unzip chromedriver_linux64.zip -d /usr/bin
RUN chmod +x /usr/bin/chromedriver


RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg --install google-chrome-stable_current_amd64.deb || apt-get -f install -y
RUN apt-get install -y -f


RUN pip3 install selenium
RUN pip3 install pyvirtualdisplay
RUN pip3 install behave
RUN pip3 install --upgrade --ignore-installed urllib3
RUN pip3 install awscli --upgrade --user


ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME
COPY . $APP_HOME/
RUN mkdir -p /usr/src/app/Test_Result/

CMD tail -f /dev/null

CMD python3 Scenario-1.py
#CMD sh aws_s3_push.sh

