"""add auth tables and default privileges

Revision ID: c3d5e7f9a1b2
Revises: b9c4f2a1e835
Create Date: 2026-06-24 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c3d5e7f9a1b2'
down_revision: Union[str, Sequence[str], None] = 'b9c4f2a1e835'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- Better Auth tables (camelCase columns, quoted identifiers) ---
    op.execute("""
        CREATE TABLE "user" (
            id              TEXT        PRIMARY KEY,
            name            TEXT        NOT NULL,
            email           TEXT        NOT NULL UNIQUE,
            "emailVerified" BOOLEAN     NOT NULL DEFAULT FALSE,
            image           TEXT,
            "createdAt"     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            "updatedAt"     TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
    """)

    op.execute("""
        CREATE TABLE account (
            id           TEXT        PRIMARY KEY,
            "accountId"  TEXT        NOT NULL,
            "providerId" TEXT        NOT NULL DEFAULT 'credential',
            "userId"     TEXT        NOT NULL REFERENCES "user"(id) ON DELETE CASCADE,
            password     TEXT,
            "createdAt"  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            "updatedAt"  TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
    """)

    op.execute("""
        CREATE TABLE session (
            id           TEXT        PRIMARY KEY,
            token        TEXT        NOT NULL UNIQUE,
            "expiresAt"  TIMESTAMPTZ NOT NULL,
            "userId"     TEXT        NOT NULL REFERENCES "user"(id) ON DELETE CASCADE,
            "ipAddress"  TEXT,
            "userAgent"  TEXT,
            "createdAt"  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            "updatedAt"  TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
    """)

    # --- grant billing_app access to the new tables ---
    op.execute('GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE "user", account, session TO billing_app;')

    # --- default privileges so billing_app automatically gets access to future tables ---
    op.execute("""
        ALTER DEFAULT PRIVILEGES IN SCHEMA public
            GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO billing_app;
    """)
    op.execute("""
        ALTER DEFAULT PRIVILEGES IN SCHEMA public
            GRANT USAGE, SELECT ON SEQUENCES TO billing_app;
    """)


def downgrade() -> None:
    # --- revoke default privileges first ---
    op.execute("""
        ALTER DEFAULT PRIVILEGES IN SCHEMA public
            REVOKE USAGE, SELECT ON SEQUENCES FROM billing_app;
    """)
    op.execute("""
        ALTER DEFAULT PRIVILEGES IN SCHEMA public
            REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM billing_app;
    """)

    # --- drop tables (FK-constrained tables before "user") ---
    op.execute("DROP TABLE IF EXISTS session;")
    op.execute("DROP TABLE IF EXISTS account;")
    op.execute('DROP TABLE IF EXISTS "user";')
