# Report Laboratorio: Exploit Java RMI 🛡️

Report tecnico in formato LaTeX sulle attività di penetration testing condotte contro il servizio vulnerabile Java RMI.

## 📋 Scenario del Laboratorio
* [cite_start]**Target (Vittima):** Metasploitable 2 (`192.168.11.112`) [cite: 10]
* [cite_start]**Attaccante:** Kali Linux (`192.168.11.111`) [cite: 9]
* [cite_start]**Servizio Vulnerabile:** Java RMI Server su porta **1099** [cite: 5]

## 🛠️ Strumenti Utilizzati
* **Framework:** Metasploit
* [cite_start]**Modulo Exploit:** `exploit/multi/misc/java_rmi_server` [cite: 38]
* **Payload:** Reverse TCP (Meterpreter)

## 🚀 Fasi Operative
1.  [cite_start]**Configurazione:** Impostazione indirizzi IP statici su entrambe le macchine[cite: 9, 10].
2.  [cite_start]**Exploitation:** Sfruttamento della configurazione insicura del servizio RMI per ottenere una sessione remota[cite: 6].
3.  [cite_start]**Post-Exploitation:** Raccolta evidenze tramite comandi Meterpreter (`ipconfig`, `route`)[cite: 12, 13].

## 📂 Struttura della Repository
* `report.tex`: Codice sorgente del report.
* `*.png/jpg`: Screenshot delle evidenze (configurazione, exploit, shell).

## 📄 Compilazione
Per generare il PDF finale, assicurarsi di avere le immagini nella stessa directory e compilare con un editor LaTeX o da riga di comando:

```bash
pdflatex report.tex
