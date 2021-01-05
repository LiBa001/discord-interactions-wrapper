from discord_interactions.flask_ext import Interactions
from discord_interactions import InteractionResponse, InteractionResponseType, InteractionApplicationCommandCallbackData
from discord_interactions.ocm import Command, Option
from flask import Flask
import os

app = Flask(__name__)
interactions = Interactions(app, os.getenv("CLIENT_PUBLIC_KEY"))


class _Echo(Command):
    """ what goes around comes around """

    message: str = Option("This will be echoed.", required=True)


@interactions.command()
def _echo(cmd: _Echo):
    msg = cmd.message

    return InteractionResponse(
        response_type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        data=InteractionApplicationCommandCallbackData(content=msg)
    )


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
