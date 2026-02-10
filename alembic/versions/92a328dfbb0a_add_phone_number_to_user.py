"""add phone number to user

Revision ID: 92a328dfbb0a
Revises: c7be2e98467d
Create Date: 2026-02-09 18:17:21.668457
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '92a328dfbb0a'
down_revision: Union[str, Sequence[str], None] = 'c7be2e98467d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ✅ ONLY add required columns to users table
    op.add_column('users', sa.Column('firstname', sa.String(), nullable=True))
    op.add_column('users', sa.Column('lastname', sa.String(), nullable=True))
    op.add_column('users', sa.Column('phone_number_country_code', sa.String(), nullable=True))
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    """
    Downgrade schema.

    Intentionally left empty to avoid accidental data loss.
    """
    pass
