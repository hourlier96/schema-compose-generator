# schema-compose-generator

## Usage

To parse docker-compose, and find matching pattern from compare.json

```bash
python3 parsing.py docker-compose.yml
```

<br/>

To generate diagram from docker-compose

```bash
python3 transition.py docker-compose.yml
```


## Description

schema-compose-generator parses docker-compose.yml to generate a schema about current architecture using diagrams library


## Dependencies and Requirements

## Dependencies

Install dependencies with 

```bash
pip3 install -r requirements.txt
```


## Requirements

To make it work, you will have to specify links between your services with the following shape:


#### I)

Suppose you have 3 services called A, B, C:

Then add on top of docker-compose.yml:

```bash
x-communication:
	- A >> B     # Service A requests service B
	- B >> C     # Service B requests service C
```

This way the algorithm will know which links to put between services

#### II)

The algorithm deduce technology fo each services from either service name, container name, or image name,
and search in a long list of technology to find a match.
So be as precise as possible for naming.
