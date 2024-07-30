// const fs = require('fs');

// Base64로 텍스트를 인코딩하는 함수
function encodeTextBase64(text) {
    return btoa(encodeURIComponent(text).replace(/%([0-9A-F]{2})/g,
        (match, p1) => String.fromCharCode(parseInt(p1, 16))));
}

// Base64로 인코딩된 텍스트를 디코딩하는 함수
function decodeTextBase64(encodedText) {
    return decodeURIComponent(Array.prototype.map.call(atob(encodedText), 
        c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)).join(''));
}

// JSON 데이터의 값만 인코딩하는 함수
function encodeJsonValuesBase64(data) {
    let encodedData = {};
    for (let key in data) {
        if (data.hasOwnProperty(key)) {
            encodedData[key] = encodeTextBase64(data[key]);
        }
    }
    return encodedData;
}

// JSON 데이터의 값만 디코딩하는 함수
function decodeJsonValuesBase64(data) {
    let decodedData = {};
    for (let key in data) {
        if (data.hasOwnProperty(key)) {
            decodedData[key] = decodeTextBase64(data[key]);
        }
    }
    return decodedData;
}






