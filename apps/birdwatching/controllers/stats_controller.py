from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from py4web.utils.url_signer import URLSigner

from ..common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from ..models import get_user_email

url_signer = URLSigner(session)

@action("stats")
@action.uses('stats.html', db, auth)
def stats():
    return dict()