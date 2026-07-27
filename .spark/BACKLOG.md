# Backlog — aSPARK Core

**Stand:** 2026-07-25 · **Repo-Version:** Plugin `0.3.1` · **Herkunft:** Antwort auf das Architektur-Review
**Master-Dokument:** `~/aSPARK Doku/REVIEW-RESPONSE.md` (enthält die normativen Cross-Repo-Verträge)

> **Für die Session in diesem Repo.** Dieses Backlog ist autonom lesbar — du brauchst die anderen Repos
> nicht geöffnet. Alles, was du über `aspark-graph` und `aspark-policy` wissen musst, steht in §2.
> Reihenfolge ist Abhängigkeitsreihenfolge, nicht Wichtigkeit.
>
> **Achtung: `.spark/` ist in diesem Repo getrackt** (kein `.gitignore`-Eintrag). Was du hier committest,
> wird auf dem Marketplace-Repo **öffentlich**. Präzedenz existiert (`.spark/situational-lenses` ist
> bewusst committed) — entscheide es aber bewusst, nicht versehentlich.

## 1. Wo dieses Repo steht

Core ist das reifste Produkt der Familie: 10 Skills, 7 Agents, 9 Lenses, 6 Templates, vier Releases.
Das Review nennt die Prozessdisziplin „the real, shippable product today, and it is very good". Das ist
richtig.

Der härteste Befund gegen dieses Repo ist kein Qualitätsmangel, sondern eine Lücke:

> `grep -riE "aspark-graph|aspark-policy"` über `skills/`, `agents/`, `templates/`, `lenses/`, `README.md`
> → **null Treffer.**

Core weiß nicht, dass die anderen Produkte existieren. `aspark-graph` v0.5.0 ist fertig, getestet und
liefert genau die Antworten, die die Gates von Hand zusammengreppen — und die Integrationsanleitung ist
fertig geschrieben, liegt aber als Copy-Paste-Block im graph-Repo.

## 2. Was du über die Nachbar-Repos wissen musst

### `aspark-graph` v0.5.0 — Shipped, aber install-from-source

Deterministischer Code- und Artefakt-Wissensgraph. Liest `.spark/`-Artefakte **und** Quellcode
(tree-sitter, 5 Sprachen), persistiert nach `.aspark-graph/`. CLI **und** MCP-Server, identische
Namen/Parameter. **Nicht auf PyPI.**

```
aspark-graph build [path] [--full]
aspark-graph query <name> [--repo PATH] <args…>
```

Queries: `get_node` · `story_trace` · `impact` · `gate_health` · `staleness` · `find_nodes` ·
`get_neighbors` · `shortest_path` — JSON auf stdout; Graph nicht gebaut → stderr + **Exit 1**.

**Bindend für Core:** optional, niemals blockierend. Core ist ein veröffentlichtes Marketplace-Plugin für
beliebige Projekte; in fast keinem ist `aspark-graph` installiert. Fehlt er, verhält sich jedes Gate
**exakt wie heute**.

### `aspark-policy` v0.1.0 — Frühphase, für Core noch nicht anschlussfähig

11 Policy-Packs (YAML + Markdown) und ein JSON-Schema, aber **8 Zeilen Python**: kein Resolver, keine CLI,
kein `[project.scripts]`. Es gibt nichts, was Core aufrufen könnte. **Nichts in diesem Backlog verdrahtet
policy.** Der Anschluss kommt, wenn dort `resolve`/`validate` existiert.

### Der Template-Vertrag — die versteckte Kopplung

`aspark-graph` parst die Templates dieses Repos und wirft `TemplateDriftError`, wenn sie nicht passen.
Es gibt **keinen Versions-Handshake**: die Templates hier tragen keine Versionsmarkierung, während der
Graph `SUPPORTED_TEMPLATE = "aspark/0.1.0"` pinnt. **Jede Template-Änderung hier ist ein stiller Breaking
Change dort.**

Beim Bearbeiten von `templates/` nicht umbenennen und nicht entfernen:

