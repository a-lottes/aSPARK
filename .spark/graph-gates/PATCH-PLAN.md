# Patch-Plan: `graph-gates` — aspark-graph als optionaler Accelerant in die Gates

**Stand:** 2026-07-25 · **Repo:** `aSPARK` (Core-Plugin, v0.3.1) · **Status:** Vorschlag, nicht freigegeben
**Herkunft:** Antwort auf das Architektur-Review — Sofortmaßnahme 1 von 6

> **Wie dieses Dokument zu benutzen ist.** Es ist ein *Brief*, kein `plan.md`. Es existiert kein
> freigegebener `spec.md`, also wäre ein `plan.md` hier ein Gate-Verstoß gegen die eigene Methode.
> **Empfohlen:** `/story-time` mit diesem Dokument als Vorlage füttern und den Loop regulär laufen lassen
> (Dogfooding — Core sollte an sich selbst glauben). **Alternativ:** direkt umsetzen, dann aber den
> übersprungenen Loop im Commit benennen.

---

## 1. Das Problem, in einem Satz

`grep -riE "aspark-graph|aspark-policy"` über `skills/`, `agents/`, `templates/`, `lenses/`, `README.md`
liefert **null Treffer**. Die Gate-Anleitung für `aspark-graph` existiert fertig ausformuliert — aber im
falschen Repo: [`aSPARK-graph/docs/aspark-integration.md`](../../../aSPARK-graph/docs/aspark-integration.md),
als Copy-Paste-Block, den jedes Projekt einzeln in sein `CLAUDE.md` schaufeln muss.

`gate_health`, `impact`, `story_trace` und `staleness` sind in `aspark-graph` v0.5.0 fertig und getestet.
Die Verdrahtung ist keine Feature-Arbeit, sondern das Einsammeln von etwas, das schon gebaut ist.

## 2. Ziel / Nicht-Ziel

**Ziel.** Die Ceremony-Skills bieten den Graph *von sich aus* an, wenn er im Zielprojekt verfügbar ist —
ohne dass ein Projekt Copy-Paste-Blöcke pflegen muss.

**Nicht-Ziel — hart:**
- **Keine Abhängigkeit.** Core ist ein veröffentlichtes Marketplace-Plugin für beliebige Projekte;
  `aspark-graph` ist install-from-source und in fast keinem davon vorhanden. Ohne Graph muss sich jedes
  Gate **exakt wie heute** verhalten — kein Fehler, kein Hinweis, keine Erwähnung.
- **Kein Gate blockiert** auf Verfügbarkeit, Frische oder Nicht-Leere einer Antwort.
- **Kein Ersatz für Lesen.** Ein Graph-Treffer ist Scoping-Input, kein Urteil.
- Kein Vendoring des Graph-Codes, kein Installer, kein Auto-Build hinter dem Rücken des Nutzers.

## 3. Architekturentscheidung

**Kontext.** Core hat bereits genau dieses Muster für optionales, situatives Wissen: **Lenses.** Ein Lens
ist eine Datei, deren Pfad das Skill an seinen Agent übergibt, wenn die Situation es verlangt; der Agent
liest seine Phasen-Scheibe. Kein neuer Agent, keine neue Ceremony, keine Skill-Umschreibung.

**Entscheidung.** Ein Geschwister-Verzeichnis **`tools/`** neben `lenses/`, mit identischer Mechanik:
Datei existiert → Skill erkennt Verfügbarkeit → übergibt den Pfad an seinen Agent → Agent liest seine
Scheibe. Erstes und einziges Mitglied: `tools/aspark-graph.md`.

**Verworfene Alternativen:**

