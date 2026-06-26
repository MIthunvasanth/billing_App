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
                "summary billing ledgers.\n\n"
                "A SUMMARY page has ALL of these traits:\n"
                "- Many rows (typically 10 or more billing records visible in the preview)\n"
                "- Each row is compact: date | CPT codes | total charges | ins paid | adjustment | balance\n"
                "- Minimal narrative text — mostly tabular data\n"
                "- Often appears near the beginning of the document\n\n"
                "A DETAIL/ITEMIZED page has these traits:\n"
                "- Only 1–3 records per page\n"
                "- Each record is expanded with many line items, descriptions, or narrative\n"
                "- More text per record than a summary page\n\n"
                "IMPORTANT: Prefer the most compact page (highest record density). "
                "If one page clearly has 10+ date entries vs another with 1–2, "
                "the dense page is the summary.\n\n"
                "Cover pages, signature pages, and authorization pages are NOT summary pages.\n"
                "Return has_summary=true and ALL matching summary page numbers."
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
