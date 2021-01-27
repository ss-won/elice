import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

//HTML을 JSX로 변환하여 element에 저장합니다.
const element = (
    <div>
        <h2>코더랜드에 오신것을 환영합니다:)</h2>
        <h2>즐거운 React! 함께 공부해봐요~</h2>
    </div>
);

ReactDOM.render(element, document.getElementById('root'));

serviceWorker.unregister();
