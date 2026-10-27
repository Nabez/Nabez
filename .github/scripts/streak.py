"""Streak-Karte fürs Profil, ohne Fremddienst.

Der öffentliche Streak-Dienst cacht serverseitig und schickt max-age=86400 —
die Karte lag paar Beiträge hinter GitHub.
Dieses Skript fragt den Beitragskalender direkt über die GraphQL-API ab
(private Beiträge zählen mit, wenn das Profil sie zeigt) und schreibt ein SVG.

    python3 streak.py <login> <ausgabe.svg>      # Token aus GH_TOKEN
"""
import datetime as dt
import json
import os
import sys
import urllib.request

ABFRAGE = """query($login:String!,$von:DateTime!,$bis:DateTime!){
  user(login:$login){ createdAt
    contributionsCollection(from:$von,to:$bis){ contributionCalendar{
      weeks{ contributionDays{ date contributionCount } } } } } }"""


def graphql(variablen):
    anfrage = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": ABFRAGE, "variables": variablen}).encode(),
        headers={"Authorization": f"bearer {os.environ['GH_TOKEN']}", "User-Agent": "nabez-streak"},
    )
    with urllib.request.urlopen(anfrage, timeout=30) as antwort:
        daten = json.load(antwort)
    if daten.get("errors"):
        raise SystemExit(f"GraphQL: {daten['errors']}")
    return daten["data"]["user"]


def tage(login):
    """Alle Kalendertage seit Kontoanlage: {datum: anzahl}. Je Abfrage höchstens ein Jahr."""
    jetzt = dt.datetime.now(dt.timezone.utc)
    start = dt.datetime.fromisoformat(graphql({"login": login, "von": jetzt.isoformat(), "bis": jetzt.isoformat()})["createdAt"].replace("Z", "+00:00"))
    ergebnis = {}
    von = start
    while von < jetzt:
        bis = min(von + dt.timedelta(days=365), jetzt)
        kalender = graphql({"login": login, "von": von.isoformat(), "bis": bis.isoformat()})
        for woche in kalender["contributionsCollection"]["contributionCalendar"]["weeks"]:
            for tag in woche["contributionDays"]:
                ergebnis[dt.date.fromisoformat(tag["date"])] = tag["contributionCount"]
        von = bis
    return start.date(), ergebnis


def serien(zaehler, heute):
    """Aktuelle und längste Serie als (länge, von, bis). Ein leeres Heute bricht die Serie nicht."""
    laengste = (0, None, None)
    lauf, lauf_start = 0, None
    for tag in sorted(zaehler):
        if tag > heute:
            break
        if zaehler[tag] > 0:
            lauf_start = tag if lauf == 0 else lauf_start
            lauf += 1
            if lauf > laengste[0]:
                laengste = (lauf, lauf_start, tag)
        else:
            lauf = 0
    ende = heute if zaehler.get(heute, 0) > 0 else heute - dt.timedelta(days=1)
    aktuell, tag = 0, ende
    while zaehler.get(tag, 0) > 0:
        aktuell += 1
        tag -= dt.timedelta(days=1)
    return (aktuell, tag + dt.timedelta(days=1), ende), laengste


def zahl(n):
    return f"{n:,}".replace(",", ".")


def datum(d, jahr=False):
    return d.strftime("%d.%m.%Y" if jahr else "%d.%m.") if d else "–"


def svg(gesamt, seit, aktuell, laengste, stand):
    a, a_von, a_bis = aktuell
    l, l_von, l_bis = laengste
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 200" width="520" height="200" role="img" aria-label="{zahl(gesamt)} Beiträge, {a} Tage am Stück, längste Serie {l} Tage">
  <style>
    .z{{font:700 34px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#c9d1d9}}
    .l{{font:400 15px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#818cf8}}
    .lf{{font:700 15px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#818cf8}}
    .d{{font:400 12px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#8b949e}}
    .s{{font:400 9px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#484f58}}
    .ein{{opacity:0;animation:ein .6s ease-out forwards}}.e2{{animation-delay:.2s}}.e3{{animation-delay:.4s}}
    @keyframes ein{{to{{opacity:1}}}}
    @media (prefers-reduced-motion: reduce){{.ein{{animation:none;opacity:1}}}}
  </style>
  <rect width="520" height="200" rx="6" fill="#0d1117"/>
  <line x1="173" y1="38" x2="173" y2="162" stroke="#818cf8" stroke-width="1" opacity=".6"/>
  <line x1="347" y1="38" x2="347" y2="162" stroke="#818cf8" stroke-width="1" opacity=".6"/>
  <g class="ein" text-anchor="middle">
    <text class="z" x="87" y="94">{zahl(gesamt)}</text>
    <text class="l" x="87" y="128">Beiträge gesamt</text>
    <text class="d" x="87" y="152">seit {datum(seit, True)}</text>
  </g>
  <g class="ein e2" text-anchor="middle">
    <circle cx="260" cy="80" r="38" fill="none" stroke="#818cf8" stroke-width="5"/>
    <rect x="245" y="34" width="30" height="16" fill="#0d1117"/>
    <path d="M260 26 C252 34 252 40 256 46 C254 41 258 37 260 34 C262 38 268 41 264 46 C270 40 268 32 260 26 Z" fill="#818cf8"/>
    <text class="z" x="260" y="92">{a}</text>
    <text class="lf" x="260" y="144">Tage am Stück</text>
    <text class="d" x="260" y="166">{datum(a_von)} – {datum(a_bis)}</text>
  </g>
  <g class="ein e3" text-anchor="middle">
    <text class="z" x="433" y="94">{l}</text>
    <text class="l" x="433" y="128">Längste Serie</text>
    <text class="d" x="433" y="152">{datum(l_von)} – {datum(l_bis)}</text>
  </g>
  <text class="s" x="512" y="192" text-anchor="end">Stand {stand}</text>
</svg>
'''


def main():
    login, ziel = sys.argv[1], sys.argv[2]
    heute = dt.datetime.now(dt.timezone.utc).date()
    seit, zaehler = tage(login)
    gesamt = sum(zaehler.values())
    aktuell, laengste = serien(zaehler, heute)
    stand = dt.datetime.now(dt.timezone.utc).strftime("%d.%m.%Y %H:%M UTC")
    os.makedirs(os.path.dirname(ziel) or ".", exist_ok=True)
    with open(ziel, "w", encoding="utf-8") as f:
        f.write(svg(gesamt, seit, aktuell, laengste, stand))
    print(f"{login}: {gesamt} Beiträge, aktuell {aktuell[0]} Tage, längste {laengste[0]} Tage")


if __name__ == "__main__":
    main()
