import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';


//클릭 횟수 저장 변수
let value = 0

//클릭 횟수 증가 함수
function click() {
    value = value + 1;
}

//엘리먼트 업데이트 & 렌더링 함수
function tick() {
    const element = (
        <div>
            <h1>버튼을 클릭해보세요</h1>
            <button onClick={click}>Click Me!</button>
            <h2>총 {value}번 클릭했습니다.</h2>
        </div>
    );

    ReactDOM.render(element, document.getElementById('root'));
}

//1초마다 tick()함수 호출
setInterval(tick, 1000);

serviceWorker.unregister();
