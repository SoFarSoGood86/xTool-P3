<img alt="502509645-d4509657-fee1-4f48-93cf-479a61443ec7" src="https://github.com/user-attachments/assets/d2a65667-f684-444f-960a-e4556185c2d5" />

## xTool P3 intégration for pour Home Assistant.

## Features :

- IP device connexion
- Real-time statut (idle, printing, paused, error)
- Commands Start / Pause / Stop
- Real-time température
- Custom icon in HACS

## Installation :

Install via HACS

1. Navigate to HACS -> Integrations -> "+ Explore & Download Repos" Search for *xTool-P3*.
2. Click on the result and select "Download this Repository with HACS".
3. Refresh your browser (due to a known HA bug that may not update the integration list immediately).
4. Go to "Settings" in the Home Assistant sidebar, then select "Devices and Services".
5. Click the blue [+ Add Integration] button at the bottom right, search for "xTool-P3", and install it.  

   [![Set up a new integration in Home Assistant](https://my.home-assistant.io/badges/config_flow_start.svg)](https://github.com/SoFarSoGood86/xTool-P3.git)



## YAML Configuration (optionnal) :
```yaml
xtool_p3:
  host: 192.168.0.120
  api_key: "your_api_key"
  scan_interval: 10
```

## Available services :
- `xtool_p3.start_job`
- `xtool_p3.pause_job`
- `xtool_p3.stop_job`
