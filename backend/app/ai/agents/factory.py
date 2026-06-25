from agents import Agent, RunContextWrapper

from app.ai.config import ECHO_AGENT_CONFIG
from app.ai.context import RunContext
from app.ai.tools import echo_tool
from app.models.extraction import ExtractionOutput, PageClassification


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
            return wrapper.context.prompt_loader.render(
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
    def build_page_classifier_agent() -> Agent[RunContext]:
        """Classifier agent — identifies summary/ledger pages from page previews."""
        return Agent[RunContext](
            name="page_classifier",
            instructions=(
                "You are a medical billing document analyst. "
                "Given short previews of each page in a PDF, identify which pages are "
                "summary billing ledgers — pages that contain a table listing multiple "
                "billing records (treatment dates, CPT codes, charges, payments, balance). "
                "A summary page shows many rows in a compact table. "
                "Detail/itemized pages expand a single record with line-item breakdowns. "
                "Cover pages, signature pages, and authorization pages are not summary pages. "
                "Return has_summary=true and the list of summary page numbers if found."
            ),
            model="gpt-4.1-mini",
            output_type=PageClassification,
            tools=[],
        )

    @staticmethod
    def build_extraction_agent() -> Agent[RunContext]:
        """Extraction agent — reads PDF pages and returns structured BillingRecord output."""

        async def instructions(
            wrapper: RunContextWrapper[RunContext], agent: Agent
        ) -> str:
            return wrapper.context.prompt_loader.render(
                "extraction/system.j2", {}
            )

        return Agent[RunContext](
            name="extraction_agent",
            instructions=instructions,
            model="gpt-4.1",
            output_type=ExtractionOutput,
            tools=[],
        )