| Alternative | Warum verworfen |
|---|---|
| Als Lens umsetzen (`lenses/aspark-graph.md`) | Ein Lens ist eine *Concern-Checkliste*, aktiviert durch das Projektprofil in der Constitution. Der Graph ist eine *Werkzeug-Fähigkeit*, aktiviert durch Installationszustand. Den Lens-Vertrag dafür zu verbiegen (`applies-to`/`triggers`/`phases` passen alle nicht) würde beide Konzepte unscharf machen. |
| Anleitung direkt in jedes SKILL.md schreiben | Vervierfacht denselben Text über peer-review, demo-day, sprint-plan, go-live und driftet garantiert auseinander. Lenses lösen genau dieses Problem über Pfad-Übergabe. |
| Copy-Paste-Blöcke wie heute lassen | Das *ist* der Befund. Verlagert Integrationsarbeit in jedes Zielprojekt und veraltet still, wenn sich die Query-Oberfläche ändert. |
| Graph zur harten Abhängigkeit machen | Bricht Core für jedes Projekt ohne Graph — also praktisch alle. Widerspricht dem Non-Goals-Prinzip des Handbuchs. |

**Konsequenzen.** Leichter: jedes weitere aSPARK-Werkzeug ist eine Datei plus eine Zeile pro Skill.
Schwerer: Core kennt jetzt einen Namen aus einem anderen Repo — die Query-Oberfläche wird zum Vertrag
(§4).

## 4. Vertrag mit `aspark-graph` (normativ, verifiziert gegen v0.5.0)

Vollständige Fassung: `~/aSPARK Doku/REVIEW-RESPONSE.md` §5. Was diese Aufgabe braucht:

**CLI und MCP-Tools tragen identische Namen und Parameter.** Ausgabe ist JSON auf stdout. Ist der Graph
nicht gebaut: Meldung auf stderr, **Exit 1**.

| Aufruf | Rückgabe |
|---|---|
| `aspark-graph query staleness --repo .` | `{"stale": bool, "files_checked": n, …}` |
| `aspark-graph query impact <file…>` oder `--diff <range>` | Blast-Radius; Fehlargumente → `{"found": false, "reason": "bad_args"}` |
| `aspark-graph query story_trace <US-n> --feature <feature>` | Story → ACs → Tasks → Code → QA |
| `aspark-graph query gate_health <feature>` | `{orphan_tasks, unverified_acs, open_findings}` oder `{"found": false, "reason": "not_found"}` |

Confidence-Stufen in Ergebnissen: `inferred` < `extracted` < `declared`.

**Erkennung (Reihenfolge bindend):**
1. Sind MCP-Tools mit den Namen `staleness` / `impact` / `story_trace` / `gate_health` in der Session
   vorhanden → diese benutzen.
