
FROM python:3.6.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip

RUN pip  --no-cache-dir  install torch
# RUN pip  --no-cache-dir  install IPython
# RUN pip  --no-cache-dir  install matplotlib
# RUN pip  --no-cache-dir  install torchchaudio


RUN pip  --no-cache-dir  install requests
RUN pip  --no-cache-dir  install django
RUN pip  --no-cache-dir  install -r requirements.txt
# RUN pip -no-cache-dir install -r requirements.txt/

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
