import re
import pandas

def display_features(features, feature_names):
    df = pandas.DataFrame(data=features, columns=feature_names)
    print(df)

    
def get_sentences_v2( text ) :
    sentences = ""
    
    sentences = re.sub(r'[\t\r\f]+', '  ', text)
    sentences = re.sub(r'[\n]+', '  ', sentences)
    sentences = sentences.replace("R&D", "Research_And_Development")
    
    sentences = sentences.replace("Activity", "activity")
    sentences = sentences.replace("activities", "activity")
    sentences = sentences.replace("Activities", "activity")
    
    sentences = sentences.replace("Physical activity", "Physical_Activity")
    sentences = sentences.replace("physical activity", "Physical_Activity")
    sentences = sentences.replace("research", "study")
    #sentences = sentences.replace("Physical activities", "Physical_Activity")
    #sentences = sentences.replace("Physical Activities", "Physical_Activity")
    #sentences = sentences.replace("physical activities", "Physical_Activity")
    
    #re.sub( r"[^a-zA-Z0-9]", " ", t[0] )
    
    return sentences
    
def get_sentences( text ) :
    sentences=""
    #print(sentences)
    sentences = re.sub( r"(http[s]?://)?([\d\w]+)\.([\d\w]+)(\.[\d\w]+)?(/([\d\w]+)*)", "", text )
    sentences = re.sub( r"[\s]*[\n]*[\s]*[\n]+", "\n", sentences )
    sentences = re.sub(r'[\t\r\f]+', '  ', sentences)
    sentences = re.sub(r'[\n]+', '  ', sentences)
    sentences = sentences.replace("&lt", "")
    sentences = sentences.replace("&gt", "")
    #sentences = sentences.replace("사실은_이렇습니다","사실 이렇습니다")
    #sentences = sentences.replace("(성)폭력","성폭력")
    #sentences = re.sub(r'돌봄[\s]?시설', '돌봄센터', sentences)
    
    #if -1 < sentences.find("센터") : 
    #    print( sentences )
    #sentences = re.sub(r'(신고.?.?상담[\s]*센터)|(상담.?.?신고[\s]*센터)', '신고상담센터', sentences)
    sentences = sentences.replace('과제지향', '과제지향훈련')
    sentences = sentences.replace('고령자', '고령')
    sentences = sentences.replace('노년기', '노년')
    sentences = sentences.replace('불안감', '불안')
    sentences = sentences.replace('불안정', '불안')
    sentences = sentences.replace('우울감', '우울')
    sentences = sentences.replace('통제군', '통제집단')
    sentences = sentences.replace('종속변수', '종속변인')
    sentences = sentences.replace('알츠하이머병', '알츠하이머')
    
    sentences = sentences.replace('여자', '여성')
    sentences = sentences.replace('우리나라', '한국')
    sentences = sentences.replace('대한민국', '한국')
    sentences = sentences.replace('남자', '남성')
    #sentences = re.sub(r'k.?pop', 'K팝', sentences)
    #sentences = re.sub(r'K.?POP', 'K팝', sentences)
    #sentences = re.sub(r'주[\s]?52[\s]?시간', '주52시간', sentences)
    #sentences = re.sub(r'주[\w]?[\w]?52[\s]?시간', '주52시간', sentences)
    #
    #sentences = sentences.replace('문대통령', '문재인')
    #sentences = re.sub(r'4차.?산업혁명', '4차산업혁명', sentences)
    #sentences = re.sub(r'개정[\s]?법률안', '개정안', sentences)
    
    # 여기부터 박사 치매 논문 전처리 코드입니다.
    sentences = sentences.replace("웨어러블 헬스케어 디바이스","웨어러블 디바이스")
    sentences = sentences.replace("CVR","내용타당도 비율")
    sentences = sentences.replace("IL","인터루킨")
    
    return sentences


# 한글 품사 태그
def get_pos_tags( komoran, split_sentences ) :
    morph_list = []
    
    for sentence in split_sentences:
        sentence = sentence.strip()
        #print(sentence)
        if '' != sentence :
            try :
                pos_tags=komoran.pos( "\n".join( [ s for s in sentence.split("\n") if s ] ) )
                morph_list.append(pos_tags)
            except Exception :
                print('error : ', sentence) 
        
    return morph_list


# get_NNG_NNP_words : 한글 명사 추출
def get_NNG_NNP_words( morphs_list, stop_words_list ) :
    NNG_NNP_words = []
    for morphs in morphs_list :
        NNG_NNP_words_item=[]
        for word, tag in morphs:
            if tag == 'NNG' or tag == 'NNP':
                # NNG : 일반 명사
                # NNP : 고유 명사
                if None != stop_words_list and len( stop_words_list ) > 0 :
                    stop_word_flag = False
                    #for stop_word in stop_words_list :
                    #    if word == stop_word :
                    #        stop_word_flag=True
                    #        break
                    if word in stop_words_list :
                        stop_word_flag=True
                    if False == stop_word_flag :
                        if "BTS" == word :
                            NNG_NNP_words_item.append("방탄소년단")
                        else :
                            if len(word) > 1 :
                                NNG_NNP_words_item.append(word)
                else :
                    if "BTS" == word :
                        NNG_NNP_words_item.append("방탄소년단")
                    else :
                        #NNG_NNP_words_item.append(word)
                        if len(word) > 1 :
                            NNG_NNP_words_item.append(word)
                        
        NNG_NNP_words.append(NNG_NNP_words_item)
    return NNG_NNP_words
