crew = {
  "Wallace": 25,
  "Jimmy": 23,
  "Petey": 15,
  "George": 12
}
crew = dict(sorted(crew.items()))

def spoils(spoils_total, expenses, captain_tax, crew):
    total = spoils_total - (spoils_total * expenses)
    crew_tax = total - captain_tax
    avg = crew_tax / len(crew)
    traitors = []
    poor = []
    for key, value in crew.items():
        if value > avg:
            traitors.append(key)
        elif value < avg:
            poor.append(key)
    if traitors:
        return f"{', '.join(sorted(traitors))} - Walk the plank!"
    if poor:
        return f"Captain needs his gold! Sorry {', '.join(sorted(poor))}"
    return "Yo-Ho. Yo-Ho. A pirate's life for me!"


print(spoils(100, .05, 20, crew))
