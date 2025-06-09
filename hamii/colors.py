"""
Hamii.colors module

Provides simple color codes that can be used in Python scripts
with easy {color} placeholders to colorize terminal output.
"""

class colors:
    # ANSI escape sequences for colors
    # Usage example:
    #   print(f"{colors.green}This will be green{colors.reset}")
    # or if you want to use placeholders {green}text{reset} in your own formatting functions

    reset = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    bright_black = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"

    @classmethod
    def format_text(cls, text: str) -> str:
        """
        Replace color names inside curly braces with actual ANSI codes.
        For example:
          "Hello {green}world{reset}!" => "Hello \033[32mworld\033[0m!"
        """
        mapping = {
            "{reset}": cls.reset,
            "{black}": cls.black,
            "{red}": cls.red,
            "{green}": cls.green,
            "{yellow}": cls.yellow,
            "{blue}": cls.blue,
            "{magenta}": cls.magenta,
            "{cyan}": cls.cyan,
            "{white}": cls.white,
            "{bright_black}": cls.bright_black,
            "{bright_red}": cls.bright_red,
            "{bright_green}": cls.bright_green,
            "{bright_yellow}": cls.bright_yellow,
            "{bright_blue}": cls.bright_blue,
            "{bright_magenta}": cls.bright_magenta,
            "{bright_cyan}": cls.bright_cyan,
            "{bright_white}": cls.bright_white,
        }
        for key, val in mapping.items():
            text = text.replace(key, val)
        return text

