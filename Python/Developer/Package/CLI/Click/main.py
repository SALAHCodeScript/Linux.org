import click

@click.command()
@click.version_option('1.0')
def main():
    print("hello, world")

if __name__ == "__main__":
    main()
