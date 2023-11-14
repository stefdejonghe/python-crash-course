import time

# Start with some designs that need to be printed
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        time.sleep(0.5)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(
    unprinted_designs[:], completed_models
)  # unprinted_designs[:] zorgt ervoor dat er een kopie wordt meegestuurd, niet de originele lijst.
# Alleen te gebruiken als je de originele list wenst te behouden.
show_completed_models(completed_models)
