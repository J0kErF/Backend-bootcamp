import pytest
from src.raffle import Raffle
@pytest.fixture

### this fixture added for asserting that the constructor works correctly
@pytest.fixture
def raffle(max_people=10, max_tickets=100, price_per_ticket=5):
  return Raffle(max_people, max_tickets, price_per_ticket)