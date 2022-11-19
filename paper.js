const fetch = require('node-fetch');
const fs = require('fs');

fetch("https://searchtest.aminer.cn/aminer-search/search/publication", {
  "headers": {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://www.aminer.cn/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "{\"query\":\"smart contract\",\"needDetails\":true,\"page\":0,\"size\":6000,\"aggregations\":[{\"field\":\"keywords.keyword\",\"size\":20,\"type\":\"terms\"},{\"field\":\"authors.orgid\",\"size\":20,\"type\":\"terms\"},{\"field\":\"authors.id\",\"size\":10,\"type\":\"terms\",\"subAggregationList\":[{\"field\":\"year\",\"size\":20,\"type\":\"terms\",\"order\":{\"field\":\"_key\",\"asc\":false}}]},{\"field\":\"year\",\"size\":10,\"type\":\"terms\",\"order\":{\"field\":\"_key\",\"asc\":false},\"subAggregationList\":[{\"field\":\"authors.id\",\"size\":5,\"type\":\"terms\"}]},{\"field\":\"venue_hhb_id\",\"size\":20,\"type\":\"terms\"},{\"field\":\"conf_tag\",\"size\":20,\"type\":\"terms\"}],\"filters\":[]}",
  "method": "POST"
}).then(res => res.json())
.then(json => {
    console.log(json['data']['hitList'].length)
    fs.writeFile('res.json', JSON.stringify(json['data']['hitList']), ()=>{
        console.log('保存成功')
    })
}
);
