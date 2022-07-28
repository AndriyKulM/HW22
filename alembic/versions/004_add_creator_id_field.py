"""004_add_creator_id_field

Revision ID: 004_add_creator_id_field
Revises: 003_make_event_desc_nullable
Create Date: 2022-07-21 20:51:15.945246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004_add_creator_id_field'
down_revision = '003_make_event_desc_nullable'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("event", sa.Column("creator_id", sa.Integer, sa.ForeignKey('user.id'), nullable=False))


def downgrade() -> None:
    op.drop_column("event", "creator_id")
