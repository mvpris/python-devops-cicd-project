from click.testing import CliRunner
from pytest_mock import MockerFixture

from simple_http_checker.cli import main


def test_main_no_url() -> None:
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.exit_code == 0
    assert "Usage: check-urls" in result.output


def test_main_single_url_success(mocker: MockerFixture) -> None:
    url = "https://www.example.com"
    mock_check_urls = mocker.patch("simple_http_checker.cli.check_urls")
    mock_check_urls.return_value = {url: "200 OK"}

    runner = CliRunner()
    result = runner.invoke(main, [url])

    # For line below: click collects pos-args into a tuple (url,), not a list [url]
    mock_check_urls.assert_called_once_with((url,), timeout=5)
    assert result.exit_code == 0

    assert "--- RESULTS ---" in result.output
    assert url in result.output
    assert "-> 200 OK" in result.output


def test_main_custom_timeout(mocker: MockerFixture) -> None:
    url = "https://www.timeout.com"
    mock_check_urls = mocker.patch("simple_http_checker.cli.check_urls")
    mock_check_urls.return_value = {url: "TIMEOUT"}

    runner = CliRunner()
    result = runner.invoke(main, [url, "--timeout", "10"])

    mock_check_urls.assert_called_once_with((url,), timeout=10)
    assert result.exit_code == 0

    assert "--- RESULTS ---" in result.output
    assert url in result.output
    assert "-> TIMEOUT" in result.output


def test_main_multiple_urls(mocker: MockerFixture) -> None:
    urls = (
        "https://www.example1.com",
        "https://www.example2.com",
        "https://www.clienterror.com",
        "https://www.servererror.com",
    )
    mock_check_urls = mocker.patch("simple_http_checker.cli.check_urls")
    mock_check_urls.return_value = {
        urls[0]: "200 OK",
        urls[1]: "200 OK",
        urls[2]: "404 Client Error",
        urls[3]: "504 Server Error",
    }

    runner = CliRunner()
    result = runner.invoke(main, urls)

    mock_check_urls.assert_called_once_with(urls, timeout=5)
    assert result.exit_code == 0

    assert "--- RESULTS ---" in result.output
    assert urls[0] in result.output
    assert urls[1] in result.output
    assert urls[2] in result.output
    assert urls[3] in result.output
    assert "-> 200 OK" in result.output
    assert "-> 404 Client Error" in result.output
    assert "-> 504 Server Error" in result.output
