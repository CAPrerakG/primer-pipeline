"""Pull OHLCV history from TradingView's chart websocket (anonymous session)."""
import json, random, re, string, sys, time
import websocket

WS = "wss://data.tradingview.com/socket.io/websocket?from=chart%2F&type=chart"
HDR = ["Origin: https://www.tradingview.com",
       "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)"]


def _rid(prefix):
    return prefix + "".join(random.choice(string.ascii_lowercase) for _ in range(12))


def _frame(msg):
    return f"~m~{len(msg)}~m~{msg}"


def _send(ws, func, args):
    ws.send(_frame(json.dumps({"m": func, "p": args}, separators=(",", ":"))))


def fetch(symbol, interval="1W", n_bars=600, timeout=45, token="unauthorized_user_token"):
    ws = websocket.create_connection(WS, header=HDR, timeout=15)
    cs, qs = _rid("cs_"), _rid("qs_")
    _send(ws, "set_auth_token", [token])
    _send(ws, "chart_create_session", [cs, ""])
    _send(ws, "quote_create_session", [qs])
    _send(ws, "resolve_symbol", [cs, "sym_1",
          '={"adjustment":"splits","symbol":"%s"}' % symbol])
    _send(ws, "create_series", [cs, "s1", "s1", "sym_1", interval, n_bars, ""])

    bars, meta, err = {}, {}, None
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            raw = ws.recv()
        except Exception:
            break
        if not raw:
            continue
        for part in re.findall(r"~m~\d+~m~(.+?)(?=~m~\d+~m~|$)", raw):
            if part.startswith("~h~"):                       # heartbeat
                ws.send(_frame(part))
                continue
            try:
                msg = json.loads(part)
            except Exception:
                continue
            m = msg.get("m")
            if m in ("critical_error", "protocol_error", "symbol_error", "series_error"):
                err = msg
                deadline = 0
                break
            if m == "symbol_resolved":
                meta = msg["p"][2] if len(msg["p"]) > 2 else {}
            if m in ("timescale_update", "du"):
                blk = msg["p"][1].get("s1", {})
                for pt in blk.get("s", []):
                    v = pt["v"]
                    bars[v[0]] = v
            if m == "series_completed":
                deadline = min(deadline, time.time() + 3)     # brief drain
    ws.close()
    if err:
        raise RuntimeError(f"{symbol}: {err}")
    rows = [bars[k] for k in sorted(bars)]
    return rows, meta


if __name__ == "__main__":
    sym = sys.argv[1]
    itv = sys.argv[2] if len(sys.argv) > 2 else "1W"
    rows, meta = fetch(sym, itv)
    import datetime as dt
    print(f"{sym}  bars={len(rows)}  currency={meta.get('currency_code')} "
          f"desc={meta.get('description')} type={meta.get('type')} tz={meta.get('timezone')}")
    for r in rows[:3] + rows[-3:]:
        print(dt.datetime.utcfromtimestamp(r[0]).strftime("%Y-%m-%d"),
              [round(x, 4) if isinstance(x, float) else x for x in r[1:]])
