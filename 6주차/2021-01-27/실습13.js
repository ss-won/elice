import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

//클래스명이 Welcome인 컴포넌트를 작성합니다.
class Welcome extends React.Component {
    render() {
        return <h2>안녕하세요.{this.props.name}님!</h2>
    }
}


//컴포넌트를 호출하여 element에 저장합니다.
//단, props는 name="Sara"를 제공합니다.
const element = <Welcome name="Sara" />;

ReactDOM.render(element, document.getElementById('root'));

serviceWorker.unregister();
