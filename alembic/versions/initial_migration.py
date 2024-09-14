from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import enum


revision = '1234567890ab'
down_revision = None
branch_labels = None
depends_on = None

class TaskStatus(enum.Enum):
    INIT = "init"
    COMPLETE = "complete"


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('username', sa.String(50), unique=True, index=True),
        sa.Column('email', sa.String(100), unique=True),
    )
    op.create_table('tasks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('status', sa.Enum(TaskStatus), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('created_by', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_tasks_id'), 'tasks', ['id'], unique=False)


def downgrade() -> None:
    op.drop_table('users')
    op.drop_index(op.f('ix_tasks_id'), table_name='tasks')
    op.drop_table('tasks')
