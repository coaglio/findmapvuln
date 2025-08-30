# findmapvuln

`findmapvuln` is a simple command-line tool that parses **Nmap XML results** and extracts information about open services, products, versions, and CPEs.  

The goal of this project is to evolve into a utility that can also check for known vulnerabilities (CVEs) based on the detected services.

---

## Usage

Run `findmapvuln` with the path to an Nmap XML file:

```bash
findmapvuln nmap_results.xml
