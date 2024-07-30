## Prerequisites
- Docker
- Python 3.x
- (Optional) Conda for environment management

## Installation

Install required Python libraries from `data` directory:
   
- Using conda:
```bash
conda create --file requirements.txt --name db
conda activate db
```

- OR using pip:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Database
- Initialize and run the Postgres DB container:
```bash
docker compose up db --detach
```

<!-- ADD TEST FILES AND DETAILS -->