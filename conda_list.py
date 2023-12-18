from rich.console import Console
from rich.table import Table

table = Table(title="packages in environment at <prefix_path>")

table.add_column("Name", style="dark_blue", no_wrap=True)
table.add_column("Version", style="magenta")
table.add_column("Build", style="dark_red")
table.add_column("Channel", style="dark_green")
                            
                                                        
table.add_row("anaconda-client", "1.12.1", "pyhd8ed1ab_1", "conda-forge")
table.add_row("backports", "1.1", "pyhd3eb1b0_0")
table.add_row("zipp", "3.11.0", "py310hca03da5_0")
table.add_row("yaml", "0.2.5", "h1a28f6b_0")
table.add_row("flake8-pyproject", "1.2.3", "pyhd8ed1ab_0", "conda-forge")
table.add_row("random-package", "1.2.3.4.5", "py1by2my3_0", "honda_torch")


console = Console()
console.print(table)