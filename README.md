# OpenReliefKit

![CI](https://github.com/OpenRelief/OpenReliefKit/actions/workflows/ci.yml/badge.svg)

OpenReliefKit provides a ready-to-extend toolkit for rapid disaster response. Our goal is to lower the barrier for communities and NGOs to deploy essential tools in the first hours after a disaster. Clone the repo and spin up a communication hub, crisis map, and resource tracker in minutes.

## Quick start

1. Install [Docker](https://docs.docker.com/get-docker/).
2. Run:
   ```sh
   docker compose up --build
   ```
3. Visit `http://localhost:8000/ui` for the Crisis Map UI and `http://localhost:3001` for the Comms Hub.

To run the Python services locally without Docker:

```sh
pip install -r requirements.txt
uvicorn core/crisis_map/backend.app:app --reload
```

## Requesting new modules

Open an issue or discussion describing the desired module. Tag it with `help wanted` if you'd like collaborators.

## Repository layout

```
OpenReliefKit/
├── core/               # main modules
├── datasets/           # data samples
├── hardware/           # open hardware plans
├── scripts/            # helper scripts
└── tests/              # unit tests
```
