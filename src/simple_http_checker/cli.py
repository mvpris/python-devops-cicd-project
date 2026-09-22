import logging
from collections.abc import Collection

import click

from .checker import check_urls

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


@click.command()
@click.argument("urls", nargs=-1)
@click.option("--timeout", "-t", default=5, help="Timeout in seconds for each request.")
@click.option("--verbose", "-v", is_flag=True, help="Enable debug logging.")
def main(urls: Collection[str], timeout: int, verbose: bool):
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled.")

    logger.debug(f"Received urls: {urls}")
    logger.debug(f"Received timeout: {timeout}")
    logger.debug(f"Received verbose: {verbose}")

    if not urls:
        logger.warning("No URLs provided to check.")
        click.echo("Usage: check-urls <URL1> <URL2> ...")
        return

    logger.info(f"Starting check for {len(urls)} URLs.")

    results = check_urls(urls, timeout=timeout)

    click.echo("\n--- RESULTS ---")
    for url, status in results.items():
        if "OK" in status:
            fg_color = "green"
        else:
            fg_color = "red"
        click.secho(f"{url:<40} -> {status}", fg=fg_color)


# Example usage (in-terminal command)
# pip install -e .
# check-urls -vt10 https://www.google.com https://www.github.com https://www.aajdfhhjsdbgsjbndfjok.com http://httpbin.org/status/404
