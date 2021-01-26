// 1. document 의 자식 노드들 중 두번째 노드를 node1변수에 할당하도록 코드를 작성하세요.
var node1 = document.childNodes[1];

// 2. node1의 자식 노드들 중 세번째 노드를 node2변수에 할당하도록 코드를 작성하세요.
var node2 = node1.childNodes[2];

// 3. node2의 자식 노드들 중 두번째 노드를 node3변수에 할당하도록 코드를 작성하세요.
var node3 = node2.childNodes[1];

// 4. node1, node2, node3의 이름을 nodeName을 이용해 출력하도록 코드를 작성하세요.

document.write(node1.nodeName);
document.write(node2.nodeName);
document.write(node3.nodeName);

// //5. `node2`의 자식 변수들을 콘솔 창에 모두 출력해봅니다.
console.log(node2.childNodes);