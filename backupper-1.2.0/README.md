# Backupper

Backupper è uno strumento Python Based per la gestione dei backup in formato ZIP o TAR

## Installazione

Per installare il pacchetto Debian con la versione desiderata di Backupper, usa:

``` bash
sudo dpkg -i nomeapp_1.0_all.deb
```
## Funzionalità

- Creazione di archivi ZIP e TAR.
- Estrazione di archivi compressi ZIP o TAR.
- Cancellazione di archivi, partendo dal meno recente.
- Supporto per archivi solo ZIP protetti da password.

## Utilizzo
```
Crea un backup della directory corrente in formato ZIP (default):
backupper -c .
	
Crea un backup della directory corrente in formato TAR:
backupper -c -f tar .

Estrai un archivio dalla directory corrente con nome corrispondente alla directory corrente e data più recente:
backupper -x .

Cancella un archivio specificando il formato tar, con nome directory corrente:
backupper -d -f tar .

Prova ad eseguire man backupper per visionare il backupper.
```
## Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file LICENSE per maggiori dettagli.