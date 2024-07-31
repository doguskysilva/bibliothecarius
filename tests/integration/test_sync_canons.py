from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius.main import cli
from bibliothecarius.repository import CanonRepository

load_dotenv()


def test_sync_canons(runner: CliRunner, bibliothecarius_context):
    canon_repository = CanonRepository(bibliothecarius_context.db_session)

    assert len(canon_repository.get_all()) == 0

    with runner.isolated_filesystem():
        with open("canons.csv", "w") as file:
            file.write(
                "id,name,tradition,total_books\n1001,protestant,ocidental,42"
            )

        result = runner.invoke(
            cli, ["sync-canons", "canons.csv"], obj=bibliothecarius_context
        )
        assert result.exit_code == 0
        assert "Start sync canons" in result.output

        assert len(canon_repository.get_all()) == 1
