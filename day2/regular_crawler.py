# -*- coding: utf-8 -*-
import re
from day1.download import download


url = 'http://example.webscraping.com/view/UnitedKingdom-239'
html = download(url)
# 正则提取数据
# re.findall('<td class="w2p_fw">(.*?)</td>', html)
result = re.findall('<td class="w2p_fw">(.*?)</td>', html)[1]
print result


# 显示   244,820 square kilometres

# 提高正则健壮性 正则匹配父节点属性
# re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)
