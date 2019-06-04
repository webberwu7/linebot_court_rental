# coding=utf-8
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
            return view.AccountHelpView()
        else:
            second = inputTextToken.pop(0)

        # account/register/60747021s
        if second == 'register':
            if not inputTextToken:
                return view.TextView("Example :\n account/register/[your student id there]")

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
                    return view.AccountHobbyTimeHelpView(last_input=inputText)

                time = inputTextToken.pop(0)

                if not inputTextToken:
                    return view.AccountHobbyCourtHelpView(last_input=inputText)

                four = inputTextToken.pop(0)
                if four == 'court':
                    if not inputTextToken:
                        return view.AccountHelpView()

                    court = inputTextToken.pop(0)
                    return view.TextView(account.set_hobby(uid, time, court))

    elif first == 'search':
        search = controller.SearchController()

        if not inputTextToken:
            return view.SearchTimeHelpView()

        second = inputTextToken.pop(0)
        if second == 'time':
            if not inputTextToken:
                return view.SearchTimeHelpView()

            time = inputTextToken.pop(0)

            if not inputTextToken:
                return view.SearchCourtHelpView(last_input='search/time/'+str(time))

            third = inputTextToken.pop(0)
            if third == 'court':
                if not inputTextToken:
                    return view.SearchCourtHelpView(last_input='search/time/'+str(time))

                court = inputTextToken.pop(0)

                return search.find(time, court)

            else:
                return view.SearchTimeHelpView()

    elif first == 'booking':
        return view.TextView('booking something')

    elif first == 'maintain':
        if not inputTextToken:
            return view.MaintainHelpView()

        maintain = controller.MaintainController()
        second = inputTextToken.pop(0)

        if(second == 'all'):
            return view.TextView(maintain.get_maintains())

        elif(second == 'post'):
            if not inputTextToken:
                return view.MaintainPostHelpView()

            court = inputTextToken.pop(0)
            maintain.post_maintain(court, uid)
            return view.TextView('報修新增完成')

    elif first == 'bulletin':
        bulletin = controller.BulletinController()
        return view.TextView(bulletin.get_bulletins())

    elif first == 'help':
        return view.HelperView("小幫手", '指令')

    elif first == 'debug':
        return view.ButtonDataView('測試', 'debug')

    else:
        return view.HelperView("小幫手", '指令')
