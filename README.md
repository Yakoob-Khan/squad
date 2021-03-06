## Fine-tuning BERT-inspired Deep Learning Models for Question-Answering
> CS 72 Accelerated Computational Linguistics
> 
> Final Project Spring 2020
>
> Yakoob Khan '21 

## Layout of Code Repository

    ├── baseline-model          # BiDAF model provided by Stanford CS 224n
        ├── Baseline.ipynb 
    ├── bert-models      	    # Using Hugging Face transformers library
        ├── DistilBERT.ipynb 
        ├── RoBERTa.ipynb
    ├── model-architectures     # images of BERT models 
    ├── screen-captures         # Screenshots from model training     
    ├── Final Report.pdf             
    └── README.md

## Dataset
> [SQuAD 1.1](https://rajpurkar.github.io/SQuAD-explorer/explore/1.1/dev/)

## Results
Model |F1 Score (%) | EM Score (%) | Training (hrs)
--- | --- | --- | ---
BiDAF (baseline) | 78.98 | 69.73 | 2.5 
Distil-BERT | **84.86** | 75.94 | 5
Distil-RoBERTa | 84.74 | **76.09** | 2
Human Performance | 89.452 | 86.831 |
SOTA | 93.011 | 90.724 |

The following bar chart visualizes the above results
<p align="left">
  <img src="./screen-captures/graph.png">
</p>

## Technologies
* Pytorch
* Hugging Face Transformer's Library

## References
* [SQuAD: 100,000+ Questions for Machine Comprehension of Text (EMNLP 2016, Rajpurkar, et al)](https://arxiv.org/pdf/1606.05250.pdf)
* [Bidirectional Attention Flow for Machine Comprehension (ICLR 2017, Seo, et al)](https://arxiv.org/pdf/1611.01603.pdf)
* [DistilBERT, a distilled version of BERT: smaller,
faster, cheaper and lighter (NeurIPS 2019, Sanh et. al)](https://arxiv.org/pdf/1910.01108.pdf)
* [RoBERTa: A Robustly Optimized BERT Pretraining Approach (Facebook AI)](https://arxiv.org/pdf/1907.11692.pdf)
* [Stanford CS 224n](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/index.html)

## Acknowledgements
> Professor Rolando A. Coto-Solano for teaching me Computational Linguistics in Spring 2020.
