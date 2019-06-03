from controller import controller
from view import view


def parser_text(inputText):
    inputText = str(inputText).lower()
    inputTextToken = inputText.split('/')

    # check first token
    first = inputTextToken.pop(0)

    if first == 'account':
        account = controller.AccountController()

        if not inputTextToken:
            return view.TextView("input more account order")
        else:
            second = inputTextToken.pop(0)

        if second == 'register':
            return view.TextView(account.get_accounts())

    elif first == 'search':
        #second = inputTextToken.pop(0)
        search = controller.SearchController()

        # if second == 'court':
        #    return str(search.get_court())

        third = inputTextToken.pop(0)
        if third == 'Monday':
            return view.TextView(search.get_day(third))

    elif first == 'booking':
        return view.TextView('booking something')

    elif first == 'maintain':
        maintain = controller.MaintainController()
        return view.TextView(maintain.get_maintains())

    elif first == 'bulletin':
        bulletin = controller.BulletinController()
        return view.TextView(bulletin.get_bulletins())

    elif first == 'help':
        return view.HelperView("小幫手", '指令')

    else:
        return view.TextView("i don't know what you say")
