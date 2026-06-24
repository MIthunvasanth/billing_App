"""add user_id, content_hash, rls, and job metrics columns

Revision ID: b9c4f2a1e835
Revises: 0de1443cd0f2
Create Date: 2026-06-24 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b9c4f2a1e835'
down_revision: Union[str, Sequence[str], None] = '0de1443cd0f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # --- new columns ---
    op.add_column('jobs', sa.Column(
        'user_id',
        postgresql.UUID(as_uuid=False),
        nullable=False,
    ))
    op.add_column('jobs', sa.Column(
        'content_hash',
        sa.String(64),
        nullable=True,
    ))
    op.add_column('jobs', sa.Column(
        'token_usage',
        postgresql.JSONB(astext_type=sa.Text()),
        nullable=True,
    ))
    op.add_column('jobs', sa.Column(
        'cost_usd',
        sa.Numeric(10, 6),
        nullable=True,
    ))
    op.add_column('jobs', sa.Column(
        'processing_duration_seconds',
        sa.Numeric(10, 3),
        nullable=True,
    ))

    # --- indexes ---
    op.create_index('idx_jobs_user_id', 'jobs', ['user_id'], unique=False)
    op.create_index(
        'idx_jobs_user_content_hash',
        'jobs',
        ['user_id', 'content_hash'],
        unique=False,
        postgresql_where="status = 'completed'",
    )

    # --- billing_app role ---
    op.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'billing_app') THEN
                CREATE ROLE billing_app WITH LOGIN PASSWORD 'billing_app';
            END IF;
        END
        $$;
    """)
    op.execute("""
        DO $$
        BEGIN
            EXECUTE format('GRANT CONNECT ON DATABASE %I TO billing_app', current_database());
        END
        $$;
    """)
    op.execute("GRANT USAGE ON SCHEMA public TO billing_app;")
    op.execute("GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO billing_app;")
    op.execute("GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO billing_app;")

    # --- enable RLS on jobs ---
    # FORCE ROW LEVEL SECURITY intentionally omitted: billing (owner) must bypass RLS
    # so Alembic migrations run without needing app.current_user_id set.
    # billing_app (non-owner) is still fully subject to RLS without FORCE.
    op.execute("ALTER TABLE jobs ENABLE ROW LEVEL SECURITY;")

    # --- RLS policies ---
    # billing_app is subject to these; billing (owner) bypasses as table owner
    op.execute("""
        CREATE POLICY jobs_select_policy ON jobs
            FOR SELECT
            USING (user_id = current_setting('app.current_user_id', true)::uuid);
    """)
    op.execute("""
        CREATE POLICY jobs_insert_policy ON jobs
            FOR INSERT
            WITH CHECK (user_id = current_setting('app.current_user_id', true)::uuid);
    """)
    op.execute("""
        CREATE POLICY jobs_update_policy ON jobs
            FOR UPDATE
            USING (user_id = current_setting('app.current_user_id', true)::uuid);
    """)
    op.execute("""
        CREATE POLICY jobs_delete_policy ON jobs
            FOR DELETE
            USING (user_id = current_setting('app.current_user_id', true)::uuid);
    """)


def downgrade() -> None:
    # --- drop policies first ---
    op.execute("DROP POLICY IF EXISTS jobs_delete_policy ON jobs;")
    op.execute("DROP POLICY IF EXISTS jobs_update_policy ON jobs;")
    op.execute("DROP POLICY IF EXISTS jobs_insert_policy ON jobs;")
    op.execute("DROP POLICY IF EXISTS jobs_select_policy ON jobs;")

    # --- disable RLS ---
    op.execute("ALTER TABLE jobs DISABLE ROW LEVEL SECURITY;")

    # --- revoke grants then drop role ---
    op.execute("REVOKE USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public FROM billing_app;")
    op.execute("REVOKE SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public FROM billing_app;")
    op.execute("REVOKE USAGE ON SCHEMA public FROM billing_app;")
    op.execute("""
        DO $$
        BEGIN
            EXECUTE format('REVOKE CONNECT ON DATABASE %I FROM billing_app', current_database());
        END
        $$;
    """)
    op.execute("""
        DO $$
        BEGIN
            IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'billing_app') THEN
                DROP ROLE billing_app;
            END IF;
        END
        $$;
    """)

    # --- drop indexes ---
    op.drop_index(
        'idx_jobs_user_content_hash',
        table_name='jobs',
        postgresql_where="status = 'completed'",
    )
    op.drop_index('idx_jobs_user_id', table_name='jobs')

    # --- drop columns (reverse order) ---
    op.drop_column('jobs', 'processing_duration_seconds')
    op.drop_column('jobs', 'cost_usd')
    op.drop_column('jobs', 'token_usage')
    op.drop_column('jobs', 'content_hash')
    op.drop_column('jobs', 'user_id')
