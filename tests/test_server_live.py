import threading
import time
import urllib.request
import json
from pathlib import Path
import pytest
from lazymeta.studio.server import start_studio_server

def test_live_server(tmp_path):
    port = 5891
    t = threading.Thread(
        target=start_studio_server,
        kwargs={"port": port, "initial_folder": Path("campaigns/daily_cat_blogs")},
        daemon=True
    )
    t.start()
    time.sleep(0.5)

    # 1. GET /
    res = urllib.request.urlopen(f"http://127.0.0.1:{port}/")
    assert res.status == 200
    html = res.read().decode("utf-8")
    assert "LazyMeta Studio" in html

    # 2. GET /api/campaigns
    res = urllib.request.urlopen(f"http://127.0.0.1:{port}/api/campaigns")
    assert res.status == 200
    camps = json.loads(res.read().decode("utf-8"))
    assert "campaigns" in camps

    # 3. GET /api/campaign
    res = urllib.request.urlopen(f"http://127.0.0.1:{port}/api/campaign")
    assert res.status == 200
    camp = json.loads(res.read().decode("utf-8"))
    assert camp["folder_name"] == "daily_cat_blogs"
    assert camp["total_posts"] == 9
    assert len(camp["posts"]) == 9
