def validate_user(new_name, checklist):
    for usuarios in checklist:
        if usuario['nome'].lower() == new_name.lower():
            return False
    return True
  