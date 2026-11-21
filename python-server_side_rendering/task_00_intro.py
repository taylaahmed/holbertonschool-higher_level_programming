#!/usr/bin/python3

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname):s %(message)s")

PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        logging.error(
            f"Invalid input: template must be a string"
            f"got {type(template).__name__}"
            )
        return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        logging.error(
            f"Invalid input: attendees must be a list of dictionaries"
            f"got {type(attendees).__name__}"
        )
        return

    if not template.strip():
        logging.error(
            f"Template is empty"
        )
        return

    if not attendees:
        logging.error(
            f"Attendees is empty"
        )
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in PLACEHOLDERS:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as file:
                file.write(content)
        except OSError as e:
            logging.error(f"Could not write {filename}")
