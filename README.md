# adjusttime 
時間を調整するモジュール

インストール
```bash
pip install git+https://github.com/sinchir0/adjusttime.git
```

使い方
```python
from adjust_time.adjust_time import adjust_date
adjust_date（"2018-10-01", 1) # -> 2018-10-02
adjust_date（"2018-10-01", -1) # -> 2018-09-30
```

### ref
https://github.com/nyk510/my-awesome-package
https://buildersbox.corp-sansan.com/entry/2019/07/11/110000