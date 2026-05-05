"""Gmail SMTP notifier. Requires GMAIL_APP_PASSWORD."""
import smtplib
from email.message import EmailMessage
from datetime import datetime, timezone

from config import GMAIL_ADDRESS, GMAIL_APP_PASSWORD, NOTIFY_TO


def send_fill_email(fills: list[dict]) -> None:
    """fills = [{coin, exchange, tf, ratio, level_price, ts, current_price}]"""
    if not fills:
        return
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        print("[notify_email] GMAIL_ADDRESS / GMAIL_APP_PASSWORD not set, skipping email")
        return

    subject = f"Fib filled: {', '.join(_short(f) for f in fills[:3])}" + (
        f" (+{len(fills) - 3} more)" if len(fills) > 3 else ""
    )

    lines = ["Fib levels filled:\n"]
    for f in fills:
        ts = datetime.fromtimestamp(f["ts"] / 1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines.append(
            f"  {f['coin']} ({f['exchange']}) {f['tf']}  "
            f"fib {f['ratio']}  @ {f['level_price']:.4f}  "
            f"current {f['current_price']:.4f}  [{ts}]"
        )
    body = "\n".join(lines) + "\n"

    msg = EmailMessage()
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = NOTIFY_TO
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        s.send_message(msg)
    print(f"[notify_email] sent {len(fills)} fill(s) to {NOTIFY_TO}")


def _short(f: dict) -> str:
    return f"{f['coin']} {f['tf']} {f['ratio']}"
