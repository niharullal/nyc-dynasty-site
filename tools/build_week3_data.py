"""Generate week3-data.js: full newsletter-style data for the Week 3 preview.

Re-run any time lineups change:  python tools/build_week3_data.py
Then bump the ?v= on week3-data.js in index.html and push.

Data sources (all public Sleeper endpoints, no auth):
- league / users / rosters / matchups: current submitted starters + records
- projections: per-player projected stats, scored with THIS league's settings
- scores: game start times, for kickoff-window buckets
- league history chain: real head-to-head, with old-account aliases applied

Win odds use the same model as the commissioner's newsletter: P(win) =
Phi(projection_gap / 25.4), reverse-engineered from the Week 2 edition
(all six published win percentages fit sigma = 25.4 within 0.1%).
"""
import json
import math
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

LEAGUE_ID = "1312585067658223616"
BASE = "https://api.sleeper.app"
SIGMA = 25.4
WEEK = 3

NAME = {"adv1996": "Advaith", "nigeluno02": "Nihar", "Develeper": "Dev",
        "alanadams": "Alan", "chutneyman": "Varun", "swagrawal": "Manas",
        "AchalK": "Achal", "VS96": "Vaibhav", "taylorjgardner1996": "Taylor",
        "Dbanda23": "Dhiraj", "sohamdeval": "Soham", "shiamak": "Shiamak"}
# Managers who used different Sleeper accounts in earlier seasons
# (identities verified against scores printed in the commissioner's newsletters).
ALIAS = {"1stInLastOut": "Vaibhav", "VaibhavS96": "Vaibhav",
         "FalconsAlterego": "Achal", "DhirajBanda": "Dhiraj"}


def get(path):
    with urllib.request.urlopen(BASE + path) as r:
        return json.load(r)


def owner_name(display_name):
    return NAME.get(display_name, ALIAS.get(display_name, display_name))


def score_points(scoring, stats):
    return round(sum(scoring[k] * v for k, v in stats.items()
                     if k in scoring and scoring[k]), 2)


def win_pct(diff):
    return round(100 * 0.5 * (1 + math.erf(diff / (SIGMA * math.sqrt(2)))), 1)


ET = timezone(timedelta(hours=-4))  # EDT; fine for September-October


def window_label(start_ms):
    dt = datetime.fromtimestamp(start_ms / 1000, tz=ET)
    wd, hr = dt.weekday(), dt.hour  # Mon=0 ... Sun=6
    if wd == 3: return "THU"
    if wd == 0: return "MON"
    if wd == 6:
        if hr < 15: return "SUN EARLY"
        if hr < 19: return "SUN PM"
        return "SUN NIGHT"
    return dt.strftime("%a").upper()


WINDOWS = ["THU", "SUN EARLY", "SUN PM", "SUN NIGHT", "MON"]

print("fetching league / users / rosters / matchups / projections / scores ...")
league = get(f"/v1/league/{LEAGUE_ID}")
scoring = league["scoring_settings"]
slots = [p for p in league["roster_positions"] if p != "BN"]
users = {u["user_id"]: u for u in get(f"/v1/league/{LEAGUE_ID}/users")}
rosters = get(f"/v1/league/{LEAGUE_ID}/rosters")
matchups = get(f"/v1/league/{LEAGUE_ID}/matchups/{WEEK}")

pos_q = "&".join(f"position[]={p}" for p in
                 ["QB", "RB", "WR", "TE", "K", "DL", "LB", "DB"])
proj = {p["player_id"]: p for p in
        get(f"/projections/nfl/{league['season']}/{WEEK}?season_type=regular&{pos_q}&order_by=pts_ppr")}
games = get(f"/scores/nfl/regular/{league['season']}/{WEEK}")
game_start = {g["game_id"]: g["start_time"] for g in games}
game_home = {g["game_id"]: (g.get("metadata") or {}).get("home_team") for g in games}

roster_info = {}
for r in rosters:
    u = users.get(r["owner_id"]) or {}
    s = r.get("settings", {})
    roster_info[r["roster_id"]] = {
        "owner": owner_name(u.get("display_name", "?")),
        "team": (u.get("metadata") or {}).get("team_name") or u.get("display_name", "?"),
        "record": f"{s.get('wins', 0)}-{s.get('losses', 0)}"
                  + (f"-{s.get('ties', 0)}" if s.get("ties") else ""),
        "wins": s.get("wins", 0), "losses": s.get("losses", 0),
        "avatar": f"https://sleepercdn.com/avatars/thumbs/{u['avatar']}" if u.get("avatar") else "",
    }

