INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


def validate_password(username, password):
    if password != username and password not in INVALID_PASSWORDS:
        return True
    raise InvalidPasswordError("nope")


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        validate_password(username, password)
    except InvalidPasswordError as e:
        print(e)
    else:
        account = create_account(username, password)


class InvalidPasswordError(KeyError):
    pass

main('jim', 'jam')
main('admin', 'password')  # Oh no!
main('guest', 'guest')  # Oh no!

