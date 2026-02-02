"""add default to tickets.created_at

Revision ID: 015030973902
Revises: 22092ca1d285
Create Date: 2026-02-02 18:13:34.686976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '015030973902'
down_revision: Union[str, Sequence[str], None] = '22092ca1d285'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
