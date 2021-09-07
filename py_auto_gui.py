import pyautogui as p

# 마우스 핸들링
## 좌표 인식

p.position()

import time
time.sleep(2)

p.position()

p.size()

p.onScreen(300,300)

p.moveTo(300, 300, duration = 1)  # 좌표로 이동
p.moveRel(500, 500, duration = 1)  # 상대적인 좌표로 이동

p.dragTo(931, 347, 1, button = 'left')  # 드래그 앤 드롭

p.click()
p.click(x = 487, y = 142)
p.click(x = 487, y = 142, button = 'right')

p.doubleClick(x = 487, y = 142)

p.rightClick(x = 487, y = 142)

p.scroll(-1000)
p.scroll(1000)

# 키보드 핸들링

p.keyDown('win')
p.keyUp('win')

p.keyDown('left')
p.keyUp('left')

p.keyDown('shift')
p.keyUp('shift')

p.press('enter')
p.press('f1')
p.press('left')

p.press(['a','b','c'], 2)
p.press(['#','^','_'], 2, 1)  # 1초 간격을 두어 특수문자를 2번 입력

p.hotkey('ctrl', 'shift', 'esc')  # 2개 이상의 키보드 키를 KeyDown 하고 keyUp 

# 메시지 박스

p.alert(text = '확인되었습니다.', title = '인증', button = 'OK')
p.confirm(text = '계속 진행하시겠습니까?', title = '경고', buttons=['OK', 'Cancel'])

p.prompt(text = '아이디를 입력해 주세요.', title= '로그인', default = 'RPA_TEST')
p.password(text='패스워드를 입력해 주세요.', title='비밀번호', default='')

# 스크린샷

## 모니터 전체 화면을 이미지 객체로 전환
im1 = p.screenshot()
im2 = p.screenshot('my_screenshot.png')  # full path를 지정할 수 있다.
im3 = p.screenshot('my_screenshot.png', region=(0,0,300,400))

