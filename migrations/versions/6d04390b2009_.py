"""empty message

Revision ID: 6d04390b2009
Revises: 19a50d406b67
Create Date: 2021-05-26 22:55:57.347606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d04390b2009'
down_revision = '19a50d406b67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.alter_column('comment', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint('tag_title_key', 'tag', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('tag_title_key', 'tag', ['title'])
    op.alter_column('post', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('comment', 'name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_table('role_users')
    op.drop_table('role')
    # ### end Alembic commands ###
