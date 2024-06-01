# NeurIPS Papers

Papers published at the Neural Information Processing Systems (NeurIPS)

[papers.nips.cc](http://papers.nips.cc/)

![nips](https://user-images.githubusercontent.com/18662067/90985024-a1c32f80-e596-11ea-8804-c3fcbfae2b2b.png)

## Requirements

1. Download and install [Python 3.8+](https://www.python.org/downloads/)

2. Create a virtual environment and install dependencies :

```
python3 -m venv nips-papers
source nips-papers/bin/activate
pip install -r requirements.txt
```

Ensure the requirements.txt file contains the following dependencies :

```
beautifulsoup4
requests
lxml
```

## Running

To run the script, execute the following command :

`python nips.py`

## Example

The script will scrape papers from the NeurIPS website and save them as JSON files in the papers directory. Each JSON file corresponds to a specific year and contains metadata for the papers published that year. The structure and format of the JSON files will look like this :

```
[
    {
        "title": "Example Paper Title",
        "authors": "Author 1, Author 2",
        "abstract": "This is an example abstract.",
        "pdf": "http://papers.nips.cc/paper/0000-example-paper.pdf"
    },
    ...
]
```
