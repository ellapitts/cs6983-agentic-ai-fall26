"""Husky Tech support agent — the ticket record.

Transfer target for W03b.1 section 7, with one change you must make:
file_ticket takes the model as an ARGUMENT instead of reaching for a
notebook global. Files have no globals to lean on; dependencies are passed in.
"""

from typing import Literal
from unittest import result

from pydantic import BaseModel, Field

class TicketRecord(BaseModel):

TICKETS = []


def file_ticket(model, result):
    """Extract a structured record from a finished conversation and save it."""
    TICKETS = []
    """Extract a structured record from a finished conversation and save it."""
    transcript = "\n".join(f"{type(m).__name__}: {m.text}" for m in result["messages"] if m.text)
    record = model.with_structured_output(TicketRecord).invoke(
        f"Create a ticket record for this support conversation:\n\n{transcript}")
    TICKETS.append(record)
    return record

file_ticket(result)

TICKETS = []