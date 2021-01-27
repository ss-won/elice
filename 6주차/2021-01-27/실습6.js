import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

//자식태그를 활용하여 JSX코드를 작성해 element에 저장합니다.
const element = (
    <div>
        <h2>안녕하세요:)</h2>
        <h2>오늘도 화이팅!!</h2>
    </div>
);


ReactDOM.render(element, document.getElementById('root'));

serviceWorker.unregister();
