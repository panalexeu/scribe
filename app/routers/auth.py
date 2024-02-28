from typing import Annotated

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuthError

from ..oauth import setup_google_oauth

router = APIRouter(
    prefix='/auth'
)


@router.get('/login')
async def login(request: Request, oauth: Annotated[setup_google_oauth, Depends()]):
    redirect_uri = request.url_for('auth')
    print(redirect_uri)
    # referer = request.headers.get('Referer')
    # print(referer)
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get('/verify')
async def auth(request: Request, oauth: Annotated[setup_google_oauth, Depends()]):
    try:
        access_token = await oauth.google.authorize_access_token(request)
        print(request)
    except OAuthError:
        return HTTPException(status_code=403, detail='Oops, something went wrong')

    user_data = await oauth.google.parse_id_token(request, access_token)
    print(user_data)
    request.session['user'] = dict(user_data)

    return RedirectResponse('docs')


@router.get('/logoout')
async def logout(request: Request):
    request.session.pop('user', None)

