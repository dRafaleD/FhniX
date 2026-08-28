# Security Policy

This repository contains two defensive projects. Please say which one a report is about.

| Project | Location | Notes |
| --- | --- | --- |
| **FhniX** (primary) | [`phishlens/`](phishlens/) | Local-first phishing email triage. Additional detail: [`phishlens/SECURITY.md`](phishlens/SECURITY.md). |
| Safe Malware Behavior Simulator | repository root (`Cargo.toml`, `src/main.rs`) | Synthetic telemetry only. Cargo package name `safe-malware-simulator`. |

## Supported Version

FhniX is currently in alpha. Security fixes are applied to the latest version on the `main` branch.

## Reporting a Vulnerability

Please do not disclose security vulnerabilities or sensitive email samples in a public GitHub issue.

Use GitHub's private vulnerability reporting feature from the repository's **Security** tab when it is available. If private reporting is unavailable, contact the repository owner through the private contact method listed on their GitHub profile and include only the minimum information needed to reproduce the issue.

A useful report contains:

- which project is affected (FhniX or the simulator)
- the affected version or commit
- a clear description of the impact
- safe reproduction steps
- relevant logs with credentials, tokens, email addresses, and message content removed
- a suggested mitigation, if known

Please allow reasonable time for investigation and remediation before public disclosure.

Do not submit real malware samples, live credentials, or active payloads in issues or pull requests.

## FhniX scope

Reports about unsafe URL handling, attachment execution, credential exposure, IMAP privacy, parser crashes caused by crafted email, model-data leakage, and report injection are especially valuable.

False positives, missed phishing indicators, and feature requests are not security vulnerabilities. They can be reported through regular GitHub issues using sanitized sample data.

## Simulator scope

The simulator does not contain real malware, exploitation logic, persistence code, credential theft, or offensive automation. All activity it shows is synthetic log generation inside the app.

The following are out of scope:

- requests to add offensive features
- exploit development
- persistence on the host machine
- real command execution chains
- live network beaconing or data exfiltration

Contributions must keep all suspicious behavior synthetic and contained to generated UI output only.
