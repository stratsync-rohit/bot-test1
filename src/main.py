import asyncio
import logging

from microsoft_teams.apps import App, ActivityContext
from microsoft_teams.api import MessageActivity


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

app = App()


@app.on_message
async def handle_message(
    ctx: ActivityContext[MessageActivity],
) -> None:
    message = (ctx.activity.text or "").strip().lower()

    logging.info(
        "Incoming message | type=%s | channel=%s | text=%s",
        ctx.activity.type,
        ctx.activity.channel_id,
        ctx.activity.text,
    )

    if message == "hello":
        await ctx.send(
            "Hello! Stratsync Risk Bot is running."
        )
        return

    if message == "help":
        await ctx.send(
            "Available commands:\n"
            "- hello\n"
            "- help\n"
            "- risk"
        )
        return

    if message == "risk":
        await ctx.send(
            "Risk ID: RSK-101\n"
            "Product: Burberry XYZ Perfume\n"
            "Severity: High\n"
            "Risk Value: $5,000"
        )
        return

    await ctx.send(
        f"You said: {ctx.activity.text}"
    )


async def main() -> None:
    await app.start()


if __name__ == "__main__":
    asyncio.run(main())