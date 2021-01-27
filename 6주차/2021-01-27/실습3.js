import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

//함수를 정의합니다.
function printStr() {
    return (
        <h2>
            안녕하세요! 코더랜드에 오신걸 환영합니다:)
        </h2>
    )
}

//함수표현식을 사용하여 함수를 호출합니다.
//<h2>태그를 사용해 함수의 결과값을 화면에 출력합니다.
const element = printStr();


ReactDOM.render(element, document.getElementById('root'));

serviceWorker.unregister();
