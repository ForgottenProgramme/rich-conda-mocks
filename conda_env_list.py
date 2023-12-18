from rich.console import Console
from rich.table import Table

table = Table(title="conda environments")

table.add_column("Name", style="dark_blue", no_wrap=True)
table.add_column("Prefix", style="dark_green")
                            
                                                        
table.add_row("", "/Users/name/Documents/github/conda/devenv/Darwin/arm64/envs/devenv-3.10-c")
table.add_row("", "/Users/name/Documents/github/conda/devenv/Darwin/arm64/envs/devenv-3.8-c")
table.add_row("", "/Users/name/documents/github/conda/devenv/Darwin/arm64")
table.add_row("base", "/Users/name/documents/github/conda/devenv/Darwin/arm64/envs/devenv-3.10-c")
table.add_row("demo", "/Users/name/documents/github/conda/devenv/Darwin/arm64/envs/devenv-3.10-c/envs/demo")


console=Console()
console.print(table)

# TODO: 
# Figure out how to highlight the current environment (presently conda puts a '*' in front of the active env)