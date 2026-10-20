import sys


def send_windows_notification(title: str, message: str) -> None:
    """
    Sends a native Windows Toast notification using winotify.
    Works reliably on Windows 10 and Windows 11. On other systems it does nothing.
    """
    if sys.platform != "win32":
        return

    try:
        from winotify import Notification

        toast = Notification(
            app_id="AI Content Engine",
            title=title,
            msg=message,
            duration="short"
        )
        toast.show()
    except Exception:
        pass
