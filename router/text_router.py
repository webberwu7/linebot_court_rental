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

            elif third == 'search':
                return account.hobby_search(uid)

            elif third == 'booking':
                return account.hobby_booking(uid)

        elif second == 'booking':
            if not inputTextToken:
                return view.AccountBookingHelpView()

            third = inputTextToken.pop(0)

            if third == 'list':
                return account.get_booking(uid)
            
            elif third == 'delete':
                if not inputTextToken:
                    return view.TextView("Example :\naccount/booking/delete/[your want delete id there]")
                
                booking = controller.BookingController()
                booking_id = inputTextToken.pop(0)

                return booking.delete(booking_id)
                

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
        booking = controller.BookingController()
        if not inputTextToken:
            return view.TimeHelpView(title='預約時間', text='請選擇預約時間', last_input='booking')

        second = inputTextToken.pop(0)
        if second == 'time':
            if not inputTextToken:
                return view.TimeHelpView(title='預約時間', text='請選擇預約時間', last_input='booking')

            time = inputTextToken.pop(0)

            if not inputTextToken:
                return view.CourtHelpView(title='預約地點', text='請選擇預約地點', last_input='booking/time/'+str(time))

            third = inputTextToken.pop(0)
            if third == 'court':
                if not inputTextToken:
                    return view.CourtHelpView(title='預約地點', text='請選擇預約地點', last_input='booking/time/'+str(time))

                court = inputTextToken.pop(0)

                return booking.store(uid, time, court)

            else:
                return view.TimeHelpView(title='預約時間', text='請選擇預約時間', last_input='booking')

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

    else:
        return view.HelperView("小幫手", '指令')
