def formula_question_entity(item):
    used_value = item.get('used', False)  # Default False if not present
    if isinstance(used_value, str):
        used_value = used_value.lower() == 'true'
    return {
        "id": str(item.get("_id", "")),
        "class_": item.get("class_", ""),
        'subject': item.get("subject", ""),
        'topic': item.get("topic", ""),
        'question': item.get("question", ""),
        "options": item.get("options", []),
        'answers': item.get('answer', []),
        'resource': item.get('resource', []),
        'used': bool(item.get('used', False)) 
         # Added used field
    }

def formula_question_entitys(items):
    return [formula_question_entity(item) for item in items]