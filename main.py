from credentials import username, password, token, chat_id
from datetime import date

from auth import AuthServer, AuthUser
from register import Register
from log import Logger


user = AuthUser(username, password)

server = AuthServer(user)
register = Register(server)
logger = Logger(token, chat_id)

server.authenticate()
pods = register.pods()


for pod in pods:
    # exceptions to registering
    if date.today() >= pod.date:
        break

    if not pod.available or pod.closed:
        break

    if pod.available == 0:
        break

    # try to register
    try:
        pod.register()
        logger.log(f"✓ {pod} ➟ geregistreerd!")
    except:
        logger.log(f"x {pod} ➟ mislukt...")