print("counting 2026 season meetings per pairing ...")
season_meetings = {}
owner_by_rid = {rid: v["owner"] for rid, v in roster_info.items()}
for wk in range(1, (league["settings"].get("playoff_week_start") or 15)):
    pr = {}
    for m in get(f"/v1/league/{LEAGUE_ID}/matchups/{wk}"):
        if m.get("matchup_id") is not None:
            pr.setdefault(m["matchup_id"], []).append(m["roster_id"])
    for ids in pr.values():
        if len(ids) == 2:
            key = frozenset(owner_by_rid[i] for i in ids)
            season_meetings[key] = season_meetings.get(key, 0) + 1

print("walking league history chain for head-to-head ...")
history = []
lid = LEAGUE_ID
while lid:
    lg = get(f"/v1/league/{lid}")
    season = lg["season"]
    pws = lg["settings"].get("playoff_week_start") or 15
    us = {u["user_id"]: u for u in get(f"/v1/league/{lid}/users")}
    ow = {r["roster_id"]: owner_name((us.get(r["owner_id"]) or {}).get("display_name", "?"))
          for r in get(f"/v1/league/{lid}/rosters")}
    last_leg = min(lg["settings"].get("last_scored_leg") or 0, 17)
    for wk in range(1, last_leg + 1):
        pairs = {}
        for m in get(f"/v1/league/{lid}/matchups/{wk}"):
            if m.get("matchup_id") is not None:
                pairs.setdefault(m["matchup_id"], []).append(m)
        for pr in pairs.values():
            if len(pr) == 2:
                a, b = pr
                history.append({"season": season, "wk": wk,
                                "bracket": "Regular" if wk < pws else "Postseason",
                                "a": ow[a["roster_id"]], "pa": a.get("points") or 0,
                                "b": ow[b["roster_id"]], "pb": b.get("points") or 0})
    lid = lg.get("previous_league_id")
print(f"  {len(history)} historical matchups")


def player_row(pid, slot):
    pr = proj.get(pid)
    if not pr:
        return {"slot": slot, "name": f"Unknown ({pid})", "team": "", "opp": "",
                "proj": 0.0, "injury": "", "window": "", "id": pid}
    pl = pr.get("player") or {}
    inj = (pl.get("injury_status") or "").strip()
    inj_tag = {"Questionable": "Q", "Doubtful": "D", "Out": "OUT",
               "IR": "OUT", "PUP": "OUT", "Sus": "OUT"}.get(inj, "")
    start = game_start.get(pr.get("game_id"))
    home = game_home.get(pr.get("game_id"))
    return {"slot": slot, "at": bool(home and pr.get("team") != home),
            "name": f"{pl.get('first_name', '')} {pl.get('last_name', '')}".strip(),
            "team": pr.get("team") or "", "opp": pr.get("opponent") or "BYE",
            "proj": score_points(scoring, pr.get("stats") or {}),
            "injury": inj_tag,
            "window": window_label(start) if start else "", "id": pid}


def side_data(m):
    info = roster_info[m["roster_id"]]
    lineup = [player_row(pid, slots[i]) for i, pid in enumerate(m["starters"])]
    total = round(sum(p["proj"] for p in lineup), 2)
    swings = {w: {"pts": 0.0, "n": 0} for w in WINDOWS}
    for p in lineup:
        if p["window"] in swings:
            swings[p["window"]]["pts"] = round(swings[p["window"]]["pts"] + p["proj"], 2)
            swings[p["window"]]["n"] += 1
    return {**info, "lineup": lineup, "total": total,
            "swings": [swings[w] for w in WINDOWS]}


