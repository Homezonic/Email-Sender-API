##  Problem Statement

You're an engineer working on the email system team at T-Shoes. The marketing team provides the HTML for the personalized emails, which have fields that need to be replaced with user information.

An incident was reported yesterday and you suspect the email validation code is not working as expected. You are responsible for fixing the validate_email_payload API implementation before more incidents occur.

The email payload contains a few parameters and all should be validated, and throws  ValueError  to the caller if anything does not meet the specifications:
- sender_name - Name of the sender

- sender_addr - Email address of the sender

- receiver_name - Name of the receiver

- receiver_addr - Email address of the receiver

- html - Body of the email to be sent

- replacements - Lookup dictionary for actual values to replace for placeholder value, used for email personalization

## Specifications

This code is expected to run in Python 3.5+.

#### Task 1: Validate names according to specification.

- Sender name should not be longer than 30 characters, and at least 5 characters

- Receiver name should not be longer than 60 characters, and at least 5 characters

- Ignore leading and trailing spaces duration validation

- Ensure that each validation failure raises ValueError

#### Task 2: Validate email addresses according to specification.

Both sender and receiver email addresses should conform to the requirements below:

- Email addresses must contain a single "@" character

- Total length of any email address no longer than 254 bytes

- Total length of the part before "@" no longer than 64 bytes

- Total length of the part after "@" no longer than 251 bytes

- Valid characters for an email address are: lower case characters, upper case characters, digits, "@", "-" and ".". However, the part after "@" does not allow periods aside from being used in
  the top layer domain (TLD) of the domain

- Hyphens (-) and dots (.) cannot occur as the first or last character of the part before @ of the email

- Email addresses must end in TLD of ".com", ".net", ".org"

- Ignore leading and trailing spaces duration validation

- Ensure that each validation failure raises ValueError

#### Task 3: Validate HTML and replacements according to specification.

replacements contains a list of key value pairs where the tag {key} in the html will then be replaced by the value. For example: "hello {name}!" with {'name': 'Jane'} will result in "hello Jane!".

Replacement values must be non-empty.

ValueError must be raised if one of the replacement keys is not present in the HTML, or there is a surplus of replacement keys not used.