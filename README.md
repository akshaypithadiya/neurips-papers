# NeurIPS papers web scraping

Web scraping for papers published at the Neural Information Processing Systems Conference

[papers.nips.cc](http://papers.nips.cc/)

## Requirements

1. Download and install [Python 3.7+](https://www.python.org/downloads/)

2. Install requirements
```
pip install beautifulsoup4
pip install lxml
pip install requests
```
## Running

`python3 nips.py`

## Example 

```
[
   {
      "title":"Provable Gradient Variance Guarantees for Black-Box Variational Inference",
      "authors":"Justin Domke",
      "abstract":"Recent variational inference methods use stochastic gradient estimators whose variance is not well understood. Theoretical guarantees for these estimators are important to understand when these methods will or will not work. This paper gives bounds for the common “reparameterization” estimators when the target is smooth and the variational family is a location-scale distribution. These bounds are unimprovable and thus provide the best possible guarantees under the stated assumptions.",
      "pdf":"http://papers.nips.cc/paper/8325-provable-gradient-variance-guarantees-for-black-box-variational-inference.pdf"
   }
]
```
