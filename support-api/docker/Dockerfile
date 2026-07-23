FROM python:3.12-slim AS builder

WORKDIR /build

COPY pyproject.toml ./
COPY src/ ./src/

RUN python -m venv /opt/venv && /opt/venv/bin/pip install .


FROM python:3.12-slim AS runtime

ENV PATH="/opt/venv/bin:$PATH" PYTHONUNBUFFERED=1

RUN groupadd --system --gid 10001 app && useradd --system --uid 10001 --gid 10001 --create-home app

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY data/ /app/data/

# make /app writeable by the app user - since at runtime the application will create 'tickets.db' in the folder when init_db runs.
RUN chown -R app:app /app

USER app

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-", "support_api.api:create_app()" ]