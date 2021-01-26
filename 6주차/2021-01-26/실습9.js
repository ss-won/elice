// 1. 아이디가 apple인 요소의 첫번째 자식 노드를 선택하도록 코드를 작성하세요.
var apple_node = document.getElementById('apple').childNodes[0];

// 2. apple_node의 값을 변수에 할당하도록 코드를 작성하세요.
var apple_node_value = apple_node.nodeValue;
// 해당 노드의 TextNode의 textContent값을 반환한다.
// nodeValue -> 해당 노드의 값을 반환한다.

// 3. apple_node의 타입을 변수에 할당하도록 코드를 작성하세요.
var apple_node_type = apple_node.nodeType;

// 4. apple_node의 값과 타입을 출력합니다.
// document.write는 바로 html로 바꾸어서 출력하는 함수이므로
// 문자열 그대로 인식하지 못하고 하나의 문자열 자체로 인식한다.
// 따라서 줄바꿈을 하려면 <br>과 같이 `태그`로 적어야한다.
document.write(apple_node_value + '\n');
document.write(apple_node_type);