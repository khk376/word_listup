from konlpy.tag import Okt
from collections import Counter
 
def get_tags(text, ntags=50):
    spliter = Okt()
    # konlpy의 (구 Twitter) => Okt객체

     # nouns 함수를 통해서 text에서 명사만 분리/추출
    nouns = spliter.nouns(text)
    #nouns = spliter.pos(text)
    #nouns = spliter.morphs(text)
   
    count = Counter(nouns)
    # Counter객체를 생성하고 참조변수 nouns할당
    return_list = []  # 명사 빈도수 저장할 변수
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)
    # most_common 메소드는 정수를 입력받아 객체 안의 명사중 빈도수
    # 큰 명사부터 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
    # 명사와 사용된 갯수를 return_list에 저장
    return return_list
 
 
def main():
    text_file_name = "results.txt"
    # 분석할 파일
    noun_count = 400
    # 최대 많은 빈도수 부터 30개 명사 추출
    output_file_name = "boja3.txt"
    # result.txt 에 저장
    open_text_file = open(text_file_name, 'r',-1,"utf-8")
    # 분석할 파일을 open 
    text = open_text_file.read() #파일 읽기
    tags = get_tags(text, noun_count) # get_tags 함수 실행
    open_text_file.close()   #파일 close
    open_output_file = open(output_file_name, 'w',-1,"utf-8")
    # 결과로 쓰일 result.txt 열기
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{} {}\n'.format(noun, count))
    # 결과 저장
    open_output_file.close() 
 
if __name__ == '__main__':
    main()
    