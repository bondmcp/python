"""BondMCP CLI"""
import click
import os
import json
from .client import BondMCPClient
from .exceptions import BondMCPError

@click.group()
@click.version_option(version="1.0.0")
def main():
    """BondMCP CLI - Health AI Platform Command Line Interface"""
    pass

@main.group()
def auth():
    """Authentication commands"""
    pass

@auth.command()
@click.option('--email', prompt=True, help='Your email address')
@click.option('--password', prompt=True, hide_input=True, help='Your password')
def login(email, password):
    """Login to BondMCP"""
    try:
        client = BondMCPClient()
        result = client.login(email, password)
        click.echo(f"✅ Login successful!")
        if 'api_key' in result:
            click.echo(f"API Key: {result['api_key']}")
            click.echo("Set environment variable: export BONDMCP_API_KEY=<your_key>")
    except BondMCPError as e:
        click.echo(f"❌ Login failed: {e}")

@auth.command()
@click.option('--email', prompt=True, help='Your email address')
@click.option('--password', prompt=True, hide_input=True, help='Your password')
@click.option('--name', prompt=True, help='Your full name')
def register(email, password, name):
    """Register for BondMCP"""
    try:
        client = BondMCPClient()
        result = client.register(email, password, name)
        click.echo(f"✅ Registration successful!")
        click.echo(f"User ID: {result.get('user_id', 'N/A')}")
        if 'api_key' in result:
            click.echo(f"API Key: {result['api_key']}")
            click.echo("Set environment variable: export BONDMCP_API_KEY=<your_key>")
    except BondMCPError as e:
        click.echo(f"❌ Registration failed: {e}")

@main.command()
@click.argument('question')
def ask(question):
    """Ask a health-related question"""
    try:
        client = BondMCPClient()
        result = client.ask(question)
        click.echo(json.dumps(result, indent=2))
    except BondMCPError as e:
        click.echo(f"❌ Error: {e}")

@main.command()
def health():
    """Check API health status"""
    try:
        client = BondMCPClient()
        result = client.health()
        click.echo(json.dumps(result, indent=2))
    except BondMCPError as e:
        click.echo(f"❌ Error: {e}")

if __name__ == '__main__':
    main()
