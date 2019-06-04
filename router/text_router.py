from controller import controller
from view import view


def parser_text(inputText, uid):
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

        # account/register/60747021s
        if second == 'register':
            third = inputTextToken.pop(0)
            answer = account.store(uid, third)
            return view.TextView(answer)

        # account/hobby/time/1/court/1
        elif second == 'hobby':
            if not inputTextToken:
                return view.TextView(account.get_hobby(uid))

            third = inputTextToken.pop(0)

            if third == 'time':
                if not inputTextToken:
                    return view.TextView('more infomation')
                
                time = inputTextToken.pop(0)
                
                if not inputTextToken:
                    return view.TextView('more infomation')
                
                four = inputTextToken.pop(0)
                if four == 'court':
                    if not inputTextToken:
                        return view.TextView('more infomation')

                    court = inputTextToken.pop(0)
                    return view.TextView(account.set_hobby(uid, time, court))

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

    elif first == 'debug':
        return view.ButtonDataView('測試', 'debug')

    else:
        return view.TextView("i don't know what you say")
