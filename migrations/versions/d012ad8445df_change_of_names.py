"""change of names

Revision ID: d012ad8445df
Revises: fd2f1f34973f
Create Date: 2021-12-10 14:08:57.744826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd012ad8445df'
down_revision = 'fd2f1f34973f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'detection_areas', 'user', ['user_id'], ['id'])
    op.add_column('in_com', sa.Column('complaint_status', sa.String(length=140), nullable=True))
    op.drop_column('in_com', 'registration_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('in_com', sa.Column('registration_status', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('in_com', 'complaint_status')
    op.drop_constraint(None, 'detection_areas', type_='foreignkey')
    # ### end Alembic commands ###
