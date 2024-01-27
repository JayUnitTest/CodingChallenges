import click

@click.group()
def cli():
    pass

def read_file(fin, num_lines):
    with open(fin, "r") as f_in:
            lines = [f_in.readline().strip() for _ in range(num_lines)]
    return lines

@cli.command()
@click.argument('fin', type=click.Path(exists=True))
@click.option('-n', '--num-lines', default=5, type= int, help = "Number of lines to return from file (default is 5)")
def head(fin, num_lines):
    print("returning line(s)...\n")
    lines = read_file(fin, num_lines)
    for line in lines:
        click.echo(line.rstrip())

@cli.command()
@click.argument('fin', nargs=2, type=click.File(mode="r"))
def cat(fin):
    for file in fin:
        click.echo(file.read().strip())
    

if __name__ == "__main__":
    cli()