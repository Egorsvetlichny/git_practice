# Модуль validators позволяет использовать уже готовые валидаторы для самых распространенных задач.

import validators
from validators import ValidationError
from validators.utils import validator


# Decorator for your functions
@validator
def even(value):
    return value % 2 == 0


def main():
    # Emails
    assert validators.email('test@mail.ru') is True
    assert validators.email('fkhor@inbox.ru') is True

    # Urls
    assert validators.url('https://example.com') is True
    assert validators.url('https://10.0.0.1') is True

    # Mac address
    assert validators.mac_address('01:23:45:67:ab:CD') is True

    # Slug
    assert validators.slug('my-slug-2134')

    # Ipv4
    assert validators.ipv4('123.0.0.7') is True

    # Ipv6
    assert validators.ipv6('abcd:ef::42:1') is True

    # Iban
    assert validators.iban('DE29100500001061045672') is True

    # Domain
    assert validators.domain('example.com') is True

    # Uuid
    assert validators.uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8') is True

    try:
        # Failed assert
        assert validators.email('testmail.ru') is True
    except AssertionError:
        assert isinstance(validators.email('testmail.ru'), ValidationError) is True
        assert isinstance(validators.email('fkhor@inbox'), ValidationError) is True
        assert isinstance(validators.url('https//example.com'), ValidationError) is True
        assert isinstance(validators.url('https//example.com'), ValidationError) is True
        assert isinstance(validators.url('https://10.0.01'), ValidationError) is True
        assert isinstance(validators.url('https://10.0.0'), ValidationError) is True
        assert isinstance(validators.mac_address('00:00:fsd00:00:00'), ValidationError) is True
        assert isinstance(validators.ipv4('900.0.0.7'), ValidationError) is True
        assert isinstance(validators.ipv6('abcd:ef::421fs2:1'), ValidationError) is True
        assert isinstance(validators.domain('examplecom'), ValidationError) is True
        assert isinstance(validators.slug('my.slug-2134'), ValidationError) is True
        assert isinstance(validators.iban('lalala3131DE29100500001061045672'), ValidationError) is True
        assert isinstance(validators.uuid('2bc1c94f'), ValidationError) is True

        assert even(4) is True
        assert isinstance(even(3), ValidationError) is True


if __name__ == '__main__':
    main()
