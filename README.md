# HuutoHaavi

This project collects, analyzes, and displays real estate data from the Uusimaa region in Finland.

## Project Structure
- `scraper/`: Contains web scraping scripts to collect real estate data
- `database/`: Handles database operations and models using PostgreSQL
- `web/`: Flask web application for displaying the real estate data

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up PostgreSQL database:
- Create a new database named 'uusimaa_real_estate'
- Update database configuration in `database/config.py`

3. Run the application:
```bash
python web/app.py
```

## Technologies Used
- Python 3.x
- PostgreSQL
- Flask
- SQLAlchemy
- BeautifulSoup4 (for web scraping)

## Project Status
Under development
