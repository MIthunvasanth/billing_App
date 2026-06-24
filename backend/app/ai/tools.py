from __future__ import annotations

from agents import function_tool
from agents.tool_context import ToolContext

from app.ai.context import RunContext


@function_tool
async def echo_tool(
    ctx: ToolContext[RunContext],
    message: str,
) -> str:
    """Echo a message back. Used only by the echo agent as a demonstration tool.

    Args:
        message: Any string to echo.

    Returns:
        The input string prefixed with 'Echo: '.
    """
    return f"Echo: {message}"


@function_tool
async def read_page(
    ctx: ToolContext[RunContext],
    page_num: int,
) -> str:
    """Read the full text content of a single PDF page.

    Args:
        page_num: 1-indexed page number to read.

    Returns:
        Full extracted text for that page, or an error string if out of range.
    """
    doc = ctx.context.document
    if page_num < 1 or page_num > doc.num_pages:
        return (
            f"Error: page {page_num} does not exist. "
            f"Document has {doc.num_pages} pages."
        )
    return doc.pages[page_num - 1].page_content


@function_tool
async def get_document_info(ctx: ToolContext[RunContext]) -> str:
    """Return a summary of the document: page count and a 150-character preview of each page.

    Returns:
        Multi-line string with page count and per-page previews.
    """
    doc = ctx.context.document
    lines = [f"Document has {doc.num_pages} pages.\n"]
    for page in doc.pages:
        preview = page.page_content[:150].replace("\n", " ")
        lines.append(f"Page {page.page_num} (preview): {preview}")
    return "\n".join(lines)
