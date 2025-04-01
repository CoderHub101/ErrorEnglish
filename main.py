import click
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@click.group()
def cli():
    """Error English CLI tool for managing error messages"""
    pass

@cli.command()
@click.argument('error_code')
def lookup(error_code):
    """Look up an error code explanation"""
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT message FROM errors WHERE code = %s", (error_code,))
    result = cur.fetchone()
    
    if result:
        click.echo(f"Error {error_code}: {result[0]}")
    else:
        click.echo(f"No explanation found for error code: {error_code}")
    
    cur.close()
    conn.close()

if __name__ == '__main__':
    cli()