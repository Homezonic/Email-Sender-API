import html
import re
import pytest

def validate_names(sender_name, receiver_name):
    # Remove leading and trailing spaces
    sender_name = sender_name.strip()
    receiver_name = receiver_name.strip()
    # Validate sender_name
    if len(sender_name) < 5 or len(sender_name) > 30:
        raise ValueError("Invalid sender name: should be between 5 and 30 characters long")

    # Validate receiver_name
    if len(receiver_name) < 5 or len(receiver_name) > 60:
        raise ValueError("Invalid receiver name: should be between 5 and 60 characters long")

def validate_email_address(email_addr):
    # Remove leading and trailing spaces
    email_addr = email_addr.strip()

    # Validate total length
    if len(email_addr) > 254:
        raise ValueError("Invalid email address: total length should be no longer than 254 bytes")

    # Split email address into username and domain parts
    try:
        username, domain = email_addr.split("@")
    except ValueError:
        raise ValueError("Invalid email address: must contain a single '@' character")

    # Validate username length
    if len(username) > 64:
        raise ValueError("Invalid email address: username part should be no longer than 64 bytes")

    # Validate domain length
    if len(domain) > 251:
        raise ValueError("Invalid email address: domain part should be no longer than 251 bytes")

    # Validate valid characters for email address
    if not all(c.islower() or c.isupper() or c.isdigit() or c in ["@", "-", "."] for c in email_addr):
        raise ValueError("Invalid email address: contains invalid characters")

    # Validate domain TLD
    valid_tlds = [".com", ".net", ".org"]
    if not any(domain.endswith(tld) for tld in valid_tlds):
        raise ValueError("Invalid email address: domain must end in '.com', '.net', or '.org'")

    # Validate that hyphens or dots are not first or last characters of username
    if username.startswith("-") or username.endswith("-") or \
       username.startswith(".") or username.endswith("."):
        raise ValueError("Invalid email address: hyphens or dots cannot be first or last characters of username")

    # Validate that dots (.) can only appear in TLD part of the domain
    if domain.count(".") > 1 or (domain.count(".") == 1 and not domain.endswith(tuple(valid_tlds))):
        raise ValueError("Invalid email address: dots (.) can only appear in TLD part of the domain")
def validate_html_replacements(html, replacements):
    # Check that all replacement keys in html are present in replacements
    html_keys = set(re.findall(r'\{(\w+)\}', html))
    replacement_keys = set(replacements.keys())
    if html_keys - replacement_keys:
        raise ValueError("Invalid replacements: some replacement keys are not present in the HTML")

    # Check that all replacements are non-empty
    if any(not replacements[key] for key in replacements):
        raise ValueError("Invalid replacements: all replacement values must be non-empty")

    # Check that there are no surplus replacement keys not used in html
    if replacement_keys - html_keys:
        raise ValueError("Invalid replacements: surplus replacement keys not used in the HTML")

def validate_email_payload(payload):
    sender_name = payload.get("sender_name", "")
    receiver_name = payload.get("receiver_name", "")
    sender_addr = payload.get("sender_addr", "")
    receiver_addr = payload.get("receiver_addr", "")
    validate_names(sender_name, receiver_name)
    validate_email_address(sender_addr)
    validate_email_address(receiver_addr)
    html = payload.get("html", "")
    replacements = payload.get("replacements", {})
    validate_html_replacements(html, replacements)

    # continue with the other validations...



#Some series of test units for valid and invalid cases
def test_validate_email_payload():
    # Valid payload
    payload = {
        "sender_name": "Johnson",
        "sender_addr": "john@example.com",
        "receiver_name": "Janet",
        "receiver_addr": "jane@example.com",
        "html": "Hello {name}!",
        "replacements": {"name": "Janet"}
    }
    validate_email_payload(payload)

    # Invalid sender name
    payload = {
        "sender_name": "J",
        "sender_addr": "john@example.com",
        "receiver_name": "Janet",
        "receiver_addr": "jane@example.com",
        "html": "Hello {name}!",
        "replacements": {"name": "Janet"}
    }
    with pytest.raises(ValueError):
        validate_email_payload(payload)

    # Invalid receiver name
    payload = {
        "sender_name": "Johnson",
        "sender_addr": "john@example.com",
        "receiver_name": "J",
        "receiver_addr": "jane@example.com",
        "html": "Hello {name}!",
        "replacements": {"name": "Jane"}
    }
    with pytest.raises(ValueError):
        validate_email_payload(payload)

    # Invalid sender address
    payload = {
        "sender_name": "John",
        "sender_addr": "john",
        "receiver_name": "Jane",
        "receiver_addr": "jane@example.com",
        "html": "Hello {name}!",
        "replacements": {"name": "Jane"}
    }
    with pytest.raises(ValueError):
        validate_email_payload(payload)

    # Invalid receiver address
    payload = {
        "sender_name": "John",
        "sender_addr": "john@example.com",
        "receiver_name": "Jane",
        "receiver_addr": "jane",
        "html": "Hello {name}!",
        "replacements": {"name": "Jane"}
    }
    with pytest.raises(ValueError):
        validate_email_payload(payload)

    # Invalid HTML and replacements
    payload = {
        "sender_name": "John",
        "sender_addr": "john@example.com",
        "receiver_name": "Jane",
        "receiver_addr": "jane@example.com",
        "html": "Hello {name}!",
        "replacements": {"age": "30"}
    }
    with pytest.raises(ValueError):
        validate_email_payload(payload)





print (test_validate_email_payload())