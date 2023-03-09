### Covid_cli

- A simple CLI for tracking and getting info about Coronavirus Outbreak

#### Dependencies

- click
- pandas==0.25
- pyfiglet
- tabulate

#### Installation

```bash
pip install covid_cli
```

### API

```bash
covid_cli show confirmed|recovered
covid_cli get latest|previous|dataset|status
covid_cli search "Countryname" --cases confirmed
covid_cli info
```

### Usage

#### Show Cases of Coronavirus By configrmed|recovered|deaths|all

```bash
covid_cli show confirmed
```

#### Get Latest Cases of Coronavirus

```bash
covid_cli get latest
```

#### Get Previous Cases of Coronavirus

```bash
covid_cli get previous
```

#### Fetch and Download Current Dataset

```bash
covid_cli get dataset
```
