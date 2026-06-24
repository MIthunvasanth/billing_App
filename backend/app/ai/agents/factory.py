from agents import Agent, RunContextWrapper

from app.ai.config import ECHO_AGENT_CONFIG
from app.ai.context import RunContext
from app.ai.tools import echo_tool, get_document_info, read_page
from app.models.extraction import ExtractionOutput


class AgentFactory:
    """Builds `Agent[RunContext]` instances for pipeline stages.

    Add more `build_*_agent()` static methods here as you introduce new stages.
    Follow `build_echo_agent` for instructions from Jinja via `prompt_loader`
    on `RunContext`, model config from `app.ai.config`, and tools from `tools.py`.
    """

    @staticmethod
    def build_echo_agent() -> Agent[RunContext]:
        """Echo agent — full working example for the executor pattern."""

        async def instructions(
            wrapper: RunContextWrapper[RunContext], agent: Agent
        ) -> str:
            return await wrapper.context.prompt_loader.render(
                ECHO_AGENT_CONFIG.instructions_key, {}
            )

        return Agent[RunContext](
            name="echo_agent",
            instructions=instructions,
            model=ECHO_AGENT_CONFIG.model,
            model_settings=ECHO_AGENT_CONFIG.model_settings,
            tools=[echo_tool],
        )

    @staticmethod
    def build_extraction_agent() -> Agent[RunContext]:
        """Extraction agent — reads PDF pages and returns structured BillingRecord output."""

        async def instructions(
            wrapper: RunContextWrapper[RunContext], agent: Agent
        ) -> str:
            return await wrapper.context.prompt_loader.render(
                "extraction/system.j2", {}
            )

        return Agent[RunContext](
            name="extraction_agent",
            instructions=instructions,
            model="gpt-4o-mini",
            output_type=ExtractionOutput,
            tools=[read_page, get_document_info],
        )
