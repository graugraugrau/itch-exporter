# Itch Exporter

<center><img src="images/itch_exporter.png" alt="Itch Exporter Logo" height="200"/></center>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)
![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)

Prometheus exporter for your itch metrics.

## Links

- [Docker Hub](https://hub.docker.com/r/dunkelgrau/itch-exporter)
- [GitHub (Mirror)](https://github.com/graugraugrau/itch-exporter)

## Installation and Usage

The `itch-exporter` is a Prometheus exporter that monitors itch.io metrics
within a Docker container, allowing you to collect and visualize your
game's performance data in Prometheus. It uses the port `8000` to expose the metrics.

```bash
docker run -d \
  -e API_KEY='1234567890abc' \
  -e INTERVAL='3600' \
  -p 8000:8000 \
  dunkelgrau/itch-exporter:latest
```

| Arguments | Description                                  |
|-----------|----------------------------------------------|
| API_KEY   | Your itch.io API key used to request metrics |
| INTERVAL  | Update interval in seconds (default: 3600)   |

## Collectors

The exporter collects various metrics for each game, identified by the
`game_id` label. Here's a list of available collectors:

| Collector                  | Description                                                         |
|----------------------------|---------------------------------------------------------------------|
| itch_views_count_total     | Total views of the game                                             |
| itch_downloads_count_total | Total downloads of the game                                         |
| itch_purchases_count_total | Total purchases of the game                                         |
| itch_meta_info             | Meta information of the game. E.g. title, description or timestamps |

Here's an example output:

```
# HELP views_count_total Views count
# TYPE views_count_total counter
itch_views_count_total{game_id="1"} 223.0
itch_views_count_total{game_id="2"} 646.0
# HELP downloads_count_total Downloads count
# TYPE downloads_count_total counter
itch_downloads_count_total{game_id="1"} 6.0
itch_downloads_count_total{game_id="2"} 190.0
# HELP purchases_count_total Purchases count
# TYPE purchases_count_total counter
itch_purchases_count_total{game_id="1"} 0.0
itch_purchases_count_total{game_id="2"} 0.0
# HELP meta_info Meta information
# TYPE meta_info gauge
itch_meta_info{created="1720000000000",description="My first game",game_id="1",published="1721000000000",title="First Game"} 1.0
itch_meta_info{created="1730000000000",description="My second game",game_id="2",published="1731000000000",title="Second Game"} 1.0
```