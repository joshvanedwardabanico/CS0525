# Report Laboratorio: Exploit Java RMI 🛡️

Report tecnico sulle attività di penetration testing condotte contro il servizio vulnerabile Java RMI.

## 📋 Scenario
* **Target:** Metasploitable 2 (`192.168.11.112`) 
* **Attaccante:** Kali Linux (`192.168.11.111`) 
* **Vulnerabilità:** Java RMI Server (Porta **1099**)

## 🚀 Attività Svolta
1.  **Configurazione:** Impostazione rete statica su VM Attaccante e Vittima.
2.  **Exploit:** Utilizzo del modulo Metasploit `exploit/multi/misc/java_rmi_server`.
3.  **Post-Exploitation:** Ottenimento sessione Meterpreter ed enumerazione rete (configurazione interfacce e routing)

---
**Autore:** Josh Van Edward D. Abanico
