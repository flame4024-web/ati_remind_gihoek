# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
import sys

# 터미널 한글 깨짐 문제를 대비하여 chcp 설정 및 표준 출력 인코딩 재설정
os.system('chcp 65001 > nul')

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    # 포트가 사용 중일 때를 고려해 재사용 옵션 부여
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print("  농식품부 5급 역량 리마인드 이메일 및 학습 페이지 테스트 서버")
        print("=" * 60)
        print(f"  [서버 구동] 로컬 서버가 성공적으로 가동되었습니다.")
        print(f"  [이메일 확인] http://localhost:{PORT}/1_이메일_템플릿.html")
        print(f"  [학습지 확인] http://localhost:{PORT}/2_기획력_학습_페이지.html")
        print("=" * 60)
        print("  * 서버를 종료하시려면 터미널에서 [Ctrl + C]를 입력하세요.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  [서버 종료] 사용자에 의해 로컬 웹 서버가 종료되었습니다.")
            sys.exit(0)

if __name__ == "__main__":
    run_server()
