import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

//href 속성을 활용해 페이지 이동을 구현합니다.
const element = (
    <a href="https://kdt.elice.io/explore">다양한 과목을 배워봅시다!</a>
);


ReactDOM.render(element, document.getElementById('root'));

serviceWorker.unregister();
