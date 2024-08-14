FROM python:3.10

ARG wheel=bank-0.0.1-py3-none-any.whl

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY ./dist/$wheel /code/$wheel
RUN pip install --no-cache-dir --upgrade /code/$wheel

CMD ["uvicorn", "greet_api.core:app", "--host", "0.0.0.0", "--port", "8000"]
