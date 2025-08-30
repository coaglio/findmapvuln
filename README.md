# findmapvuln

`findmapvuln` is a command-line tool that parses **Nmap XML results** and correlates detected services and versions with **CPEs and CVEs**.  

It is designed to be lightweight and practical: feed it an Nmap scan in XML format, and quickly identify known vulnerabilities associated with the discovered services.

---

## Features

- Parse Nmap XML output (`-oX output.xml`).
- List services, products, versions, and detected CPEs.
- Query CVEs directly from the **NVD** using CPE identifiers (product+version fallback planned).
- Filter results by severity (LOW / MEDIUM / HIGH / CRITICAL).
- Export results in plain text or JSON for integration with other tools.
- (Planned) Integration with exploit databases (ExploitDB, Vulners).

---

## Usage

Run `findmapvuln` with the path to an Nmap XML file:

```bash
findmapvuln nmap_results.xml
```

This will parse the scan results and display detected services, versions, CPEs, and known vulnerabilities (CVEs).

Optional flags (planned):

```bash
findmapvuln nmap_results.xml --min-severity HIGH --format json --out vulns.json
```

---

## Installation (development)

Clone the repository and run locally:

```bash
git clone https://github.com/<your-username>/findmapvuln.git
cd findmapvuln
python3 findmapvuln.py --help
```

Future releases will include packaging for `.deb` and PyPI.

---

## Roadmap

- [x] Nmap XML parser
- [x] Basic CLI
- [ ] NVD integration (CPE → CVE)
- [ ] Fallback search by product+version
- [ ] JSON output
- [ ] Exploit database integration
- [ ] Packaging for APT / PyPI

---

## Contributing

Contributions, feature requests, and bug reports are welcome. Please open an issue or submit a pull request.

---

## License

MIT License
