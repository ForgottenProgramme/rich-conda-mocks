from rich.console import Console
from rich.table import Table

table = Table(title="Information about current conda install", show_header=False, leading=False, show_lines=True)

table.add_column("", style="dark_blue", no_wrap=True)
table.add_column("", style="dark_green", no_wrap=True)

table.add_row("active environment", "base")
table.add_row("active env location", "/Users/maheiramkhan/documents/github/conda/devenv/Darwin/arm64/envs/devenv-3.10-c")
table.add_row("shell level","1")
# end_section=True draws a line after the row. This shows when show_lines is set to False. Otherwise no effect
table.add_row("user config file", "/Users/maheiramkhan/.condarc")
virtual_packages = ["virtual packages","__archspec=1=m1","__conda=23.10.1.dev97+gcfbb1f175=0","__osx=13.6=0","__unix=0=0"]
virtual_packages_string="\n".join(virtual_packages)
table.add_row("virtual packages", virtual_packages_string) 
# Both "None" or empty "" can be used to create an empty cell
channel_urls=["https://repo.anaconda.com/pkgs/main/osx-arm64", "https://repo.anaconda.com/pkgs/main/noarch", "https://repo.anaconda.com/pkgs/r/osx-arm64", "https://repo.anaconda.com/pkgs/r/noarch]"]
channel_urls_string= "\n".join(channel_urls)  
table.add_row("channel URLS", channel_urls_string)  
console=Console()
console.print(table)
