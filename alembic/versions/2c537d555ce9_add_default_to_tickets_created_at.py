"""add default to tickets.created_at

Revision ID: 2c537d555ce9
Revises: 015030973902
Create Date: 2026-02-02 21:16:13.100043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c537d555ce9'
down_revision: Union[str, Sequence[str], None] = '015030973902'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
