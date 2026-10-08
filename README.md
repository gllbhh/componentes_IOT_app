# Components of IoT Application

Learning diary and assignments for the **Components of IoT Application** course, Autumn 2026, at Oulu University of Applied Sciences (Oamk).

Gleb Bulygin · DIN24SP

Course page: [tl.oamk.fi/iot](https://tl.oamk.fi/iot/)

---

## Weeks

Each week has a Markdown file with my answers, an exported PDF, and the screenshots, code and capture files used in the answers.

| Week | Topic | Questions | Diary | PDF |
| --- | --- | --- | --- | --- |
| 1 | Networking basics, network devices, RFCs, OSI vs TCP/IP | 1–6 | [week1.md](week1/week1.md) | [PDF](week1/week1.pdf) |
| 2 | VLANs, routing, AS/BGP, DNS, traceroute, IPv4 subnetting | 7–19 | [week2.md](week2/week2.md) | [PDF](week2/week2.pdf) |
| 3 | TCP/UDP, network services, netstat | 20–25 | [week3.md](week3/week3.md) | [PDF](week3/week3.pdf) |
| 4 | File transfer with croc, NTP, Python socket programming | 26–28 | [week4.md](week4/week4.md) | [PDF](week4/week4.pdf) |
| 5 | Encoding vs encryption, Wireshark, JSON, GraphQL, curl, base64 | 29–37 | [week5.md](week5/week5.md) | [PDF](week5/week5.pdf) |
| 6 | MQTT, CoAP, 6LoWPAN, RPL, HTTP/1.1–3, WebSockets, Firebase | 38–57 | [week6.md](week6/week6.md) | [PDF](week6/week6.pdf) |
| 7 | Information security: CVE/CVSS, STRIDE, DREAD, real-world IoT vulnerabilities | 58–68 | [week7.md](week7/week7.md) | [PDF](week7/week7.pdf) |

## Repository structure

```text
weekN/
├── weekN.md      # questions and answers for the week
├── weekN.pdf     # PDF export of weekN.md
└── src/          # screenshots, scripts and other artifacts
```

Week 1 keeps its screenshots next to `week1.md` instead of in `src/`.

Notable artifacts:

- [week4/src](week4/src): Python TCP client/server and the NTP client used in week 4
- [week5/src](week5/src): Wireshark captures (`.pcap`), the IoT sensor JSON file and FMI weather XML from week 5

## Exporting to PDF

The PDFs are made with the VS Code extension **Custom MD PDF** (`deadpoulpe.custom-md-pdf`). The workspace settings in [.vscode/settings.json](.vscode/settings.json) and the stylesheet [.vscode/markdown-pdf.css](.vscode/markdown-pdf.css) give it a light, GitHub-like look, a page-number footer, and page breaks that keep headings, figures and captions together.

To export a week, open its `.md` file and run **Custom MD PDF: Export (pdf)** from the command palette.

## Note on tools

I wrote the answers in my own words first. Before committing, I used Claude to verify the answers, improve wording and grammar, and keep the formatting consistent across weeks.
