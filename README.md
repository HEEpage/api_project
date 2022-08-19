# OPEN API 라이브러리
- 설치방법
```bash
pip install git+https://github.com/HEEpage/api_project.git
```

- 사용방법
```python
from my_api import naver_api

# 검색
search_api(url, client_id, client_secret, params)
# 파파고 번역
translate_api(text, url, client_id, client_secret, source="ko", target="en")
```

```python
from my_api import kakao_api

# 검색
search_api(url, AUTHORIZATION, params)
```