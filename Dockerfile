FROM python:3.11.6

WORKDIR /home/

RUN git clone https://github.com/akfldk1028/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-s0ypvv7i_g2n6&sax1tgnv7egn_r=4!%j3xmynfv$=hj5b8(ws" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]