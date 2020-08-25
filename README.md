# NIPS papers

Web scraping for papers published at the Neural Information Processing Systems (NIPS) Conference

[papers.nips.cc](http://papers.nips.cc/)

![nips](https://user-images.githubusercontent.com/18662067/90985024-a1c32f80-e596-11ea-8804-c3fcbfae2b2b.png)

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
      "title":"Multimodal Model-Agnostic Meta-Learning via Task-Aware Modulation",
      "authors":"Risto Vuorio, Shao-Hua Sun, Hexiang Hu, Joseph J. Lim",
      "abstract":"Model-agnostic meta-learners aim to acquire meta-learned parameters from similar tasks to adapt to novel tasks from the same distribution with few gradient updates. With the flexibility in the choice of models, those frameworks demonstrate appealing performance on a variety of domains such as few-shot image classification and reinforcement learning. However, one important limitation of such frameworks is that they seek a common initialization shared across the entire task distribution, substantially limiting the diversity of the task distributions that they are able to learn from. In this paper, we augment MAML with the capability to identify the mode of tasks sampled from a multimodal task distribution and adapt quickly through gradient updates. Specifically, we propose a multimodal MAML (MMAML) framework, which is able to modulate its meta-learned prior parameters according to the identified mode, allowing more efficient fast adaptation. We evaluate the proposed model on a diverse set of few-shot learning tasks, including regression, image classification, and reinforcement learning. The results not only demonstrate the effectiveness of our model in modulating the meta-learned prior in response to the characteristics of tasks but also show that training on a multimodal distribution can produce an improvement over unimodal training. The code for this project is publicly available at https://vuoristo.github.io/MMAML.",
      "pdf":"http://papers.nips.cc/paper/8296-multimodal-model-agnostic-meta-learning-via-task-aware-modulation.pdf"
   },
   {
      "title":"ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations for Vision-and-Language Tasks",
      "authors":"Jiasen Lu, Dhruv Batra, Devi Parikh, Stefan Lee",
      "abstract":"We present ViLBERT (short for Vision-and-Language BERT), a model for learning task-agnostic joint representations of image content and natural language. We extend the popular BERT architecture to a multi-modal two-stream model, processing both visual and textual inputs in separate streams that interact through co-attentional transformer layers. We pretrain our model through two proxy tasks on the large, automatically collected Conceptual Captions dataset and then transfer it to multiple established vision-and-language tasks -- visual question answering, visual commonsense reasoning, referring expressions, and caption-based image retrieval -- by making only minor additions to the base architecture. We observe significant improvements across tasks compared to existing task-specific models -- achieving state-of-the-art on all four tasks. Our work represents a shift away from learning groundings between vision and language only as part of task training and towards treating visual grounding as a pretrainable and transferable capability.",
      "pdf":"http://papers.nips.cc/paper/8297-vilbert-pretraining-task-agnostic-visiolinguistic-representations-for-vision-and-language-tasks.pdf"
   }

]
```
