from pytest_mock import MockerFixture

from bibliothecarius.controller import sync_books


def test_sync_books(mocker: MockerFixture):
    read_data = "id;name;abbreviation;testament;chapters\n1001;Genesis;gen;old;50"
    
    mock_open = mocker.mock_open(read_data=read_data)
    mocker.patch('builtins.open', mock_open)

    sync_books()

    mock_open.assert_called_once_with("resources/books.csv", "r")

