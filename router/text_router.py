from controller import controller

def parser_text(inputText):
    inputText = str(inputText)
    inputTextToken = inputText.split('/')

    # check first token
    first = inputTextToken.pop(0)

    if first == 'account':
        second = inputTextToken.pop(0)
        account = controller.AccountController()

        if(second == 'register'):
            return str(account.get_accounts())

    elif first == 'search':
        #second = inputTextToken.pop(0)
        search = controller.SearchController()

        #if second == 'court':
        #    return str(search.get_court())
        
        third = inputTextToken.pop(0)
        if third == 'Monday':
            return str(search.get_day(third))

    elif first == 'booking':
        return 'booking something'
    
    elif first == 'maintain':
        maintain = controller.MaintainController()
        return str(maintain.get_maintains())

    elif first == 'bulletin':
        ##content
        ##time
        bulletin = controller.BulletinController()
        return str(bulletin.get_bulletins())

    else:
        return "i don't know what you say"