| Template | Geschützt |
|---|---|
| `plan.md` | Heading-Wort `Task Breakdown`; Spalten `#`, `Task`, `Story`, `Status`, `Definition of Done`; Task-IDs `^T\d+$` |
| `spec.md` | `### US-<n> (<moscow>): <title>`; `- [ ] AC-<n>.<m>: <text>` |
| `review-report.md` | Heading-Wort `Findings`; Finding-IDs `^F\d+$` |
| `qa-report.md` | Spalten `Spec ID` und `Result` — die Gegenseite erwartet weiterhin `AC` und wirft daher heute `TemplateDriftError` (Defekt im graph-Repo, `artifacts.py:234`) |
| `release-notes.md` | Kopfzeilen `Status` und `Version` |

**Spalten anfügen ist erlaubt** — der Parser matcht per Substring und toleriert Extra-Spalten.

---

## 3. Features in Abhängigkeitsreihenfolge

### C1 · `graph-gates` — Graph als optionaler Accelerant in die Gates

**Priorität: Sofort.** Größter Hebel bei geringstem Aufwand im gesamten Projekt. Verdrahtet Vorhandenes,
führt kein neues Konzept ein. Enthält auch die `files:`-Notizen (siehe unten), weil beide dieselben
Dateien berühren.

Vollständiger Plan mit Architekturentscheidung, 8 Tasks, Teststrategie und Risiken:
**[`.spark/graph-gates/PATCH-PLAN.md`](graph-gates/PATCH-PLAN.md)** — vor dem Start lesen.

```
/story-time graph-gates — aspark-graph als optionalen Accelerant in die Ceremony-Gates verdrahten.
Der vollständige Brief liegt in .spark/graph-gates/PATCH-PLAN.md und ist verbindlicher Scope:
neues tools/-Verzeichnis analog zu lenses/, Erkennung über Installationszustand, niemals blockierend.
Lies ihn zuerst, dann schreibe die Spec dagegen.
```

**Teil-Highlight — `files:`-Notizen (T5 im Plan).** Der Graph unterstützt *bereits* `files: a.py, b.py`
inline in der Definition-of-Done-Zelle und erzeugt daraus `implements`-Kanten mit Confidence `declared`
statt `inferred`. Es braucht **keine neue Spalte** — nur eine Anweisung an den Engineering Manager. Das ist
der billigste Determinismus-Gewinn im ganzen Projekt und beantwortet die im graph-Repo notierte Tier-1-Idee
„explicit `files:` column (needs an aSPARK PR)" ohne Template-Bruch.

---

### C2 · `handbook-maturity` — Reifegrad-Label pro Kapitel im Handbuch

**Priorität: Sofort.** Betrifft `docs/aSPARK_Enterprise_Architecture_Handbook.docx`.

Der schärfste Vorwurf des Reviews, und er trifft: das Handbuch beschreibt eine Zielplattform, während die
Eingeständnisse mitten in den Kapiteln versteckt sind. Leser verwechseln Ambition mit Lieferumfang.

Die Website macht es schon richtig. Übernimm **wörtlich diese vier Stufen**, keine eigenen Begriffe:

| Stufe | Gilt für |
|---|---|
| **Shipped** | Core, graph |
| **Frühphase / Early dev** | policy |
| **Geplant / Planned** | insights, ci |
| **Zukunft / Future** | memory |

Umfang: sichtbares Label an jedem Kapitel, das eine Fähigkeit beschreibt, plus eine Übersichtstabelle
vorn. Zusätzlich die Dokumentversion zweiteilen — „Zielarchitektur v1.0" vs. „Ausgeliefert: Core 0.3.x,
graph 0.5.x, policy 0.1.x".

```
/story-time handbook-maturity — Reifegrad-Kennzeichnung pro Kapitel im Enterprise Architecture Handbook
(docs/aSPARK_Enterprise_Architecture_Handbook.docx). Vier Stufen wörtlich wie auf der Website:
Shipped / Frühphase / Geplant / Zukunft. Zusätzlich Zielarchitektur-Version von den ausgelieferten
Produktversionen trennen. Scope-Grenze: keine inhaltliche Umschreibung der Kapitel, nur Kennzeichnung.
```

