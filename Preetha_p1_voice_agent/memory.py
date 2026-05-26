context_memory = []

def add_to_memory(text):
    context_memory.append(text)

    # Keep only last 5 commands
    if len(context_memory) > 5:
        context_memory.pop(0)


def get_context():
    return "\n".join(context_memory)