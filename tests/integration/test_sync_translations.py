from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius import entities
from bibliothecarius.main import cli
from bibliothecarius.repository import CanonRepository, TranslationRepository

load_dotenv()


def test_sync_translations(runner: CliRunner, bibliothecarius_context):
    translation_repository = TranslationRepository(bibliothecarius_context.db_session)
    canon_repository = CanonRepository(bibliothecarius_context.db_session)

    canon_repository.add_many(
        [
            entities.Canon(
                canon_id=2002, name="any-name", tradition="any-tradition", total_books=1
            )
        ]
    )

    assert len(translation_repository.all()) == 0

    with runner.isolated_filesystem():
        with open("translations.csv", "w") as file:
            file.write(
                "id,name,description,language,country,total_verses,canon_id\n1,any-name,descrição,pt,br,31105,2002"
            )

        result = runner.invoke(
            cli, ["sync-translations", "translations.csv"], obj=bibliothecarius_context
        )
        assert result.exit_code == 0
        assert "Start sync translations" in result.output

        assert len(translation_repository.all()) == 1
