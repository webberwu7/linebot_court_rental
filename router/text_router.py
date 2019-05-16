from controller import controller


def parser_text(inputText):
    inputText = str(inputText)
    inputTextToken = inputText.split('/')

    # check first token
    first = inputTextToken.pop(0)

    if first == 'account':
        account = controller.AccountController()
        return str(account.get_accounts())

    elif first == 'search':
        return 'search manager'

    elif first == 'booking':
        return 'booking something'

    else:
        return "i don't know what you say"
