def test_raffle_init(raffle):
  assert raffle.max_people == 10
  assert raffle.max_tickets == 100
  assert raffle.price_per_ticket == 5
  assert raffle.total_earnings == 0
  assert raffle.participants == {}

def test_add_participant_success(raffle):
  assert raffle.add_participant("Mohammad") is "SUCCESS"
  assert raffle.participants == {"Mohammad": 0}

def test_add_participant_failure(raffle):
  for index in range(raffle.max_people):
    raffle.add_participant("Person " + str(index))
  assert raffle.add_participant("Hasan") is "FAIL: you have reached the max number of people"

def test_buy_tickets_success_enough(raffle):
  raffle.add_participant("Yosef")
  assert raffle.buy_tickets("Yosef", 10) is "SUCCESS"
  assert raffle.participants["Yosef"] == 10
  assert raffle.total_earnings == 10 * raffle.price_per_ticket

def test_buy_tickets_success_not_enough(raffle):
  raffle.add_participant("Yosef")
  raffle.max_tickets = 10
  assert raffle.buy_tickets("Yosef", 11) is "FAIL: there is no enough tickets"
  assert raffle.participants["Yosef"] == 0
  assert raffle.total_earnings == 0

def test_buy_tickets_participant_not_found(raffle):
  assert raffle.buy_tickets("bakir", 1) == "FAIL: this person is not participated."