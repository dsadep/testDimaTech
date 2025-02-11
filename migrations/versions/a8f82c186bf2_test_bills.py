"""test bills

Revision ID: a8f82c186bf2
Revises: 819a4b6da884
Create Date: 2025-02-11 16:46:31.438804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8f82c186bf2'
down_revision: Union[str, None] = '819a4b6da884'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO bills (balance, user_id) VALUES 
        (0.0, 1),
        (0.0, 2);
        """
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
