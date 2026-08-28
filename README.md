<p align="center">
  <img src="docs/assets/fhnix-hero.png" alt="FhniX email risk analysis banner" width="100%">
</p>

<h1 align="center">FhniX</h1>

<p align="center">
  <img src="phishlens/src/phishlens/assets/fhnix-logo.png" alt="FhniX phoenix shield logo" width="96">
</p>

<p align="center">
  Explainable, local-first phishing triage for exported emails and read-only IMAP mailbox scans.
</p>

<p align="center">
  <img alt="Python 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-2ea44f?style=flat-square">
  <img alt="License MIT" src="https://img.shields.io/badge/License-MIT-00b894?style=flat-square">
  <img alt="Status Alpha" src="https://img.shields.io/badge/Status-Alpha-f0ad4e?style=flat-square">
  <img alt="Local first" src="https://img.shields.io/badge/Privacy-Local--first-00bcd4?style=flat-square">
</p>

This GitHub repository is named **FhniX**. The primary product is the Python phishing-email triage tool in [`phishlens/`](phishlens/). The repository root also contains a smaller, separate Rust desktop app (Cargo package `safe-malware-simulator`) that only renders synthetic telemetry.

| Path | What it is | How to run |
| --- | --- | --- |
| [`phishlens/`](phishlens/) | **Primary.** FhniX: explainable local-first phishing triage (CLI + tkinter GUI). Package name `fhnix` 0.5.0. | `cd phishlens` then `py -m pip install -e .` |
| repository root (`Cargo.toml`, `src/main.rs`) | **Secondary.** Safe Malware Behavior Simulator: a tiny egui/eframe trainer. It does not implement FhniX. | `cargo run` |

> [!IMPORTANT]
> FhniX is a defensive triage aid, not a final security verdict. Verify unexpected requests through a trusted, independent channel before taking action.

Full FhniX documentation, including mailbox mode, local training, scoring, and platform notes, lives in [`phishlens/README.md`](phishlens/README.md).

## Why FhniX?

FhniX helps analysts, blue teams, students, and everyday users inspect suspicious emails without opening links or executing attachments. It combines transparent detection rules with an optional locally trained Naive Bayes model and explains the signals behind every result.

| Capability | What it provides |
| --- | --- |
| Explainable analysis | Every warning includes a rule, severity, score contribution, and evidence. |
| Safe inspection | URLs are defanged in reports; links are not visited and attachments are not executed. |
| Local-first workflow | `.eml` analysis, model training, and inference stay on your machine. |
| Flexible input | Analyze one email, scan folders recursively, or fetch recent messages through read-only IMAP. |
| Useful output | Review results in the GUI or export text, JSON, and Excel-friendly CSV reports. |
| Hybrid detection | Combine deterministic security rules with an optional model trained on your own labeled data. |

## Requirements

- Python 3.11 or newer
- Windows, macOS, or Linux
- Tk support when using the desktop GUI
- No third-party runtime dependencies for the core application

## Installation

```powershell
git clone https://github.com/dRafaleD/FhniX.git
cd FhniX/phishlens
py -m pip install -e .
fhnix --version
```

Use `python` instead of `py` on systems where the Python launcher is unavailable. The legacy `phishlens` command remains available for compatibility.

## Quick Start

Analyze an exported email:

```powershell
fhnix analyze "C:\Users\you\Desktop\suspicious.eml"
```

Launch the terminal-style desktop interface:

```powershell
fhnix gui
```

You can also use the short form:

```powershell
fhnix "C:\Users\you\Desktop\suspicious.eml"
```

The GUI supports single-message analysis, folder scans, model loading, local training, evidence inspection, report saving, and CSV export.

<p align="center">
  <img src="phishlens/docs/assets/fhnix-gui.png" alt="FhniX terminal-style desktop interface" width="100%">
</p>

A sample message is included at `phishlens/examples/suspicious.eml`.

## Development tests

From `phishlens/`:

```powershell
$env:PYTHONPATH = "src"
py -m unittest discover -s tests -v
```

## Security

Please do not publish vulnerabilities or sensitive sample emails in public issues. Read [SECURITY.md](SECURITY.md) for the supported version and responsible disclosure process.

## Also in this repository: Safe Malware Behavior Simulator

The files at the repository root (`Cargo.toml`, `src/main.rs`) are **not** FhniX. They are a separate defensive, educational Rust desktop app for demonstrating suspicious telemetry patterns without creating or executing real malware.

Cargo package name: `safe-malware-simulator` 0.1.0. Window title: Safe Malware Behavior Simulator. Tech stack: Rust, `egui`, `eframe`.

It is intended for blue-team demos, malware-analysis training, SOC workflow practice, UI experiments for detection tooling, and classroom-safe behavior simulation. Profiles included in the UI:

- `File Dropper`
- `Persistence`
- `Network Beaconing`
- `Obfuscated Script`
- `Multi-stage Chain`

### Run the simulator

```powershell
cargo run
```

On Windows, Microsoft C++ build tools (Visual Studio Build Tools with the Desktop development with C++ workload, or Visual Studio Community with C++ tooling) may be required so `link.exe` is on `PATH`.

### Safe scope

This simulator stays on the safe side of cybersecurity work:

- no real payload execution
- no registry modification
- no persistence on the host
- no actual file dropping
- no live network traffic
- no exploit or offensive capability

Everything shown in the interface is synthetic telemetry rendered inside the application. Contributions must keep all suspicious behavior synthetic and contained to generated UI output only.

## License

Released under the [MIT License](LICENSE).
