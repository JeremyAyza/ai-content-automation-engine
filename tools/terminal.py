import ctypes
import os

def disable_quick_edit() -> None:
    """
    Disables QuickEdit mode in the Windows command prompt/PowerShell terminal to prevent
    the script from freezing/pausing when the terminal window is clicked or goes into the background.
    Only works on Windows.
    """
    if os.name != 'nt':
        return

    try:
        kernel32 = ctypes.windll.kernel32
        # STD_INPUT_HANDLE is -10
        STD_INPUT_HANDLE = -10
        handle = kernel32.GetStdHandle(STD_INPUT_HANDLE)
        
        # Get current console mode
        mode = ctypes.c_uint()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            # ENABLE_QUICK_EDIT_MODE is 0x0040
            # ENABLE_EXTENDED_FLAGS is 0x0080
            # To modify QuickEdit, ENABLE_EXTENDED_FLAGS must also be set/cleared correctly.
            ENABLE_QUICK_EDIT_MODE = 0x0040
            ENABLE_EXTENDED_FLAGS = 0x0080
            
            # Clear QuickEdit flag and ensure extended flags is set
            new_mode = (mode.value & ~ENABLE_QUICK_EDIT_MODE) | ENABLE_EXTENDED_FLAGS
            kernel32.SetConsoleMode(handle, new_mode)
    except Exception:
        pass
