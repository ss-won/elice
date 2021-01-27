import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

//정의된 이름
const name = "Sara"

//함수명이 Welcome인 컴포넌트를 작성합니다.
function Welcome(props) {
    return (
        <h2>Welcome, {props.name}!</h2>
    );
}

//컴포넌트를 호출하여 element에 저장합니다.
const element = <Welcome name={name} />;

ReactDOM.render(element, document.getElementById('root'));


serviceWorker.unregister();
