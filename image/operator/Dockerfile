FROM python:3.7
RUN pip install --no-cache-dir kopf pykube-ng pyyaml
ADD malls-operator.py /src/malls-operator.py
CMD kopf run /src/malls-operator.py --verbose
