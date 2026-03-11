from translate import  Translator

text = '안녕하세요. 제 이름은 인공지능 스피커입니다.'

# Translator 객체 생성
translator = Translator(to_lang='ja', from_lang='ko')

# 번역 실행
result = translator.translate(text) # 한국어를 영어로 번역

print('원본 텍스트 :', text)
print("번역된 텍스트 :", result)