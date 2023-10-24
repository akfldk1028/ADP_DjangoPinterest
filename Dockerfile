FROM python:3.11.6

WORKDIR /home/

RUN git clone https://github.com/akfldk1028/ADP_DjangoPinterest.git

WORKDIR /home/pragmatic

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-s0ypvv7i_g2n6&sax1tgnv7egn_r=4!%j3xmynfv$=hj5b8(ws" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]