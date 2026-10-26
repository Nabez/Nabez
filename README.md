<div align="center">
  <img src="./trabbi-film.svg" width="100%" alt="Grand Theft Trabbi: Hamburg – ein Trabant 601 und eine Simson S51 am Hafen. Alta, wie geil ist Dustin! GiG – GeSaast is Geil!" />
</div>

<br>

<div align="center">
  <img src="./header.svg" width="100%" alt="Nabez – Sales Manager & average Leptos Enjoyer" />
</div>

<br>

<div align="center">
  <img src="https://raw.githubusercontent.com/Nabez/Nabez/output/streak.svg" width="520" alt="Beiträge gesamt, Tage am Stück, längste Serie" />
</div>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Nabez/Nabez/output/schlange-dunkel.svg" />
    <img src="https://raw.githubusercontent.com/Nabez/Nabez/output/schlange.svg" width="820" alt="Beiträge des letzten Jahres als Schlange" />
  </picture>
</div>

<br>

**[Selly](https://sellycrm.de) – ein CRM, das kein Projekt ist.**

> **GiG – GeSaast is Geil.**

---

```yaml
# ~/.config/nabez/stack.yml

languages:  [Rust, SQL, TypeScript, CSS]
frontend:   [Leptos, WebAssembly]             # average enjoyer, wa
backend:    [Axum, tokio, sqlx, PostgreSQL]
infra:      [Server in DE, Docker, Caddy, GitHub Actions]
ai:         [Ollama]                          # selbst jehostet, bleibt im Haus
```

---

#### `> wc -l selly/**` · XXL-Portion, keene halben Sachen

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
running 9 tests
test dashboard_tickt_live_ohne_f5 .................. ok
test dashboard_laeuft_aufm_buero_tv ................ ok
test eine_million_kontakte_liste_in_5_ms ........... ok
test so_viele_server_wie_de_willst ................. ok
test prod_umzug_in_46_sekunden ..................... ok
test videocall_ohne_zoom_und_teams ................. ok
test zehn_leute_eine_liste_keiner_ruft_doppelt ..... ok
test push_aufs_iphone_ohne_app_store ............... ok
test kunde_a_sieht_nie_die_daten_von_kunde_b ....... ok

test result: ok. 9 passed; 0 failed; 0 ignored
```

<details>
<summary><b>Wie jetz? Kiek ma, so jeht dit:</b></summary>
<br>

- **Dashboard tickt live, ohne F5** – Hörma: Deal jewonnen, und zack, bei allen springt die Kachel um. Keener drückt F5, keener wartet. Dit läuft per WebSocket, een `tokio::broadcast`-Kanal pro Mandant, wa.
- **Dashboard aufm Büro-TV** – Dashboard an die Wand, Alta, wie inne Kneipe dit Fußballspiel. Im CRM kriegste Adresse und Code, der Fernseher tippt den ein – fertich. Keen Login am Jerät, freijegeben wird im CRM.
- **1 Mio Kontakte, Liste in 5 ms** – Wa ham dit XXL jetestet: 1,05 Millionen Kontakte, 9,76 Millionen Zeilen. Kontaktliste in 4,7 ms, Profil in 1,4 ms, Feeds aus Tabellen mit 2–3 Millionen Zeilen in 1–4 ms. Dit is schneller, als de „Moin“ sagen kannst.
- **So viele Server wie de willst** – Een Binary, und dit startest de so oft de willst. Alle machen Oberfläche und API, die Hintergrund-Jobs fährt aber nur EENER (Postgres-Advisory-Lock). Kippt der um, übernimmt der nächste. Automatisch, keener muss wat drücken.
- **Prod-Umzug in 46 Sekunden** – Neuer Server, Alta: einfrieren, Dump, rüber, einspielen, hochfahren. 46 Sekunden. Zeilen jezählt, Prüfsumme gleich, nix verloren.
- **Videocall ohne Zoom und Teams** – Selly Meet: Jeder Termin hat seinen eigenen Videoraum. Der Kunde kommt per Link rein, ohne Konto, ohne Jedöns, und wartet inne Lobby, bis de ihn reinlässt. WebRTC, eigener TURN-Server.
- **Zehn Leute, eine Liste, keiner ruft doppelt** – Kaltakquise im Team, wa: Wer 'n Kontakt zieht, hat den 10 Minuten für sich alleene (Claim-Lease in Postgres). Keen Lebenszeichen? Dann jeht er zurück inne Liste.
- **Push aufs iPhone, ohne App Store** – Web Push mit VAPID und aes128gcm, allet selbst jebaut. Läuft auf Mac, iPhone (als Home-Bildschirm-App) und sogar auf der Apple Watch, Alta.
- **Kunde A sieht nie die Daten von Kunde B** – Row-Level-Security mit FORCE auf 210 von 225 Tabellen, dazu Fremdschlüssel über `(tenant_id, id)`. Een Verweis auf fremde Daten kriegste physisch nich mal rinjeschrieben. Dit is dicht, Leute.

</details>

---

#### `> ls Selly-CRM/`

▸ **selly** — dit Produkt: Multi-Tenant-CRM, een Binary, 45 Crates · [sellycrm.de](https://sellycrm.de)

▸ **selly-web** — die Website: statisch, keen JavaScript, keene fremden Server

---

<div align="center">

  [sellycrm.de](https://sellycrm.de) · [GitHub](https://github.com/Nabez)

  <img src="https://komarev.com/ghpvc/?username=Nabez&color=6366f1&style=flat-square&label=views" alt="Profilaufrufe" />

</div>
