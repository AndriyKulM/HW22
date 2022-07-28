"""005_add_invitation_status_field

Revision ID: 005_add_invitation_status_field
Revises: 004_add_creator_id_field
Create Date: 2022-07-24 21:01:40.986249

"""
from tkinter import CASCADE
from sqlalchemy.dialects import postgresql
from alembic import op
import sqlalchemy as sa

from core.models.user_event import InvitationStatus


# revision identifiers, used by Alembic.
revision = '005_add_invitation_status_field'
down_revision = '004_add_creator_id_field'
branch_labels = None
depends_on = None


def upgrade() -> None:
    inv_status = postgresql.ENUM(InvitationStatus, name="invitation_status")
    inv_status.create(op.get_bind(), checkfirst=True)
    op.add_column('user_event', sa.Column('invitation_status',  inv_status))


def downgrade() -> None:
    inv_status = postgresql.ENUM(InvitationStatus, name="invitation_status")
    inv_status.drop(op.get_bind())