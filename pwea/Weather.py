from rich.console import Console, ConsoleOptions, RenderResult
from rich.panel import Panel
from rich.table import Table

from datetime import date, timedelta


class CurrentWeather:
    """Class which contains and displays renderables for the current
    weather report. Uses the rich library to create a nice Panel
    object on the user's console."""
    def __init__(self, renderables):
        self.renderables = renderables

    def __rich_console__(self, console: Console,
                         options: ConsoleOptions) -> RenderResult:
        yield Panel(self.renderables, expand=False)


class ForecastWeather:
    """Class which contains and displays renderables for the
    forecasted weather report. Uses the rich library to create a nice
    Table object on the user's console."""
    def __init__(self, renderables, header_color):
        self.renderables = renderables
        self.header_color = f"[{header_color}]"

    def __rich_console__(self, console: Console,
                         options: ConsoleOptions) -> RenderResult:
        renderable_table = Table()
        for day in range(len(self.renderables)):
            renderable_table.add_column(f"{self.header_color}{date.today()+timedelta(day+1)}")
        renderable_table.add_row(*self.renderables.values())
        yield renderable_table
