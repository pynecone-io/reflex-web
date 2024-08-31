"""empty message.

Revision ID: 0e2da5026c00
Revises:
Create Date: 2024-05-22 17:31:15.245402

"""

from collections.abc import Sequence

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0e2da5026c00"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "customer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("phone", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("address", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "feedback",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("feedback", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("score", sa.Integer(), nullable=True),
        sa.Column("date_created", sa.DateTime(), nullable=False),
        sa.Column("page", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "waitlist",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("date_created", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###

    op.execute(
        """INSERT INTO Customer (name, email, phone, address) VALUES
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Elm Street, Springfield'),
('Jane Smith', 'jane.smith@example.com', '234-567-8901', '456 Oak Street, Springfield'),
('Alice Johnson', 'alice.johnson@example.com', '345-678-9012', '789 Pine Street, Springfield'),
('Bob Brown', 'bob.brown@example.com', '456-789-0123', '101 Maple Street, Springfield'),
('Charlie Davis', 'charlie.davis@example.com', '567-890-1234', '202 Birch Street, Springfield'),
('Dana White', 'dana.white@example.com', '678-901-2345', '303 Cedar Street, Springfield'),
('Eve Black', 'eve.black@example.com', '789-012-3456', '404 Ash Street, Springfield'),
('Frank Green', 'frank.green@example.com', '890-123-4567', '505 Willow Street, Springfield'),
('Grace Blue', 'grace.blue@example.com', '901-234-5678', '606 Elm Street, Springfield'),
('Hank Brown', 'hank.brown@example.com', '012-345-6789', '707 Oak Street, Springfield');
""",
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("waitlist")
    op.drop_table("feedback")
    op.drop_table("customer")
    # ### end Alembic commands ###
