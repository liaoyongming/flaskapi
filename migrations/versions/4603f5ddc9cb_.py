"""empty message

Revision ID: 4603f5ddc9cb
Revises: 
Create Date: 2019-01-15 12:24:13.352143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4603f5ddc9cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('alerttime', sa.DateTime(), nullable=True),
    sa.Column('tag', sa.Text(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('task_type', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    # ### end Alembic commands ###
