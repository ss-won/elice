import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';


//element 객체를 생성합니다.
const element = React.createElement(
    'h2',
    { className: 'welcome' },
    '코더랜드에 오신 것을 환영합니다:)'
);


ReactDOM.render(element, document.getElementById('root'));

serviceWorker.unregister();