def bullets(own, opp):
    out = []
    skill = sorted((p for p in own["lineup"] if p["slot"] not in ("DL", "LB", "DB", "IDP_FLEX", "K")),
                   key=lambda p: -p["proj"])[:3]
    out.append(", ".join(p["name"] for p in skill[:-1]) + f" and {skill[-1]['name']} "
               f"combine for {round(sum(p['proj'] for p in skill), 2)} projected points — "
               f"{own['owner']}'s core of this lineup.")
    edges = [(o["proj"] - t["proj"], o, t) for o, t in zip(own["lineup"], opp["lineup"])]
    diff, o, t = max(edges, key=lambda e: e[0])
    if diff > 0:
        out.append(f"{o['name']} projects {round(diff, 2)} points ahead of {t['name']} "
                   f"at {o['slot']} — the biggest single-slot edge in this matchup.")
    flagged = [p for p in opp["lineup"] if p["injury"]]
    if flagged:
        f = flagged[0]
        out.append(f"{opp['owner']} lists {f['name']} ({f['injury']}) in the supplied lineup. "
                   f"An absence there changes the math before kickoff.")
    else:
        late = [p for p in own["lineup"] if p["window"] in ("SUN NIGHT", "MON")]
        if late:
            out.append(f"{own['owner']} keeps {len(late)} starter{'s' if len(late) > 1 else ''} "
                       f"alive into the late windows — the final answer comes after "
                       f"{opp['owner']}'s lineup finishes.")
    return out[:3]


data = {"week": WEEK, "sigma": SIGMA,
        "generatedAt": datetime.now(tz=ET).strftime("%b %d, %Y · %I:%M %p ET"),
        "matchups": []}

pairs = {}
for m in matchups:
    if m.get("matchup_id") is not None:
        pairs.setdefault(m["matchup_id"], []).append(m)

