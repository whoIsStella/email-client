# Email Client

An unfinished FastAPI backend prototype for storing encrypted message payloads and user public keys.

This repository is a small experiment, not a deployable secure-email service.

## What it does

- stores users with an email address, a client-supplied password hash, and a public key
- stores opaque encrypted subject/body payloads
- looks up recipients by email address
- exposes a simple inbox endpoint
- supports SQLite by default and PostgreSQL through `DATABASE_URL`

## What it does not do

- authenticate users
- hash passwords
- perform encryption or key exchange
- verify message senders
- send mail over SMTP or another transport
- provide production authorization, migrations, rate limiting, or abuse controls

Do not deploy this as a secure messaging service in its current state.

## Run locally

```bash
cd secure-mail-backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
uvicorn app.main:app --reload
```

The default configuration uses SQLite if `DATABASE_URL` is not set.

Example PostgreSQL configuration:

```text
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/securemail
```

## Endpoints

- `GET /health`
- `POST /users/`
- `POST /emails/`
- `GET /emails/{user_id}`

## Repository status

This is a cleanup of an old prototype. The immediate goal is to keep the code small, runnable, and explicit about what is and is not implemented.
