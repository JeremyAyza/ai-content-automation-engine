from winotify import Notification


def send_windows_notification(title: str, message: str) -> None:
    """
    Sends a native Windows Toast notification using winotify.
    Works reliably on Windows 10 and Windows 11.
    """
    try:
        toast = Notification(
            app_id="AI Content Engine",
            title=title,
            msg=message,
            duration="short"
        )
        toast.show()
    except Exception:
        pass
