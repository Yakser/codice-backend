def generate_slug_from_id(paste_id: int) -> str:
    return hex(paste_id)[2:]
