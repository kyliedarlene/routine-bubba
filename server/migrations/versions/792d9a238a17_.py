"""empty message

Revision ID: 792d9a238a17
Revises: ff68b7f7971f
Create Date: 2024-02-15 23:44:03.145254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '792d9a238a17'
down_revision = 'ff68b7f7971f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('routines', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_routines_dog_id_dogs'), 'dogs', ['dog_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_routines_activity_id_activities'), 'activities', ['activity_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('routines', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_routines_activity_id_activities'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_routines_dog_id_dogs'), type_='foreignkey')

    # ### end Alembic commands ###
