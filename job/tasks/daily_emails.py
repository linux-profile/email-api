import os

from datetime import date, timedelta
from email_profile import Email
from dotenv import load_dotenv


def main():
    load_dotenv()

    app = Email(
        server=os.getenv("EMAIL_SERVER"),
        user=os.getenv("EMAIL_USERNAME"),
        password=os.getenv("EMAIL_PASSWORD")
    )

    query = app.select(mailbox="Inbox").where(
        since=date.today(),
        before=date.today() + timedelta(days=1)
    )

    data = query.list_data()

    for content in data:
        print(content.email.subject)


if __name__ == '__main__':
    main()