# Keep the same card order as the light preview in weeks.js
ORDER = ["Advaith", "Dev", "Varun", "Achal", "Taylor", "Soham"]
built = {}
for mid, (ma, mb) in pairs.items():
    A, B = side_data(ma), side_data(mb)
    if B["owner"] in ORDER and A["owner"] not in ORDER:
        A, B = B, A
    diff = A["total"] - B["total"]
    fav, dog = (A, B) if diff >= 0 else (B, A)
    fav_win = win_pct(abs(diff))
    h2h = [g for g in history
           if {g["a"], g["b"]} == {A["owner"], B["owner"]} and g["season"] != league["season"]]
    h2h_rows = []
    a_wins = b_wins = 0
    for g in sorted(h2h, key=lambda g: (g["season"], g["wk"])):
        pa, pb = (g["pa"], g["pb"]) if g["a"] == A["owner"] else (g["pb"], g["pa"])
        winner = A["owner"] if pa > pb else B["owner"]
        a_wins += pa > pb; b_wins += pb > pa
        h2h_rows.append({"season": g["season"], "wk": g["wk"], "bracket": g["bracket"],
                         "homePts": round(pa, 2), "awayPts": round(pb, 2),
                         "winner": winner, "margin": round(abs(pa - pb), 2)})
    # Newsletter-style series line with Reg./Post. split, from leader's perspective
    def wins_in(bracket, who):
        return sum(1 for g in h2h if g["bracket"] == bracket
                   and ((g["a"] == who and g["pa"] > g["pb"]) or (g["b"] == who and g["pb"] > g["pa"])))
    reg_a, post_a = wins_in("Regular", A["owner"]), wins_in("Postseason", A["owner"])
    reg_b = sum(1 for g in h2h if g["bracket"] == "Regular") - reg_a
    post_b = sum(1 for g in h2h if g["bracket"] == "Postseason") - post_a
    if a_wins >= b_wins and a_wins > 0 and a_wins != b_wins:
        series_full = (f"{A['owner']} leads {B['owner']} {a_wins}–{b_wins} "
                       f"(Reg. {reg_a}–{reg_b}; Post. {post_a}–{post_b})")
        series_cls = "home"
    elif b_wins > a_wins:
        series_full = (f"{B['owner']} leads {A['owner']} {b_wins}–{a_wins} "
                       f"(Reg. {reg_b}–{reg_a}; Post. {post_b}–{post_a})")
        series_cls = "away"
    else:
        series_full = (f"Series tied {a_wins}–{b_wins} "
                       f"(Reg. {reg_a}–{reg_b}; Post. {post_a}–{post_b})")
        series_cls = "even"

    meets = season_meetings.get(frozenset([A["owner"], B["owner"]]), 0)
    series_leader = A["owner"] if a_wins > b_wins else B["owner"] if b_wins > a_wins else None

    # Left tag: marquee rivalry (storied series, single meeting this season) or meeting count
    if meets == 1 and len(h2h) >= 5:
        meet_tag, marquee = "MARQUEE RIVALRY", True
    elif meets == 2:
        meet_tag, marquee = "TWO MEETINGS THIS SEASON", False
    else:
        meet_tag, marquee = ("ONE MEETING THIS SEASON" if meets == 1 else ""), False

    # Badge, data-derived, newsletter vocabulary
    out_flag = [p for p in A["lineup"] + B["lineup"] if p["injury"] == "OUT"]
    if abs(diff) < 5:
        badge = "RAZOR THIN"
    elif fav_win >= 90:
        badge = "BLOWOUT POTENTIAL"
    elif out_flag:
        badge = "LINEUP WATCH"
    elif series_leader and series_leader == dog["owner"]:
        badge = "FAVORITE'S EDGE"
    else:
        badge = ""

    # One-line commentary in the newsletter's cadence
    def top_skill(side, n=2):
        sk = [p for p in side["lineup"] if p["slot"] not in ("DL", "LB", "DB", "IDP_FLEX", "K")]
        return sorted(sk, key=lambda p: -p["proj"])[:n]
    def last_name(full):
        return full.split(" ", 1)[1] if " " in full else full
    if A["record"] == B["record"] and A["losses"] == 0 and A["wins"] > 0:
        hook = f"Someone leaves {A['wins'] + 1}–0."
    elif A["record"] == B["record"] and A["wins"] == 0 and A["losses"] > 0:
        hook = "Someone gets their first win."
    elif series_leader and min(a_wins, b_wins) == 0 and max(a_wins, b_wins) >= 3:
        hook = f"{series_leader} has never lost this series."
    elif series_leader:
        hook = f"{series_leader} leads {max(a_wins, b_wins)}–{min(a_wins, b_wins)} all-time."
    else:
        hook = f"The series is tied {a_wins}–{b_wins}."
    ft, dt = top_skill(fav), top_skill(dog, 1)[0]
    one_liner = (f"{hook} {fav['owner']} brings the current edge, led by "
                 f"{last_name(ft[0]['name'])} and {last_name(ft[1]['name'])}; "
                 f"{dog['owner']} answers with {dt['name']} at {dt['proj']:.2f}.")

    heroes = sorted(A["lineup"], key=lambda p: -p["proj"])[:3] + \
             sorted(B["lineup"], key=lambda p: -p["proj"])[:3]
    built[A["owner"]] = {
        "marquee": marquee,
        "home": A["owner"], "homeTeam": A["team"], "homeRecord": A["record"],
        "away": B["owner"], "awayTeam": B["team"], "awayRecord": B["record"],
        "homeProj": A["total"], "awayProj": B["total"],
        "homeWin": win_pct(diff), "awayWin": win_pct(-diff),
        "seriesLine": series_full, "seriesCls": series_cls,
        "badge": badge, "meetTag": meet_tag, "oneLiner": one_liner,
        "homeAvatar": A["avatar"], "awayAvatar": B["avatar"],
        "heroes": [{"id": p["id"], "name": p["name"], "team": p["team"]} for p in heroes],
        "swingHome": A["swings"], "swingAway": B["swings"], "windows": WINDOWS,
        "h2h": h2h_rows,
        "homeBullets": bullets(A, B), "awayBullets": bullets(B, A),
        "homeLineup": A["lineup"], "awayLineup": B["lineup"],
    }
data["matchups"] = [built[o] for o in ORDER]

out = "// Generated by tools/build_week3_data.py — do not edit by hand.\n"
out += "const WEEK3_DATA = " + json.dumps(data, indent=1) + ";\n"
import os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(root, "week3-data.js"), "w", encoding="utf-8") as f:
    f.write(out)

for m in data["matchups"]:
    print(f"{m['home']} {m['homeProj']} ({m['homeWin']}%) vs "
          f"{m['awayProj']} ({m['awayWin']}%) {m['away']}  | {m['seriesLine']} | h2h {len(m['h2h'])}")
missing = [p["name"] for m in data["matchups"] for p in m["homeLineup"] + m["awayLineup"]
           if p["name"].startswith("Unknown")]
print("missing projections:", missing if missing else "none")
print("wrote week3-data.js")
