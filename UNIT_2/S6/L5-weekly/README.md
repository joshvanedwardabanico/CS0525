# Network Authentication Cracking Report - Project U2 S6 L5

Questo repository contiene la documentazione tecnica e le evidenze del laboratorio di Cybersecurity dedicato all'**Authentication Cracking** e all'audit dei servizi di rete.

Il progetto si concentra sull'analisi della robustezza delle credenziali per i protocolli **SSH** e **FTP**, dimostrando la vulnerabilità dei sistemi a fronte di password deboli e attacchi automatizzati.

## 📄 Contenuto del Repository

* **Report Tecnico (PDF/LaTeX):** Analisi dettagliata della metodologia, esecuzione e risultati.
* **Proof of Concept (PoC):** Screenshot e log dell'attività svolta con Hydra.
* **Codice Sorgente LaTeX:** I file sorgente utilizzati per generare il report finale.

## ecnologie e Strumenti Utilizzati

* **OS Attaccante:** Kali Linux
* **Tool di Cracking:** [Hydra](https://github.com/vanhauser-thc/thc-hydra) (Network Logon Cracker)
* **Servizi Target:** SSH (OpenSSH), FTP (vsftpd)
* **Wordlists:** Seclists (Xato-net-10-million)
* **Reporting:** LaTeX

## Metodologia

L'esercitazione è stata suddivisa in due fasi principali:

### 1. Preparazione e Ottimizzazione
Per simulare uno scenario realistico ma efficiente, le wordlist massive (*Seclists*) sono state filtrate utilizzando comandi bash (`grep`, `head`) per creare dizionari mirati e ridurre i tempi di esecuzione del brute-force.

```bash
# Esempio di ottimizzazione wordlist
grep "test" original_wordlist.txt | head -n 15 > target_wordlist.txt
```
### 2. Attacco SSH & FTP
Utilizzo di Hydra per testare le credenziali contro l'indirizzo IP target.

* **Fase 1**: Attacco al servizio SSH (Porta 22).

* **Fase 2**: Installazione, configurazione e attacco al servizio FTP (Porta 21).

### ⚠️ Disclaimer
Questo progetto è stato realizzato esclusivamente a scopo didattico nell'ambito del corso di Cyber Security & Ethical Hacking. Tutte le attività di test sono state condotte in un ambiente di laboratorio controllato e isolato (macchine virtuali locali). L'autore non si assume alcuna responsabilità per l'uso improprio delle informazioni contenute in questo repository.

**Autore**: Josh Van Edward Abanico **Corso**: Cyber Security & Ethical Hacking - CS0525IT - Epicode
