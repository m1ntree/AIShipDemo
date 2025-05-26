# app_translation.py
import gradio as gr 
from transformers import pipeline

# 지정된모델: 영어-> 한국어번역파이프라인로드
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ko-en")
def translate_text(text_to_translate):
    if not text_to_translate.strip():
        return""
    translated_text = translator(text_to_translate)
    return translated_text[0]['translation_text']

iface= gr.Interface(
    fn=translate_text,
    inputs=gr.Textbox(lines=5, placeholder="Enter Korean text to translate..."),
    outputs=gr.Textbox(lines=5, label="번역결과(English)"),
    title="한-영번역기(opus-mt-ko-en)",
    description="Hugging Face Transformers 모델(Helsinki-NLP/opus-mt-ko-en)을사용한번역앱입니다."
)
iface.launch() # 로컬테스트용. Hugging Face Spaces는app.py 파일을직접실행