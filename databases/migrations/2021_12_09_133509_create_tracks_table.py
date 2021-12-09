"""CreateTracksTable Migration."""

from masoniteorm.migrations import Migration


class CreateTracksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("tracks") as table:
            table.increments("id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("tracks")
