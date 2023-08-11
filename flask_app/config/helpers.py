from flask import session, request, redirect

def set_token(data):
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
        if len(history) > 0:
            if history[-1] != page:
                history.append(page)
                session['history'] = history

def page_back(qty=1):
    page = request.path
    if 'page_history' not in session:
        session['page_history'] = [page]
    last_page = '/'
    if len(session['page_history']) > 0:
        for time in range(qty):
            last_page = session['page_history'].pop()
    return last_page