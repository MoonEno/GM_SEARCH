import requests
import re
import json
from bs4 import BeautifulSoup, Comment
from code import encode_json_values_to_base64

# python파일 실행시 
# 시 홈페이지 > 조직 안내 & 전화번호 크롤링 후 
# data >value값이 암호화 되어 json파일 생성됨

gm_list = []
buseo_list = [
    { 'id': '3900328'},
    { 'id': '3900284'},
    { 'id': '3900332'},
    { 'id': '3900285'},
    { 'id': '3900255'},
    { 'id': '3900331'},
    { 'id': '3900333'},
    { 'id': '3900334'},
    { 'id': '3900358'},
    { 'id': '3900337'},
    { 'id': '3900262'},
    { 'id': '3900308'},
    { 'id': '3900309'},
    { 'id': '3900265'},
    { 'id': '3900286'},
    { 'id': '3900287'},
    { 'id': '3900268'},
    { 'id': '3900324'},
    { 'id': '3900288'},
    { 'id': '3900270'},
    { 'id': '3900271'},
    { 'id': '3900273'},
    { 'id': '3900274'},
    { 'id': '3900275'},
    { 'id': '3900359'},
    { 'id': '3900276'},
    { 'id': '3900295'},
    { 'id': '3900357'},
    { 'id': '3900341'},
    { 'id': '3900360'},
    { 'id': '3900342'},
    { 'id': '3900344'},
    { 'id': '3900362'},
    { 'id': '3900363'},
    { 'id': '3900364'},
    { 'id': '3900365'},
    { 'id': '3900366'},
    { 'id': '3900326'},
    { 'id': '3900297'},
    { 'id': '3900367'},
    { 'id': '3900346'},
    { 'id': '3900347'},
    { 'id': '3900368'},
    { 'id': '3900348'},
    { 'id': '3900349'},
    { 'id': '3900353'},
    { 'id': '3900354'},
    { 'id': '3900355'},
    { 'id': '3900356'},
    { 'id': '3900121'},
    { 'id': '3900035'},
    { 'id': '3900036'},
    { 'id': '3900037'},
    { 'id': '3900038'},
    { 'id': '3900039'},
    { 'id': '3900040'},
    { 'id': '3900041'},
    { 'id': '3900042'},
    { 'id': '3900043'},
    { 'id': '3900044'},
    { 'id': '3900045'},
    { 'id': '3900046'},
    { 'id': '3900047'},
    { 'id': '3900048'},
    { 'id': '3900049'},
    { 'id': '3900050'},
    { 'id': '3900051'},
    { 'id': '3900312'},
    { 'id': '3900052'}
]


def getGmData(id): 

    site = 'https://www.gm.go.kr/pt/gi/cityhallInfo/groupInfo/view.do?q_deptCode='
    ids = id
    param = '&q_chargerId=&q_teamCode=&q_searchKey=chrg_job&q_searchVal=&'

    urls = f"{site}{ids}{param}"

    response = requests.get(urls)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    # 주석 처리된 내용까지 포함한 모든 <tr> 태그 찾기
    rows = soup.find_all('tr')
    buseo = ''

    for row in rows:
        row_data = []
        obj = {
            '부서명': '',
            '팀명': '',
            '직위': '',
            '이름': '',
            '전화번호': '',
            '담당업무': '',
        }
        num = 0;
        # <td> 태그와 주석을 포함한 텍스트 수집
        for content in row.contents:
            
            if isinstance(content, Comment):
                # 주석 내용에서 <td> 태그를 추출하여 추가
                comment_soup = BeautifulSoup(content, 'html.parser')
                td_tags = comment_soup.find_all('td')
                for td in td_tags:
                    pattern = r'^\D*$' 
                    text = td.get_text(strip=True)
                    match = re.match(pattern, text) is not None
                    if (bool(match)) : 
                        obj["이름"] = td.get_text(strip=True)
                        num += 1

            elif content.name == 'td':
                    if (num == 0) :
                        buseo = content.get_text(strip=True)
                        obj["부서명"] = content.get_text(strip=True)
                    elif (num == 1) :
                        obj["팀명"] = content.get_text(strip=True)
                    elif (num == 2) :
                        obj["직위"] = content.get_text(strip=True)
                    elif (num == 4) :
                        obj["전화번호"] = content.get_text(strip=True)
                    elif (num == 5) :
                        obj["담당업무"] = content.get_text(strip=True)
                
                    num += 1

        
        if not(obj["이름"] == '') :
            enc_obj = encode_json_values_to_base64(obj)
            gm_list.append(enc_obj)

    print(buseo, len(rows)-1)


for b in buseo_list :
    getGmData(b["id"])

# 결과 출력
#for data in parsed_data:
with open('../data/gm_list.json', 'w', encoding='utf-8') as file :
    json.dump(gm_list, file, ensure_ascii=False, indent=4)

## 부서명/팀명/직위/이름/전화번호/담당업무