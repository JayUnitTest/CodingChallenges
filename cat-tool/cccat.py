import click
import sys


def read_file(filenames):
    if not filenames:
        for line in sys.stdin:
            yield line.strip()
    else:
        for file in filenames:
            with open(file, 'r') as f:
                for line in f:
                    yield line.strip()

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
@click.option("-n", "number_lines", is_flag=True, help="Number the lines outputted to the console")
@click.option("-b", "exclude_blank_lines", is_flag=True, help= "Number lines but exclude blank lines being numbered in output.")
def cc_cat(filenames, number_lines, exclude_blank_lines):
     
    lines = read_file(filenames)
    if number_lines:
        for i, line in enumerate(lines, start=1):
            click.echo(f"{i}: {line.strip()}")
    elif exclude_blank_lines:
        for i, line in enumerate(lines, start=1):
            if line.strip() == "":
                click.echo("")
            else:
                click.echo(f"{i}: {line.strip()}")
    else:
        for line in lines:
            click.echo(line.strip())

if __name__ == "__main__":
    cc_cat()