**Nicht in diesem Feature:** die inhaltlichen Lücken, die das Review am Handbuch nennt (Security-Kapitel,
Graph-Skalierung, TOGAF-Mapping). Erst kennzeichnen, dann inhaltlich nacharbeiten — und die
Security-Substanz entsteht ohnehin im graph-Repo, nicht in einem Word-Dokument.

---

### C3 · `template-version-marker` — Versions-Handshake mit dem Graph

**Priorität: Danach. Koordiniert — beide Repos im selben Zug.**

Heute wird Template-Drift erst am Symptom erkannt: `aspark-graph` rätselt strukturell und wirft
`TemplateDriftError` mit einer Vermutung, statt einen Versionskonflikt zu benennen.

**Core-Anteil:** `<!-- aspark-template: aspark/0.1.0 -->` als erste Zeile in jede Datei unter `templates/`.
Die Version steigt nur, wenn sich eine der in §2 geschützten Strukturen ändert.
**graph-Anteil:** Marker lesen, mit `SUPPORTED_TEMPLATE` vergleichen, bei Abweichung klaren
Versionskonflikt melden statt Struktur zu raten. Steht dort als Item G5.

Ohne den graph-Anteil ist der Core-Anteil ein harmloser, aber wirkungsloser Kommentar. Nicht separat
releasen — sonst entsteht ein Marker, den niemand liest.

```
/story-time template-version-marker — Versionsmarkierung in alle Dateien unter templates/ einfügen
(<!-- aspark-template: aspark/0.1.0 -->), damit aspark-graph Template-Drift als Versionskonflikt melden
kann statt strukturell zu raten. Achtung: die Gegenseite (Item G5 im aSPARK-graph-Repo) muss im selben
Zug umgesetzt werden — sonst nicht releasen.
```

---

### C4 · `release-evidence` — `/go-live` schreibt Release-Evidenz maschinenlesbar

**Priorität: Danach. Blockiert durch das graph-Repo (Item G1).**

`aspark-graph` parst `release-notes.md` heute schon, legt Version und Status aber nur als Attribute auf den
Feature-Knoten. Für DORA-Metriken braucht es einen echten `Release`-Knoten mit **Datum und Commit**.
Sobald G1 dort liegt, prüfe hier: schreibt `/go-live` genug, um `version`, `date` und `commit`
deterministisch zu bestimmen — oder muss der Release Manager Tag und Commit-SHA explizit in die Kopftabelle
oder die Release-Actions-Tabelle schreiben?

**Erst starten, wenn G1 im graph-Repo abgeschlossen ist** — sonst wird gegen ein Schema entwickelt, das
noch nicht steht.

---

## 4. Bewusst nicht in diesem Backlog

| Review-Empfehlung | Warum nicht hier |
|---|---|
| Model-Provider-Abstraktion („Now" im Review) | Keine Abstraktion, sondern ein Rewrite: Core *ist* ein Claude-Code-Plugin, das Skills/Agents-Format ist Claude-spezifisch. Braucht eine Strategieentscheidung, nicht ein Feature. **Nicht ohne Rückfrage anfangen.** |
| SAFe-Portfolio-Entities über Story-Ebene | Abgelehnt. Widerspricht der eigenen Complexity-Kritik des Reviews. |
| TOGAF/ArchiMate-Mapping | Zurückgestellt. Zwei Seiten Anhang, wenn ein Kunde danach fragt. |
| „Deterministic vs. human-judgment artifacts" trennen | Gehört in `aspark-policy` (dortige `check:`-Taxonomie `static`/`review`/`manual`), nicht in Core. |
| DORA-Metriken | Gehört in `aspark-graph` (Item G2) — dort liegen Commits und Releases. |
| Sicherheitsarchitektur, MCP-Threat-Model | Gehört in `aspark-graph` (Item G3) — dort läuft der MCP-Server. |
| `aspark-policy` verdrahten | Dort existiert noch keine aufrufbare Oberfläche. |
