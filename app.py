import time
import streamlit as st
from transformers import pipeline
st.set_page_config(page_title='Encoder and Decoder Sentiment',page_icon='🎬')
st.title('Encoder and Decoder Sentiment')
st.write('Compare DistilBERT and DistilGPT2 fine-tuned on IMDb movie reviews.')
MODELS={'Encoder':'sangatbaloch/imdb-encoder-finetuned','Decoder':'sangatbaloch/imdb-decoder-finetuned'}
@st.cache_resource(max_entries=2)
def load_model(repo):
    return pipeline('text-classification',model=repo,device=-1)
choice=st.selectbox('Choose model',['Compare both','Encoder','Decoder'])
review=st.text_area('Enter an English movie review',max_chars=10000)
st.caption('Inputs are truncated to 256 tokens. Confidence is uncalibrated.')
if st.button('Analyze',type='primary'):
    if not review.strip():
        st.warning('Enter a review first.')
    else:
        rows=[]
        for name in (list(MODELS) if choice=='Compare both' else [choice]):
            try:
                with st.spinner('Running '+name):
                    model=load_model(MODELS[name])
                    start=time.perf_counter()
                    result=model(review.strip(),truncation=True,max_length=256)[0]
                    elapsed=time.perf_counter()-start
                rows.append({'Model':name,'Sentiment':result['label'],'Confidence':round(result['score'],4),'Seconds':round(elapsed,3)})
                st.markdown(f"[{name} model and evaluation](https://huggingface.co/{MODELS[name]})")
            except Exception:
                st.error(name+' is unavailable. Verify that the fine-tuned model is uploaded and public.')
        if rows: st.dataframe(rows,hide_index=True)
        if len(rows)==2:
            st.write('Models agree.' if rows[0]['Sentiment']==rows[1]['Sentiment'] else 'Models disagree.')
st.caption('Educational experiment on English movie reviews. Sarcasm, mixed sentiment and domain shift can cause errors. Timing excludes model loading.')
