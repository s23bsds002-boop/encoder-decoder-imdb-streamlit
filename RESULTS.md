# Measured IMDb experiment results

Both models were genuinely fine-tuned in Google Colab on a Tesla T4 GPU.
Dataset: stanfordnlp/imdb. Identical stratified subsets: 4,000 training,
1,000 validation, 1,000 official test reviews. Seed 42, two epochs,
learning rate 0.00002, effective batch size 16, maximum 256 tokens.
Checkpoint selection used validation F1 only.

| Model | Test accuracy | Precision | Recall | F1 | Parameters |
|---|---:|---:|---:|---:|---:|
| DistilBERT encoder | 0.899 | 0.911340 | 0.884 | 0.897462 | 66,955,010 |
| DistilGPT2 decoder | 0.857 | 0.849315 | 0.868 | 0.858556 | 81,914,112 |

Precision, recall and F1 use positive sentiment as the positive class.
Confusion matrices (rows=true, columns=predicted; negative then positive):

- Encoder: [[457, 43], [58, 442]]
- Decoder: [[423, 77], [66, 434]]

The encoder achieved 4.2 percentage points higher test accuracy and
approximately 0.0389 higher F1 on this experiment. Its bidirectional
attention is suited to classification, but this single experiment does
not prove an architecture is always better. The models differ in size
and pretraining as well as attention structure. Results are on subsets,
not the full IMDb benchmark. No statistical significance test was run.

Training notebook:
https://colab.research.google.com/drive/1BqLHstwb4a3MU9mVpBOpyPXrhJeeIEw5

GitHub repository:
https://github.com/s23bsds002-boop/encoder-decoder-imdb-streamlit

Weights, tokenizers, configurations, model cards and measured metrics are
saved in the active Colab runtime under /content/Encoder_Decoder_Assignment.
These runtime files are temporary until uploaded or downloaded.
Both Hugging Face models have been uploaded and remotely reloaded successfully.
The public Streamlit app has been deployed and verified without a login. Both models pass positive and negative reviews in Compare both mode, each model works individually, and empty input shows a warning.
See SUBMISSION_LINKS.md for submission URLs and current verification status.


## Submission links

- Live app: https://sangatbaloch-encoder-decoder-imdb.streamlit.app/
- Encoder: https://huggingface.co/sangatbaloch/imdb-encoder-finetuned
- Decoder: https://huggingface.co/sangatbaloch/imdb-decoder-finetuned

Runtime: CPU-only PyTorch 2.6.0, Streamlit 1.44.1; file watching disabled for compatibility with PyTorch custom classes.
