import sys
import pytest
from pathlib import Path
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.schemas import TicketRequest

def test_valid_description():
  ticket = TicketRequest(description="This is a valid ticket description")
  assert ticket.description == "This is a valid ticket description"

def test_empty_description():
  with pytest.raises(ValidationError) as exc_info:
    TicketRequest(description="")

  assert "empty" in str(exc_info.value).lower()

def test_whitespace_only_description():
  with pytest.raises(ValidationError) as exc_info:
    TicketRequest(description="     ")
  
  assert "empty" in str(exc_info.value).lower() or "whitespace" in str(exc_info.value).lower()

def test_too_short_description():
  with pytest.raises(ValidationError) as exc_info:
    TicketRequest(description="Short")
  
  error_msg = str(exc_info.value)
  assert "too short" in error_msg. lower()
  assert "10" in error_msg

def test_strips_whitespace():
  ticket = TicketRequest(description="   Valid description here   ")
  assert ticket.description == "Valid description here"

def test_minimum_valid_length():
  ticket = TicketRequest(description="1234567890")
  assert len(ticket.description) == 10
  
def test_maximum_valid_lenght():
  long_text = "x" * 1500
  ticket = TicketRequest(description=long_text)
  assert len(ticket.description) == 1500
  
def test_too_long_description():
  with pytest.raises(ValidationError) as exc_info:
    TicketRequest(description="x" * 1501)
  
  error_msg = str(exc_info.value)
  assert "too long" in error_msg.lower()
  assert "1500" in error_msg