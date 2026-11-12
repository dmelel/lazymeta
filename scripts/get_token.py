#!/usr/bin/env python3
"""Interactive Meta Token Helper for LazyMeta.

Automatically converts a short-lived Graph API Explorer token into a
permanent, NEVER-EXPIRING Facebook Page Access Token and configures .env.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()

GRAPH_VERSION = "v22.0"
BASE_URL = f"https://graph.facebook.com/{GRAPH_VERSION}"


def print_header() -> None:
    banner = (
        "[bold cyan]LazyMeta Permanent Token Generator[/bold cyan]\n"
        "[dim]Instantly convert 1-hour tokens into Never-Expiring Page Tokens[/dim]"
    )
    console.print(Panel(banner, border_style="cyan"))


def get_token_flow() -> None:
    print_header()

    console.print("\n[bold]Step 1: Enter your Meta App Details (from App Settings > Basic)[/bold]")
    app_id = Prompt.ask("[cyan]Enter App ID[/cyan]").strip()
    if not app_id:
        console.print("[red]App ID is required.[/red]")
        sys.exit(1)

    app_secret = Prompt.ask("[cyan]Enter App Secret[/cyan]", password=True).strip()
    if not app_secret:
        console.print("[red]App Secret is required.[/red]")
        sys.exit(1)

    console.print("\n[bold]Step 2: Enter the Short-Lived User Token (from Graph API Explorer)[/bold]")
    short_token = Prompt.ask("[cyan]Paste Short-Lived Token[/cyan]").strip()
    if not short_token:
        console.print("[red]Short-lived token is required.[/red]")
        sys.exit(1)

    # 1. Exchange short-lived token for 60-day long-lived user token
    console.print("\n[dim]1/3 Exchanging short-lived token for 60-day User Token...[/dim]")
    exchange_url = f"{BASE_URL}/oauth/access_token"
    exchange_params = {
        "grant_type": "fb_exchange_token",
        "client_id": app_id,
        "client_secret": app_secret,
        "fb_exchange_token": short_token,
    }

    try:
        resp = requests.get(exchange_url, params=exchange_params, timeout=15)
        data = resp.json()
        if resp.status_code != 200 or "access_token" not in data:
            error_msg = data.get("error", {}).get("message", resp.text)
            console.print(f"[bold red]✗ Token Exchange Failed:[/bold red] {error_msg}")
            sys.exit(1)
        long_lived_user_token = data["access_token"]
        console.print("[bold green]✓ Success:[/bold green] Acquired 60-day Long-Lived User Token.")
    except Exception as e:
        console.print(f"[bold red]✗ Network Error during exchange:[/bold red] {e}")
        sys.exit(1)

    # 2. Query /me/accounts using the long-lived token to get NEVER-EXPIRING Page tokens
    console.print("[dim]2/3 Querying /me/accounts for Permanent Page Access Tokens...[/dim]")
    accounts_url = f"{BASE_URL}/me/accounts"
    try:
        resp = requests.get(accounts_url, params={"access_token": long_lived_user_token}, timeout=15)
        data = resp.json()
        if resp.status_code != 200 or "data" not in data:
            error_msg = data.get("error", {}).get("message", resp.text)
            console.print(f"[bold red]✗ Failed to fetch Pages:[/bold red] {error_msg}")
            sys.exit(1)

        pages = data.get("data", [])
        if not pages:
            console.print("[bold red]✗ No Facebook Pages found for this account.[/bold red]")
            console.print("[yellow]Ensure your account has admin access to at least one Facebook Page.[/yellow]")
            sys.exit(1)

        console.print(f"\n[bold green]✓ Found {len(pages)} Facebook Page(s):[/bold green]")
        for idx, page in enumerate(pages, start=1):
            name = page.get("name", "Unknown Page")
            pid = page.get("id", "Unknown ID")
            console.print(f"  [bold cyan][{idx}][/bold cyan] {name} [dim](ID: {pid})[/dim]")

        # Selection if multiple pages
        selected_page = pages[0]
        if len(pages) > 1:
            choice = Prompt.ask(
                "\n[cyan]Select Page number to configure for LazyMeta[/cyan]",
                choices=[str(i) for i in range(1, len(pages) + 1)],
                default="1",
            )
            selected_page = pages[int(choice) - 1]

        target_name = selected_page.get("name")
        target_id = selected_page.get("id")
        permanent_page_token = selected_page.get("access_token")

        console.print(f"\n[bold green]✓ Target Page Selected:[/bold green] [bold]{target_name}[/bold]")
        console.print(f"[bold green]✓ Permanent Page Token Acquired![/bold green] [dim](Expires: NEVER)[/dim]")

    except Exception as e:
        console.print(f"[bold red]✗ Error querying accounts:[/bold red] {e}")
        sys.exit(1)

    # 3. Save to .env
    console.print("\n[dim]3/3 Configuration Setup...[/dim]")
    should_save = Confirm.ask(f"[bold cyan]Automatically save credentials to .env?[/bold cyan]", default=True)

    if should_save:
        env_path = Path(".env")
        env_content = ""
        if env_path.exists():
            env_content = env_path.read_text(encoding="utf-8")

        # Update or set META_PAGE_ID
        if "META_PAGE_ID=" in env_content:
            env_content = re.sub(r"META_PAGE_ID=.*", f"META_PAGE_ID={target_id}", env_content)
        else:
            env_content += f"\nMETA_PAGE_ID={target_id}"

        # Update or set META_PAGE_ACCESS_TOKEN
        if "META_PAGE_ACCESS_TOKEN=" in env_content:
            env_content = re.sub(r"META_PAGE_ACCESS_TOKEN=.*", f"META_PAGE_ACCESS_TOKEN={permanent_page_token}", env_content)
        else:
            env_content += f"\nMETA_PAGE_ACCESS_TOKEN={permanent_page_token}"

        # Ensure version and delay are present
        if "META_GRAPH_VERSION=" not in env_content:
            env_content += f"\nMETA_GRAPH_VERSION={GRAPH_VERSION}"
        if "META_REQUEST_DELAY=" not in env_content:
            env_content += "\nMETA_REQUEST_DELAY=2.5"

        env_path.write_text(env_content.strip() + "\n", encoding="utf-8")
        console.print(f"[bold green]✓ Successfully written to .env![/bold green]")
        console.print(f"  [cyan]META_PAGE_ID[/cyan] = {target_id}")
        console.print(f"  [cyan]META_PAGE_ACCESS_TOKEN[/cyan] = {permanent_page_token[:15]}...{permanent_page_token[-6:]}")

        console.print("\n[bold]Running verification with 'lazymeta doctor'...[/bold]")
        try:
            from lazymeta.config import Config
            from lazymeta.api import MetaClient
            cfg = Config.from_env()
            client = MetaClient(cfg)
            info = client.verify_credentials()
            console.print(Panel(
                f"[bold green]🎉 All Done! Everything is verified.[/bold green]\n\n"
                f"Page Name: [bold]{info['page_name']}[/bold]\n"
                f"Page ID: [bold]{info['page_id']}[/bold]\n"
                f"Publishing Permissions: [bold green]Active[/bold green]\n"
                f"Expiration: [bold green]NEVER EXPIRES[/bold green]\n\n"
                f"You can now run [bold cyan]python run.py studio[/bold cyan] to start scheduling!",
                title="[bold green]Success[/bold green]",
                border_style="green"
            ))
        except Exception as e:
            console.print(f"[yellow]Note: Saved to .env, but check returned: {e}[/yellow]")
    else:
        console.print("\n[bold]Manual Configuration Details:[/bold]")
        console.print(f"META_PAGE_ID={target_id}")
        console.print(f"META_PAGE_ACCESS_TOKEN={permanent_page_token}")


if __name__ == "__main__":
    get_token_flow()
