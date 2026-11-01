# IMDb encoder and decoder experiment

Both pretrained models were fine-tuned on a Tesla T4 in Google Colab. The task is binary movie review sentiment classification (negative=0, positive=1).

| Model | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| DistilBERT encoder | 0.899 | 0.911340 | 0.884 | 0.897462 |
| DistilGPT2 decoder | 0.857 | 0.849315 | 0.868 | 0.858556 |

These are measured results on the same 1000 held-out official IMDb test reviews. Precision, recall and F1 use the positive class. Encoder confusion matrix: [[457,43],[58,442]]. Decoder: [[423,77],[66,434]]. Rows=true labels; columns=predicted labels; negative then positive.

## Procedure
Base checkpoints: distilbert/distilbert-base-uncased and distilbert/distilgpt2. Each receives a sequence classification head; both backbone and head are fine-tuned. Encoder uses bidirectional attention; decoder uses causal attention and predicts sentiment rather than generating text.

Dataset: stanfordnlp/imdb. Stratified subsets: 4000 training, 1000 validation, 1000 test; seed 42. Both models use identical subsets. Two epochs, learning rate 2e-5, weight decay 0.01, batch size 8 with 2-step accumulation, maximum 256 tokens, dynamic padding, FP16. Decoder uses EOS as its padding token. Best validation F1 selects the checkpoint. Test data never selects checkpoints.

## Interpretation and limitations
The encoder achieved 4.2 percentage points higher accuracy and about 0.0389 higher F1. This single experiment does not establish universal architecture superiority: model size and pretraining also differ. These are subset results, not full IMDb benchmark scores. No significance test was run. Sarcasm, domain shift, mixed sentiment and truncated reviews can cause errors. Confidence is uncalibrated.

## Reproducible notebook
https://colab.research.google.com/drive/1BqLHstwb4a3MU9mVpBOpyPXrhJeeIEw5

Both fine-tuned weights, tokenizers, configurations, model cards and measured metrics are saved in the active Colab runtime. Hugging Face upload and live Streamlit verification are pending authentication; this repository alone is not a completed live deployment.
