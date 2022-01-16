
app = None

session = None

redis = None


def init_default(_app):
    global app, session, redis
    app = _app
    session = app.Session()
    redis = app.Redis


def check_redis():
    if redis:
        return redis.keys("*")
    return 0


def check_app():
    if app:
        return app.config
    return None


def check_session():

    if session:
        proxy = session.execute(
            """
            SELECT * FROM leads.campaigns
            """,
        )
        return proxy.fetchone()
    return 0
