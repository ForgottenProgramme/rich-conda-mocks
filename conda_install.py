import time

from rich.progress import Progress
from rich.console import Console
from rich.table import Table

with Progress() as progress:

    task1 = progress.add_task("Retrieving notices", total=100)
    while not progress.finished:
        progress.update(task1, advance=0.7)
        time.sleep(0.02)

print("Channels:\n  - defaults\n  - conda-forge\n")
print("Platform: osx-arm64")

with Progress() as progress:

    task2 = progress.add_task("Collecting package metadata (repodata.json)", total=100)
    task3 = progress.add_task("Solving environment", total=100)
    while not progress.finished:
            progress.update(task2, advance=0.6)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)

table = Table(title="WARNING: A new version of conda exists:", title_justify="left", show_header=False, show_lines=True, style= "black")

table.add_column("", style="dark_blue", no_wrap=True)
table.add_column("", style="dark_green", no_wrap=True)

table.add_row("Current Version", "23.10.1.dev99+g849ad6661")
table.add_row("Latest Version", "23.11.0")

console=Console()
console.print(table)

print("Please update conda by running\n    $ conda update -n base -c defaults conda")

table2= Table(show_header=False, show_lines=True, style= "black")

table2.add_column("", style="dark_blue", no_wrap=True)
table2.add_column("", style="dark_green", no_wrap=True)

table2.add_row("Environment location", "/Users/some_name/documents/github/conda/devenv/Darwin/arm64/envs/devenv-3.10-c/envs/demo")
table2.add_row("Added/Updated Spec", "numpy")

console.print(table2)
# The following packages will be downloaded:

table_download= Table(title="The following packages will be downloaded:", title_justify="left",
                      show_header=True, show_lines=True, style="black", header_style="black")

table_download.add_column("Name", style="dark_blue", no_wrap=True)
table_download.add_column("Version", style="dark_green", no_wrap=True)
table_download.add_column("Build", style="dark_green", no_wrap=True)
table_download.add_column("Size", style="dark_green", no_wrap=True)

download_packages=(("llvm-openmp", "14.0.6", "hc6e5704_0", "253 KB"), ("B", "1.3.4", "silly_0", "266 KB"), ("C", "1.6.7", "funny_0", "700 KB"), ("D", "5.6.7", "crazy_0", "67 KB"))

for package in download_packages:
     table_download.add_row(*package)

console.print(table_download)

table_install=Table(title="The following NEW packages will be INSTALLED", title_justify="left", style="black", show_header=True,show_lines=True)

table_install.add_column("Name", style="dark_blue", no_wrap=True)
table_install.add_column("Version", style="dark_green", no_wrap=True)
table_install.add_column("Build", style="dark_green", no_wrap=True)
table_install.add_column("Channel", style="dark_green", no_wrap=True)
table_install.add_column("Subdir", style="dark_green", no_wrap=True)

install_packages=(("bzip2", "1.0.8", "h620ffc9_4", "pkgs/main", "osx-arm64"), ("some_package", "1.0.0", "something_4", "pkgs/main", "osx-arm64"), ("some_package", "1.0.0", "something_4", "pkgs/main", "osx-arm64"), ("some_package", "1.0.0", "something_4", "pkgs/main", "osx-arm64"))

for package in install_packages:
     table_install.add_row(*package)

console.print(table_install)