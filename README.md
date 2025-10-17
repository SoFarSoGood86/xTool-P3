<img width="3083" height="884" alt="xTool P3" src="https://github.com/user-attachments/assets/d4509657-fee1-4f48-93cf-479a61443ec7" />

xTool P3 intégration for pour Home Assistant.

## Fonctionnalités :
- Connexion à la machine via IP locale
- Suivi de l’état (idle, printing, paused, error)
- Commandes Start / Pause / Stop
- Capteur température interne
- Icône personnalisée dans HACS

## Installation via HACS :
Ajouter le dépôt comme repository personnalisé : `https://github.com/SoFarSoGood86/xTool-P3`

## Configuration YAML (optionnelle) :
```yaml
xtool_p3:
  host: 192.168.0.120
  api_key: "votre_cle_api_si_necessaire"
  scan_interval: 10
```

## Services disponibles :
- `xtool_p3.start_job`
- `xtool_p3.pause_job`
- `xtool_p3.stop_job`
