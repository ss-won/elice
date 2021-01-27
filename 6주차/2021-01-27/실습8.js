import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';


//hello, React!를 출력하는 JSX를 element에 저장합니다.
const element = (<h1>Hello, React!</h1>);

//ReactDOM에 element를 렌더링합니다.
ReactDOM.render(element, document.getElementById('root'));

serviceWorker.unregister();
