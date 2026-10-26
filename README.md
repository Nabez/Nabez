<div align="center">
  <img src="./header.svg" width="100%" alt="Nabez – Sales Manager & average Leptos Enjoyer" />
</div>

<br>

Alta, wie geil is dit denn.

Hörma, ich bin Sidney, Vertriebler durch und durch. Und wir hamma hier son XXL-Ding am Laufen, dit glaubste nich.

Jo und ich ham die CRMs alle durch, wa: Pipedrive, HubSpot, Salesforce. Ham alle irgendwie ihre Berechtigung, keene Frage. Aber gut wird da nix, bevor de nich erst 'n Projekt draus machst – Berater hier, externe IT da, Rechnung mit so vielen Nullen. Und am Ende? Mittelmäßig, Alta.

Also ham wa gesagt: machen wa selbst. In Rust. Dit Frontend och. Ja, wirklich – kiek ma unten rein.

Eine Million Zeilen, Leute. XXL-Portion, keene halben Sachen.

**[Sell.ly](https://sellycrm.de) – ein CRM, das kein Projekt ist.**

> **SIG – SaaS ist geil.**

---

```yaml
# ~/.config/nabez/stack.yml

languages:  [Rust, SQL, TypeScript, CSS]
frontend:   [Leptos, WebAssembly]             # average enjoyer
backend:    [Axum, tokio, sqlx, PostgreSQL]
infra:      [Hetzner, Docker, Caddy, GitHub Actions]
ai:         [Ollama]                          # self-hosted, bleibt im Haus
```

---

#### `> wc -l selly/**` · XXL-Portion, keine halben Sachen

```text
1.129.958 Zeilen in 7.290 Dateien

Rust         916.437   5.801 Dateien   ████████████████████████░░░░░░  81 %
CSS           72.579     473 Dateien   ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░   6 %
TypeScript    50.451     337 Dateien   █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   4 %
SQL           24.118     269 Dateien   █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   2 %
──────────────────────────────────────────────────────────────────────
10.453 Tests · 294 E2E-Specs · 261 Migrationen · 45 Crates · 1 Binary
```

#### `> cargo test echte_probleme`

```text
running 7 tests
test kunde_a_sieht_nie_die_daten_von_kunde_b ....... ok
test kein_cent_geht_verloren ....................... ok
test jede_automation_laeuft_genau_einmal ........... ok
test das_audit_log_luegt_nicht ..................... ok
test ki_ohne_datenabfluss .......................... ok
test ui_ohne_javascript_framework .................. ok
test vier_telefonanlagen_ein_stecker ............... ok

test result: ok. 7 passed; 0 failed; 0 ignored
```

<details>
<summary><b>Und wie genau?</b></summary>
<br>

- **Kunde A sieht nie die Daten von Kunde B** – Row-Level-Security mit FORCE auf 210 von 225 Tabellen, dazu Fremdschlüssel über `(tenant_id, id)`. Ein Verweis auf fremde Daten lässt sich physisch nicht einfügen.
- **Kein Cent geht verloren** – Geld ist ein eigener Typ auf `rust_decimal`, in Postgres `NUMERIC(14,2)`. `f64` für Beträge gibt's nicht.
- **Jede Automation läuft genau einmal** – alles in einem Binary, Hintergrund-Jobs inklusive. Laufen zwei Server, entscheidet ein Postgres-Advisory-Lock, wer führt.
- **Das Audit-Log lügt nicht** – jeder Eintrag ist `SHA-256(Vorgänger-Hash ‖ Inhalt)`. Wer nachträglich eine Zeile ändert, bricht die Kette.
- **KI ohne Datenabfluss** – nur Ollama, selbst gehostet. Kein Kundendatensatz geht an OpenAI & Co.
- **UI ohne JavaScript-Framework** – 325.000 Zeilen Leptos, kompiliert zu WebAssembly. Kein React, kein Vue, eine Sprache von der Datenbank bis zum Button.
- **Vier Telefonanlagen, ein Stecker** – sipgate, Twilio, Placetel und 3CX hinter einem Port. Die Adapter bauen nur Daten, gesendet wird an einer Stelle – testbar ohne ein einziges Netzpaket.

</details>

---

#### `> ls Selly-CRM/`

▸ **selly** — das Produkt: Multi-Tenant-CRM, ein Binary, 45 Crates · [sellycrm.de](https://sellycrm.de)

▸ **selly-web** — die Website: statisch, ohne JavaScript, ohne fremde Server

---

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=Nabez&theme=dark&background=0D1117&border=30363D&stroke=818CF8&ring=818CF8&fire=818CF8&currStreakNum=C9D1D9&sideNums=C9D1D9&currStreakLabel=818CF8&sideLabels=818CF8&dates=8B949E&hide_border=true" width="520" alt="Streak" />
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Nabez/Nabez/output/schlange-dunkel.svg" />
    <img src="https://raw.githubusercontent.com/Nabez/Nabez/output/schlange.svg" width="820" alt="Beiträge des letzten Jahres als Schlange" />
  </picture>
</div>

---

<div align="center">

  [sellycrm.de](https://sellycrm.de) · [GitHub](https://github.com/Nabez)

  <img src="https://komarev.com/ghpvc/?username=Nabez&color=6366f1&style=flat-square&label=views" alt="Profilaufrufe" />

</div>
