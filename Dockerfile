FROM python:3.6.6-alpine3.6

COPY counttothree.py counttothree.py
COPY  requirements/ requirements/

RUN pip install --upgrade pip && pip install -r requirements/prod.txt


CMD python counttothree.py
