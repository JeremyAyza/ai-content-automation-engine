import random
import time
from functools import wraps
from typing import Callable, ParamSpec, Type, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def sleep_decorator(
    min_seconds: float, max_seconds: float
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator that introduces a random sleep within the specified range of seconds.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = func(*args, **kwargs)
            sleep_time = random.uniform(min_seconds, max_seconds)
            time.sleep(sleep_time)
            return result

        return wrapper

    return decorator


def retry(
    max_attempts: int = 3, delay: float = 0, exceptions: tuple[Type[Exception], ...] = (Exception,)
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator that retries a function a specified number of times on specific exceptions.
    """

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_exception: Exception | None = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts:
                        if delay > 0:
                            time.sleep(delay)
                        continue
            if last_exception:
                raise last_exception
            raise Exception("Max attempts reached")

        return wrapper

    return decorator

import sys

def sleep_with_countdown(seconds: int, message: str = "Esperando") -> None:
    """
    Sleeps for a specified number of seconds while displaying a live countdown in the terminal.
    This prevents the terminal from appearing frozen.
    """
    for remaining in range(int(seconds), 0, -1):
        mins, secs = divmod(remaining, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        # Print with carriage return (\r) to overwrite the same line
        sys.stdout.write(f"\r⏳ {message}: {time_format} restantes...")
        sys.stdout.flush()
        time.sleep(1)
    
    # Clear the line when done
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()

import threading
from contextlib import contextmanager

@contextmanager
def api_spinner(message: str = "Consultando API"):
    """
    Context manager that displays a live stopwatch in the terminal while the block executes.
    Used for long-running synchronous API calls to prevent the terminal from appearing frozen.
    """
    stop_event = threading.Event()
    
    def spinner_task():
        start_time = time.time()
        while not stop_event.is_set():
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            sys.stdout.write(f"\r⏳ {message} [{mins:02d}:{secs:02d}]...")
            sys.stdout.flush()
            stop_event.wait(1)
            
    thread = threading.Thread(target=spinner_task, daemon=True)
    thread.start()
    
    try:
        yield
    finally:
        stop_event.set()
        thread.join(timeout=2)
        sys.stdout.write("\r" + " " * 80 + "\r")
        sys.stdout.flush()

import concurrent.futures

def run_with_timeout(func, timeout_seconds, *args, **kwargs):
    """
    Executes a function in a background thread and waits for the result with a strict timeout.
    This prevents the main thread from freezing if the underlying socket hangs silently.
    """
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(func, *args, **kwargs)
    try:
        return future.result(timeout=timeout_seconds)
    except concurrent.futures.TimeoutError:
        executor.shutdown(wait=False)
        raise TimeoutError(f"Operación bloqueada por más de {timeout_seconds}s. Cancelada por seguridad.")
    finally:
        executor.shutdown(wait=False)
