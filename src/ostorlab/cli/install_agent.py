"""Module responsible for installing an agent : Pulling the image from the ostorlab store."""
from typing import Dict, Optional, Generator
import click
import docker
import docker.errors

from ostorlab.cli import console as cli_console
from ostorlab.apis.runners import runner as base_runner
from ostorlab.apis.runners import public_runner, authenticated_runner
from ostorlab.apis import agent_details as agent_details_api
from ostorlab import configuration_manager
from ostorlab.cli.agent.install import install_progress


console = cli_console.Console()


def _image_name_from_key(agent_key: str) -> str:
    """Generate docker image name from an agent key.

    Args:
        agent_key: agent key in the form agent/organization/name.

    Returns:
        image_name: image name in the form : agent_organization_name.
    """
    return agent_key.replace('/', '_').lower()


def _parse_repository_tag(repo_name: str, tag: str = None) -> tuple:
    """Get repo name and tag"""
    parts = repo_name.rsplit('@', 1)
    if len(parts) == 2:
        return tuple(parts)
    parts = repo_name.rsplit(':', 1)
    if len(parts) == 2 and '/' not in parts[1]:
        return tuple(parts)
    return repo_name, tag


def _pull_logs(docker_client: docker.DockerClient,
               repository: str,
               tag: Optional[str] = None) -> Generator[Dict, None, None]:
    """Generate logs of the docker pull method."""
    repository, tag = _parse_repository_tag(repository, tag)
    pull_log = docker_client.api.pull(repository, tag=tag, stream=True, decode=True)
    for log in pull_log:
        yield log


def _get_image(docker_client: docker.DockerClient,
               repository: str,
               tag: str = None) -> docker.models.images.Image:
    """Gets a docker image."""
    repository, tag = _parse_repository_tag(repository, tag)
    name = f'{repository}:{tag}'

    return docker_client.images.get(name)


def _is_image_present(docker_client: docker.DockerClient, image_name: str) -> bool:
    """Check if a docker image exists."""
    try:
        docker_client.images.get(image_name)
        return True
    except docker.errors.ImageNotFound:
        return False


def get_agent_details(agent_key: str) -> Dict:
    """Sends an API request with the agent key, and retrieve the agent information.

    Args:
        agent_key: the agent key in the form : agent/org/name

    Returns:
        dictionary of the agent information like : name, dockerLocation..

    Raises:
        click Exit exception with satus code 2 when API response is invalid.
    """
    config_manager = configuration_manager.ConfigurationManager()

    if config_manager.is_authenticated:
        runner = authenticated_runner.AuthenticatedAPIRunner()
    else:
        runner = public_runner.PublicAPIRunner()

    try:
        response = runner.execute(agent_details_api.AgentDetailsAPIRequest(agent_key))
    except base_runner.ResponseError as e:
        console.error('Requested resource not found.')
        raise click.exceptions.Exit(2) from e


    if 'errors' in response:
        error_message = f"""\b The provided agent key : {agent_key} does not correspond to any agent.
        Please make sure you have the correct agent key.
        """
        console.error(error_message)
        raise click.exceptions.Exit(2)
    else:
        agent_details = response['data']['agent']
        return agent_details



def install(agent_key: str, version: str = '') -> None:
    """Install an agent : Fetch the docker file location of the agent corresponding to the agent_key,
    and pull the image from the registry.

    Args:
        agent_key: key of the agent in agent/org/agentName format.
        version: version of the docker image.

    Returns:
        None

    Raises:
        click Exit exception with satus code 2 when the docker image does not exist.
    """

    agent_details = get_agent_details(agent_key)

    agent_docker_location = agent_details['dockerLocation']
    image_name = _image_name_from_key(agent_details['key'])

    try:
        docker_client = docker.from_env()

        if _is_image_present(docker_client, image_name):
            console.info(f'{agent_key} already exist.')
        else:
            console.info('Pulling the image from the ostorlab store.')

            pull_logs_generator = _pull_logs(docker_client, agent_docker_location)

            progress_foo = install_progress.AgentInstallProgress()
            progress_foo.display(pull_logs_generator)

            agent_image = _get_image(docker_client=docker_client, repository=agent_docker_location, tag=version)
            agent_image.tag(repository=image_name, tag=version)

    except docker.errors.ImageNotFound as e:
        error_message = f'Image of the provided agent : {agent_key} was not found.'
        console.error(error_message)
        raise click.exceptions.Exit(2) from e
