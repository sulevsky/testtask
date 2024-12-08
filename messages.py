welcome_message = """
Welcome to the Test bot!
Please send your report in format
`longitude, latitude, target_type`
ex.
`48.567123 39.87897 tank`
Types are: tank, ifv, infantry
"""


def error_message(parse_error: str) -> str:
    return f"{parse_error}\n{welcome_message}"


ok_message = """
Thank you, message received!
"""