2. Sonst: `command -v aspark-graph` **und** `test -d .aspark-graph` → CLI benutzen.
3. CLI vorhanden, aber `.aspark-graph/` fehlt → **einmalig** einen Satz sagen („aspark-graph ist
   installiert, aber für dieses Repo nicht gebaut — `aspark-graph build .`"), dann normal ohne Graph
   weitermachen. Nicht wiederholen, nicht nachfragen, nicht selbst bauen.
4. Nichts davon → schweigen und exakt wie heute arbeiten.

**Gegenrichtung — Template-Vertrag.** `aspark-graph` parst die Core-Templates und wirft
`TemplateDriftError`, wenn sie nicht passen. Beim Bearbeiten von `templates/` gilt:

- **Nicht umbenennen, nicht entfernen:** in `plan.md` die Spalten `#`, `Task`, `Story`, `Status`,
  `Definition of Done`; das Heading-Wort `Task Breakdown`; die Task-IDs im Muster `^T\d+$`.
- Ebenso in `spec.md` (`### US-n (…): …`, `- [ ] AC-n.m: …`), `review-report.md` (`## … Findings`,
  `^F\d+$`), `qa-report.md` (Spalten `Spec ID` + `Result` — die Gegenseite erwartet weiterhin `AC` und
  wirft daher heute `TemplateDriftError`, ein Defekt im graph-Repo, `artifacts.py:234`),
  `release-notes.md` (Kopfzeilen `Status`, `Version`).
- **Spalten anfügen ist erlaubt** (der Parser matcht per Substring und toleriert Extra-Spalten).

## 5. Task-Breakdown

DoD-Zellen tragen `files:`-Notizen — dieser Plan dogfoodet die Änderung, die T5 einführt.

| # | Task | Covers | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|
| T1 | `tools/README.md` anlegen: was ein Tool-File ist, wie es aktiviert wird, wie man ein weiteres hinzufügt. Struktur an `lenses/README.md` anlehnen, aber die Abgrenzung Tool↔Lens explizit benennen | Vertrag | – | `todo` | Datei erklärt Aktivierung über Installationszustand (nicht Projektprofil) und enthält die Abgrenzung aus §3. `files: tools/README.md` |
| T2 | `tools/aspark-graph.md` schreiben: Frontmatter (`name`, `phases`, `detect`), Erkennungsblock aus §4, dann eine Scheibe je Phase — **Plan** (`impact` für „Affected Components"), **Review** (`staleness` → `impact` → `story_trace` → `gate_health`), **QA** (`story_trace`, `gate_health` zum Scoping des Testplans) | Vertrag | T1 | `todo` | Jede Phasen-Scheibe nennt Aufruf, Rückgabeform und Fallback. Die drei Interpretationsregeln aus `aSPARK-graph/docs/aspark-integration.md` (Karte kein Zertifikat · Confidence-Stufen · leeres Ergebnis = zurückfallen) sind inhaltlich übernommen. `files: tools/aspark-graph.md` |
| T3 | `skills/peer-review/SKILL.md`: Erkennung als Teilschritt in Schritt 1 („Check the gate"), Pfad-Übergabe in Schritt 2 analog zur Lens-Übergabe | Wiring | T2 | `todo` | Bei Nicht-Verfügbarkeit ist der Ablauf unverändert. `files: skills/peer-review/SKILL.md` |
| T4 | Dasselbe in `skills/demo-day/SKILL.md` (Schritt 1 „Check the gates and the gear" / Schritt 2) und `skills/sprint-plan/SKILL.md` (Schritt 1 / Schritt 2) | Wiring | T2 | `todo` | Graph-Nichtverfügbarkeit ändert in beiden Skills nichts. Browser-Tooling in demo-day bleibt **harte** Voraussetzung — der Graph ersetzt es nicht. `files: skills/demo-day/SKILL.md, skills/sprint-plan/SKILL.md` |
| T5 | **`files:`-Notizen einführen.** `templates/plan.md`: Kommentar über der Task-Tabelle um einen Satz zu `files:` in der DoD-Zelle erweitern. `agents/engineering-manager.md`: in „Cut the tasks" (Schritt 4) die Anweisung ergänzen, jede DoD-Zelle mit `files: <pfad>[, …]` zu schließen, wo die berührten Dateien bekannt sind | Determinismus | – | `todo` | Format entspricht §4/C1 exakt. Tabellenspalten sind **unverändert**. Ein damit erzeugter Plan liefert `implements`-Kanten mit Confidence `declared` statt `inferred`. `files: templates/plan.md, agents/engineering-manager.md` |
| T6 | `agents/reviewer.md`: Abschnitt „Wenn der Aufrufer ein Tool-File übergibt" nach `## How You Work` Schritt 2 („Get the diff"). `agents/qa-tester.md`: analog beim Aufbau des Testplans. `agents/engineering-manager.md`: `impact` für „Affected Components" | Wiring | T2 | `todo` | Jeder Abschnitt sagt ausdrücklich: Graph-Ausgabe ersetzt weder Code-Lesen (Reviewer) noch das Ausführen der Schritte (QA). `files: agents/reviewer.md, agents/qa-tester.md, agents/engineering-manager.md` |
| T7 | `README.md`: kurzer Abschnitt „Optionale Werkzeuge" mit einem Absatz zu `aspark-graph` und Link ins graph-Repo | Doku | T2 | `todo` | Beschreibt es als optional und install-from-source. Keine PyPI-Behauptung — das Paket ist nicht veröffentlicht. `files: README.md` |
| T8 | Version auf `0.4.0` in `.claude-plugin/plugin.json` | Release | T1–T7 | `todo` | Minor-Bump: neue optionale Fähigkeit, keine Breaking Change. `files: .claude-plugin/plugin.json` |

**Nicht in dieser Aufgabe:** `/go-live` (braucht den `Release`-Knoten aus dem graph-Repo — dort Item G1),
`/increment`, `/charter`, `aspark-policy` (dort noch keine ausführbare Oberfläche), der
Template-Versions-Handshake (koordiniert, Item 11).

## 6. Teststrategie

Kein Unit-Test möglich — das Artefakt ist Prompt-Material. Verifikation ist Dogfooding, in dieser
Reihenfolge:

1. **Negativfall zuerst, und zwar hier.** `aSPARK` selbst hat keinen gebauten Graph. `/peer-review` auf
   den eigenen Diff laufen lassen: der Ablauf muss unverändert sein und `aspark-graph` **nirgends**
   erwähnen. Das ist die wichtigste Prüfung — ein Regressionsrisiko für jedes bestehende Nutzerprojekt.
2. **Positivfall in `~/aSPARK-graph`.** Dort liegen sieben echte `.spark/<feature>/`-Trails, und der Graph
   lässt sich mit `aspark-graph build .` bauen. `/peer-review` laufen lassen: der Report muss `impact`-
   und `story_trace`-Ergebnisse als Scoping-Begründung zitieren — und trotzdem echte Code-Lektüre zeigen.
3. **Stale-Fall.** Eine Quelldatei in `~/aSPARK-graph` ändern, **nicht** neu bauen, `/peer-review`
   wiederholen: `staleness` meldet `stale: true`, das Gate fällt sichtbar auf grep/Read zurück, sagt das
   ausdrücklich, und **läuft durch**.
4. **`files:`-Fall (T5).** `/sprint-plan` für ein kleines Feature laufen lassen, danach
   `aspark-graph build . && aspark-graph query story_trace <US-n> --feature <feature>`: die
   `implements`-Kanten müssen `declared` statt `inferred` tragen.
5. **Kein Template-Drift.** Nach T5: `aspark-graph build .` in `~/aSPARK-graph` muss ohne
   `TemplateDriftError` durchlaufen.

## 7. Risiken

| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| Ein Gate blockiert doch, wenn der Graph fehlt | Bricht Core für praktisch alle Nutzerprojekte | Testschritt 1 ist Pflicht und läuft **zuerst** |
| Agent behandelt Graph-Ausgabe als Urteil und liest den Code nicht mehr | Reviews werden schlechter statt schneller — die Kernqualität von aSPARK | Formulierung „Karte, kein Zertifikat" in Tool-File **und** in jedem Agent-Abschnitt; Testschritt 2 prüft, dass echte Code-Lektüre im Report steht |
| T5 bricht den Graph-Parser | Graph baut für aSPARK-Projekte nicht mehr | Nur Kommentar- und Agent-Text, **keine** Spaltenänderung; Testschritt 5 |
| Query-Oberfläche driftet später im graph-Repo | Skills rufen ins Leere | Vertrag ist in §5 von `REVIEW-RESPONSE.md` normativ festgeschrieben; das graph-Backlog kennt ihn |
| `tools/` bleibt für immer einelementig | Abstraktion ohne Gegenwert | Bewusst akzeptiert: der Aufwand ist eine Datei, und der Alternativpfad (Text in vier Skills duplizieren) ist teurer |

## 8. Fertig, wenn

- [ ] `tools/README.md` und `tools/aspark-graph.md` existieren, Tool↔Lens ist abgegrenzt
- [ ] peer-review, demo-day, sprint-plan erkennen und übergeben; kein Gate blockiert
- [ ] reviewer, qa-tester, engineering-manager haben ihre Scheibe, jeweils mit der Nicht-Ersetzungsregel
- [ ] `templates/plan.md` und der EM-Agent erzeugen `files:`-Notizen; Spalten unverändert
- [ ] Alle fünf Testschritte aus §6 durchgeführt, **Negativfall zuerst**, Ergebnisse notiert
- [ ] `README.md` nennt es optional und install-from-source
- [ ] Plugin-Version `0.4.0`
