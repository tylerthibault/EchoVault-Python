from flask import session, request, redirect

def set_token(data):
    print(f"data: {data}")
    session['token'] = {
        'id': data['id'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'level': data['level'],
    }

def page_history():
    page = request.path
    if 'page_history' not in session:
        session['page_history'] = [page]
    else:
        history = session['page_history']
        if history[-1] != page:
            history.append(page)
            session['history'] = history
        print(page, session['page_history'])

def page_back(qty=1):
    if 'page_history' not in session:
        return redirect('/')
    last_page = ''
    for time in range(qty):
        last_page = session['page_history'].pop()
    return last_page