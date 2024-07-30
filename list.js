const axios = require('axios');
const cheerio = require('cheerio');

let list = [];
let buseoInfo = [
    { id: '3900284', name: '정책기획과' },
    { id: '3900332', name: '탄소중립과' },
    { id: '3900285', name: '예산법무과' },
    { id: '3900255', name: '정보통신과' },
    { id: '3900331', name: '총무과' },
    { id: '3900333', name: '자치분권과' },
    { id: '3900334', name: '회계과' },
    { id: '3900358', name: '세정과' },
    { id: '3900337', name: '민원토지과' },
    { id: '3900262', name: '일자리창출과' },
    { id: '3900308', name: '사회적경제과' },
    { id: '3900309', name: '기업지원과' },
    { id: '3900265', name: '도시농업과' },
    { id: '3900286', name: '문화관광과' },
    { id: '3900287', name: '체육진흥과' },
    { id: '3900268', name: '복지정책과' },
    { id: '3900324', name: '어르신복지과' },
    { id: '3900288', name: '장애인복지과' },
    { id: '3900270', name: '여성가족과' },
    { id: '3900271', name: '보육정책과' },
    { id: '3900273', name: '안전총괄과' },
    { id: '3900274', name: '도로과' },
    { id: '3900275', name: '도시교통과' },
    { id: '3900359', name: '철도정책과' },
    { id: '3900276', name: '하수과' },
    { id: '3900295', name: '가로정비과' },
    { id: '3900357', name: '도시계획과' },
    { id: '3900341', name: '주택과' },
    { id: '3900360', name: '건축과' },
    { id: '3900342', name: '정원도시과' },
    { id: '3900344', name: '건설지원과' },
    { id: '3900362', name: '신도시조성과' },
    { id: '3900363', name: '스마트도시과' },
    { id: '3900364', name: '도시개발과' },
    { id: '3900365', name: '균형개발과' },
    { id: '3900366', name: '도시재생과' },
    { id: '3900326', name: '보건정책과' },
    { id: '3900297', name: '감염병관리과' },
    { id: '3900367', name: '건강위생과' },
    { id: '3900346', name: '평생학습원' },
    { id: '3900347', name: '교육청소년과' },
    { id: '3900368', name: '도서관정책과' },
    { id: '3900348', name: '하안도서관' },
    { id: '3900349', name: '광명도서관' },
    { id: '3900353', name: '환경관리과' },
    { id: '3900354', name: '자원순환과' },
    { id: '3900355', name: '수도과' },
    { id: '3900356', name: '정수과' },
    { id: '3900121', name: '차량등록사업소' },
    { id: '3900035', name : '광명1동' },
    { id: '3900036', name : '광명2동' },
    { id: '3900037', name : '광명3동' },
    { id: '3900038', name : '광명4동' },
    { id: '3900039', name : '광명5동' },
    { id: '3900040', name : '광명6동' },
    { id: '3900041', name : '광명7동' },
    { id: '3900042', name : '철산1동' },
    { id: '3900043', name : '철산2동' },
    { id: '3900044', name : '철산3동' },
    { id: '3900045', name : '철산4동' },
    { id: '3900046', name : '하안1동' },
    { id: '3900047', name : '하안2동' },
    { id: '3900048', name : '하안3동' },
    { id: '3900049', name : '하안4동' },
    { id: '3900050', name : '소하1동' },
    { id: '3900051', name : '소하2동' },
    { id: '3900312', name : '일직동' },
    { id: '3900052', name : '학온동' }
  ]


let buseos = [{ id: '3900328', name: '시민소통관'}]
function makeData() {
    buseos.forEach(b => {
        parsing(b.id)
    });
}

function parsing(id, type){
    let urls = 'https://www.gm.go.kr/pt/gi/cityhallInfo/groupInfo/view.do?q_deptCode=' + id + '&q_chargerId=&q_teamCode=&q_searchKey=chrg_job&q_searchVal=&';
    (async () => {
        try {
          // 웹사이트에서 HTML 가져오기
          const { data } = await axios.get(urls);
          
          const $ = cheerio.load(data, { xmlMode: true, decodeEntities: false });
      
          const details = [];
      
          // 주석 처리된 텍스트와 주석 아닌 텍스트 모두 추출
          $('tbody.text_center').contents().each((index, element) => {
            // 주석 처리된 부분
            if (element.type === 'comment') {
                // 주석 처리된 내용이 HTML로 작성된 경우
                const commentText = element.data.trim();
                console.log(commentText)
                const $inner = cheerio.load(commentText, { xmlMode: false, decodeEntities: false });
                $inner('tr').each((i, row) => {
                  $inner(row).find('td').each((j, cell) => {
                    const value = $inner(cell).text().trim();
                    if (value) {
                      details.push({ value, 주석처리여부: 'Y' });
                    }
                  });
                });
              }
            // 일반 태그 <td> 요소
            else if (element.type === 'tag' && element.name === 'tr') {
              $(element).find('td').each((i, el) => {
                const value = $(el).text().trim();
                if (value) {
                  details.push({ value, 주석처리여부: 'N' });
                }
              });
            }
          });
      
        //   console.log(details);
        } catch (error) {
          console.error(error);
        }
      })();
}


makeData();