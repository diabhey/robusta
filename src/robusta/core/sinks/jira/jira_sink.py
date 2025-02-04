from .jira_sink_params import JiraSinkConfigWrapper
from ..sink_base import SinkBase
from ...reporting.base import Finding
from ....integrations.jira.sender import JiraSender


class JiraSink(SinkBase):
    def __init__(self, sink_config: JiraSinkConfigWrapper, registry):
        super().__init__(sink_config.jira_sink, registry)

        self.url = sink_config.jira_sink.url
        self.sender = JiraSender(
            self.cluster_name,
            self.account_id,
            self.params
        )

    def write_finding(self, finding: Finding, platform_enabled: bool):
        self.sender.send_finding_to_jira(
            finding,  platform_enabled
        )
