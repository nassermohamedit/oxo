"""This module triggers a scan using the android_store asset."""

import logging
from typing import Tuple, Optional

import click

from ostorlab.cli.scan.run import run
from ostorlab.cli import console as cli_console
from ostorlab.assets import android_store as android_store_asset
from ostorlab import exceptions
from ostorlab.runtimes.local.models import models

console = cli_console.Console()
logger = logging.getLogger(__name__)


@run.run.command(name="android-store")
@click.option("--package-name", multiple=True, required=False)
@click.pass_context
def android_store(
    ctx: click.core.Context, package_name: Optional[Tuple[str]] = ()
) -> None:
    """Run scan for a package_name."""
    runtime = ctx.obj["runtime"]
    assets = []
    if package_name != ():
        for package in package_name:
            assets.append(android_store_asset.AndroidStore(package_name=package))
    else:
        console.error("Command missing a package name.")
        raise click.exceptions.Exit(2)

    logger.debug("scanning assets %s", [str(asset) for asset in assets])
    try:
        created_scan = runtime.scan(
            title=ctx.obj["title"],
            agent_group_definition=ctx.obj["agent_group_definition"],
            assets=assets,
        )

        with models.Database() as session:
            agent_group_db = models.AgentGroup.create_from_agent_group_def(
                ctx.obj["agent_group_definition"]
            )
            created_scan.agent_group_id = agent_group_db.id
            session.add(created_scan)
            session.commit()

            if assets is not None:
                models.Asset.create_from_assets_def(created_scan, assets)
    except exceptions.OstorlabError as e:
        console.error(f"An error was encountered while running the scan: {e}")
