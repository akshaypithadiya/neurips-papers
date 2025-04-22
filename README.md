# NeurIPS Papers

A curated collection of NeurIPS conference papers with research in machine learning, AI, and computational neuroscience.

[![Papers Published at NeurIPS](https://user-images.githubusercontent.com/18662067/90985024-a1c32f80-e596-11ea-8804-c3fcbfae2b2b.png)](http://papers.nips.cc/)

## Overview

This repo contains NeurIPS papers scraped from the official website. The data is saved in a structured format for easy use and analysis.

## Features

- Auto-scrapes papers from the NeurIPS site
- Saves paper details in JSON format
- Simple Python script for scraping
- Organized by year
- Includes titles, authors, abstracts, and PDF links

## Installation

1. Install Python 3.8 or higher
2. Set up a virtual environment and install the dependencies :

```bash
python3 -m venv neurips-env
source neurips-env/bin/activate
pip install -r requirements.txt
```

## Requirements

- beautifulsoup4
- requests
- lxml

## Usage

To run the scraper :

```bash
python nips.py
```

## Output Format

Papers are saved as JSON files in the `papers/` folder by year. Example :

```json
[
  {
    "title": "Example Paper Title",
    "authors": "Author 1, Author 2",
    "abstract": "This is an example abstract.",
    "pdf": "http://papers.nips.cc/paper/0000-example-paper.pdf"
  }
]
```

## License

MIT License

## Links

- [Official NeurIPS Website](http://papers.nips.cc/)
- [NeurIPS Conference](https://neurips.cc/)

---
