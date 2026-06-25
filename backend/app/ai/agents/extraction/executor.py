from __future__ import annotations

from agents import Agent, Runner

from app.ai.agents.factory import AgentFactory
from app.ai.context import RunContext
from app.core.common.logger import get_logger
from app.models.extraction import ExtractionOutput


class ExtractionAgentExecutor:
    """Runs the extraction agent over a document and returns structured billing records.

    Follows the same executor pattern as EchoAgentExecutor — see echo/executor.py.
    """

    def __init__(
        self,
        agent: Agent[RunContext] | None = None,
        max_turns: int = 25,
    ) -> None:
        self.agent = agent if agent is not None else AgentFactory.build_extraction_agent()
        self.max_turns = max(1, max_turns)
        self.logger = get_logger(__name__)

    async def run(self, ctx: RunContext) -> tuple[ExtractionOutput, object]:
        """Run the extraction agent and return (ExtractionOutput, usage).

        Args:
            ctx: RunContext with loaded document and prompt_loader.

        Returns:
            Tuple of structured extraction output and SDK usage object.
        """
        user_text =  ctx.prompt_loader.render(
            "extraction/user.j2",
            {
                "doc_id": ctx.document.doc_id,
                "total_pages": ctx.document.num_pages,
                "page_summaries": [
                    {"page_num": p.page_num, "preview": p.page_content[:300]}
                    for p in ctx.document.pages
                ],
            },
        )

        self.logger.info(
            "extraction_agent_started",
            doc_id=ctx.document.doc_id,
            num_pages=ctx.document.num_pages,
        )

        result = await Runner.run(
            self.agent,
            user_text,
            context=ctx,
            max_turns=self.max_turns,
        )

        output: ExtractionOutput = result.final_output

        self.logger.info(
            "extraction_agent_completed",
            doc_id=ctx.document.doc_id,
            records=len(output.records) if output else 0,
            flagged=len(output.flagged) if output else 0,
        )

        return output, result.context_wrapper.usage
