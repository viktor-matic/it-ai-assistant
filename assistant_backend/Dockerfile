# We are setting global argument APP_NAME which applies to all stages.
# Keep in mind that ENVs and ARGs are normally scoped at a stage level.
ARG APP_NAME="assistant_backend"

FROM python:3.11-buster as builder

RUN pip install poetry==1.7.1

ARG APP_NAME

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Create direcotries and copy project toml files
RUN mkdir -p /app/${APP_NAME} /app/assistant_commons
COPY ${APP_NAME}/pyproject.toml /app/${APP_NAME}
COPY ${APP_NAME}/poetry.lock /app/${APP_NAME}
# Copy commons library for the installation process via pip install -e method
COPY assistant_commons /app/assistant_commons/

WORKDIR /app/${APP_NAME}
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY ${APP_NAME}/${APP_NAME} /app/${APP_NAME}/${APP_NAME}

#  In following runtime stage we create a slim image.
#  To run code we only need to copy virtual environment and 
# the application from the previous stage to the new slim image. 
FROM python:3.11-slim-buster as runtime

ARG APP_NAME

ENV VIRTUAL_ENV=/app/${APP_NAME}/.venv \
    PATH="/app/${APP_NAME}/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
# Besides virtual environment we also need the application and shared commons library
COPY --from=builder /app/${APP_NAME}/${APP_NAME} /app/${APP_NAME}/${APP_NAME}/
COPY --from=builder /app/assistant_commons /app/assistant_commons/

EXPOSE 80

WORKDIR /app/${APP_NAME}/${APP_NAME}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]