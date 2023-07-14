import dataclasses
from typing import List


@dataclasses.dataclass
class SubjectBusConfigs:
    """Represents the configuration for a subject and its corresponding queue."""
    subject: str
    queue: str


@dataclasses.dataclass
class ScannerConfig:
    """Represents the configuration for a scanner."""
    bus_url: str
    bus_cluster_id: str
    bus_client_name: str
    subject_bus_configs: List[SubjectBusConfigs]

    @classmethod
    def from_json(cls, config):
        """Creates a ScannerConfig instance from a JSON configuration.

        Args:
            config: The JSON configuration.

        Returns:
            ScannerConfig: An instance of ScannerConfig.
        """
        subject_configs = config.get("data", {}).get("scanners", {}).get("scanners", [])[0].get("config", {})
        bus_configs = []
        for subject_config in subject_configs.get("subjectBusConfigs", {}).get("subjectBusConfigs", []):
            bus_configs.append(
                SubjectBusConfigs(subject=subject_config.get("subject"), queue=subject_config.get("queue")))

        return cls(
            bus_url=config.get("data", {}).get("scanners", {}).get("scanners", [])[0].get("config", {}).get("busUrl"),
            bus_cluster_id=config.get("data", {}).get("scanners", {}).get("scanners", [])[0].get("config", {}).get(
                "busClusterId"),
            bus_client_name=config.get("data", {}).get("scanners", {}).get("scanners", [])[0].get("config", {}).get(
                "busClientName"),
            subject_bus_configs=bus_configs
        )
