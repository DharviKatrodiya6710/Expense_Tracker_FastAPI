"""add user id

Revision ID: 39c0c5a5031f
Revises: 23afc22fa701
Create Date: 2026-02-06 17:25:20.158834
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "39c0c5a5031f"
down_revision: Union[str, Sequence[str], None] = "23afc22fa701"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # id already exists as String (UUID) in Base
    # no schema change needed
    pass


def downgrade() -> None:
    pass
