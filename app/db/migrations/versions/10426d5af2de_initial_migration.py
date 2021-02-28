"""Initial migration

Revision ID: 10426d5af2de
Revises: 
Create Date: 2021-02-28 14:29:17.355638

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '10426d5af2de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('ref_id', sa.Integer(), nullable=False),
    sa.Column('ref_type', sa.String(length=255), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_created_at'), 'users', ['created_at'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_ref_id'), 'users', ['ref_id'], unique=False)
    op.create_index(op.f('ix_users_ref_type'), 'users', ['ref_type'], unique=False)
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('name_bn', sa.Unicode(length=255), nullable=False),
    sa.Column('details', sa.UnicodeText(), nullable=True),
    sa.Column('key', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('layer', sa.Integer(), nullable=False),
    sa.Column('root_account', sa.String(length=255), nullable=False),
    sa.Column('account_type', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('visible', sa.Boolean(), nullable=True),
    sa.Column('editable', sa.Boolean(), nullable=True),
    sa.Column('deletable', sa.Boolean(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['accounts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'key')
    )
    op.create_index(op.f('ix_accounts_created_at'), 'accounts', ['created_at'], unique=False)
    op.create_index(op.f('ix_accounts_id'), 'accounts', ['id'], unique=False)
    op.create_index(op.f('ix_accounts_key'), 'accounts', ['key'], unique=False)
    op.create_table('entries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.NUMERIC(precision=2, scale=2), nullable=False),
    sa.Column('source_type', mysql.ENUM('INCOME', 'EXPENSE', 'DUE', 'DEPOSIT', 'POS', 'INVENTORY', 'EMI'), nullable=False),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('emi_month', sa.Integer(), nullable=True),
    sa.Column('note', sa.UnicodeText(), nullable=True),
    sa.Column('attachments', sa.JSON(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('created_from', sa.JSON(), nullable=False),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('payment_method', sa.String(length=255), nullable=True),
    sa.Column('interest', sa.NUMERIC(precision=2, scale=2), nullable=True),
    sa.Column('bank_transaction_charge', sa.NUMERIC(precision=2, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entries_created_at'), 'entries', ['created_at'], unique=False)
    op.create_index(op.f('ix_entries_customer_id'), 'entries', ['customer_id'], unique=False)
    op.create_index(op.f('ix_entries_emi_month'), 'entries', ['emi_month'], unique=False)
    op.create_index(op.f('ix_entries_id'), 'entries', ['id'], unique=False)
    op.create_index(op.f('ix_entries_source_id'), 'entries', ['source_id'], unique=False)
    op.create_index(op.f('ix_entries_source_type'), 'entries', ['source_type'], unique=False)
    op.create_index(op.f('ix_entries_user_id'), 'entries', ['user_id'], unique=False)
    op.create_table('daily_account_stats',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.Column('opening_balance', sa.Numeric(precision=2, scale=2), nullable=True),
    sa.Column('closing_balance', sa.Numeric(precision=2, scale=2), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_daily_account_stats_account_id'), 'daily_account_stats', ['account_id'], unique=False)
    op.create_index(op.f('ix_daily_account_stats_created_at'), 'daily_account_stats', ['created_at'], unique=False)
    op.create_index(op.f('ix_daily_account_stats_date'), 'daily_account_stats', ['date'], unique=False)
    op.create_index(op.f('ix_daily_account_stats_id'), 'daily_account_stats', ['id'], unique=False)
    op.create_table('journals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.Column('sub_account_id', sa.Integer(), nullable=False),
    sa.Column('debit', sa.Numeric(precision=2, scale=2), nullable=False),
    sa.Column('credit', sa.Numeric(precision=2, scale=2), nullable=False),
    sa.Column('details', sa.UnicodeText(), nullable=True),
    sa.Column('entry_at', sa.DATETIME(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('source_type', sa.String(length=255), nullable=False),
    sa.Column('reference', sa.String(length=255), nullable=True),
    sa.Column('receiver_type', sa.String(length=255), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], onupdate='cascade', ondelete='cascade'),
    sa.ForeignKeyConstraint(['sub_account_id'], ['accounts.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_journals_account_id'), 'journals', ['account_id'], unique=False)
    op.create_index(op.f('ix_journals_created_at'), 'journals', ['created_at'], unique=False)
    op.create_index(op.f('ix_journals_entry_at'), 'journals', ['entry_at'], unique=False)
    op.create_index(op.f('ix_journals_id'), 'journals', ['id'], unique=False)
    op.create_index(op.f('ix_journals_receiver_id'), 'journals', ['receiver_id'], unique=False)
    op.create_index(op.f('ix_journals_receiver_type'), 'journals', ['receiver_type'], unique=False)
    op.create_index(op.f('ix_journals_source_id'), 'journals', ['source_id'], unique=False)
    op.create_index(op.f('ix_journals_source_type'), 'journals', ['source_type'], unique=False)
    op.create_index(op.f('ix_journals_sub_account_id'), 'journals', ['sub_account_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_journals_sub_account_id'), table_name='journals')
    op.drop_index(op.f('ix_journals_source_type'), table_name='journals')
    op.drop_index(op.f('ix_journals_source_id'), table_name='journals')
    op.drop_index(op.f('ix_journals_receiver_type'), table_name='journals')
    op.drop_index(op.f('ix_journals_receiver_id'), table_name='journals')
    op.drop_index(op.f('ix_journals_id'), table_name='journals')
    op.drop_index(op.f('ix_journals_entry_at'), table_name='journals')
    op.drop_index(op.f('ix_journals_created_at'), table_name='journals')
    op.drop_index(op.f('ix_journals_account_id'), table_name='journals')
    op.drop_table('journals')
    op.drop_index(op.f('ix_daily_account_stats_id'), table_name='daily_account_stats')
    op.drop_index(op.f('ix_daily_account_stats_date'), table_name='daily_account_stats')
    op.drop_index(op.f('ix_daily_account_stats_created_at'), table_name='daily_account_stats')
    op.drop_index(op.f('ix_daily_account_stats_account_id'), table_name='daily_account_stats')
    op.drop_table('daily_account_stats')
    op.drop_index(op.f('ix_entries_user_id'), table_name='entries')
    op.drop_index(op.f('ix_entries_source_type'), table_name='entries')
    op.drop_index(op.f('ix_entries_source_id'), table_name='entries')
    op.drop_index(op.f('ix_entries_id'), table_name='entries')
    op.drop_index(op.f('ix_entries_emi_month'), table_name='entries')
    op.drop_index(op.f('ix_entries_customer_id'), table_name='entries')
    op.drop_index(op.f('ix_entries_created_at'), table_name='entries')
    op.drop_table('entries')
    op.drop_index(op.f('ix_accounts_key'), table_name='accounts')
    op.drop_index(op.f('ix_accounts_id'), table_name='accounts')
    op.drop_index(op.f('ix_accounts_created_at'), table_name='accounts')
    op.drop_table('accounts')
    op.drop_index(op.f('ix_users_ref_type'), table_name='users')
    op.drop_index(op.f('ix_users_ref_id'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_created_at'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###