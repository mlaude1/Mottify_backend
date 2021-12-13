"""CreateTracksTable Migration."""

from masoniteorm.migrations import Migration


class CreateTracksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("tracks") as table:
            table.increments("id")
            table.string("title").default("Unknown Title")
            table.string("artist")
            table.string("album")
            table.string("albumCover")
            table.string("genre")
            table.boolean("favorite")
            table.string("mp3Url")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("tracks")
