# HttpAutoDiff
* http接口自动化diff工具
## 1使用场景
（如果您在工作遇到以下场景，可以考虑使用本工具让你的工作效率事半功倍）

发生在系统重构过程中，即代码逻辑未发生变更，只调整代码、项目结构时，需要回归外部HTTP或dubbo接口的响应值是否发生变化时
发生在技术改进，需要校验各层吐出数据的准确性，可以采用TestController灵活对新老接口返回数据进行diff
业务发生变更但只新增减少字段，而老字段需要保证数据和以前的一致时
任何新老分支的HTTP接口返回值的差异比较....
2工具简介
本工具是基于python+django框架实现的可视化web工具。输入为新老http接口请求的url、prarm、cookie，输出为http响应值的diff报告。报告展示为两个Json响应比较结果，即old接口相对于new接口返回的Json是新增字段、减少字段亦或是相同字段value发生变更

平台地址：http://b1.opc-api.beta.wormpex.com/chenlie/qa/index（由于返回报告是无状态的，所以目前未接入sso登录）

## 3如何使用
### 3.1使用前准备
建议您使用Google浏览器，并到Google商城安装Json Formatter，这会让返回报告更加格式化
如果您是第一次使用本工具，建议先到Postman中对您要比对的接口进行测试，确保有返回值
### 3.2执行diff
步骤	操作	步骤拆解详情	操作详情
第一步	准备输入参数并填写	
入参解释

request_method：选择框GET / POST
cookie：针对不同环境（dev、beta、gray、prod），抓包获取cookie，只填写value即可
old_url：本次被比较对象的请求url，请注意填写全路径，包括域名
old_param：
GET请求，入参为requestPrarm，请按照 {key1:value1,key2:value2} 的格式进行填写
POST请求，入参为requestBody，请按照{key1:value1,key2:value2} 的格式进行填写
new_url：比较对象的请求url，请注意填写全路径，包括域名
new_param：同上
QA > HTTP接口自动化diff工具使用手册 > image2020-4-28 20:50:23.png
第二步	点击执行diff	点击开始diff按钮触发执行	
第三步	报告查看	执行后报告实时返回，关于报告的详情解释见3.3	QA > HTTP接口自动化diff工具使用手册 > image2020-4-28 20:55:19.png


### 3.3报告展示
字段	释义	样例解释
replace	
表示key相同value不同，即字段存在差异

"prev"为old_url的字段值，"value"为new_url的字段值，"detail"为差异详情

样例：{ "replace": "/effectiveTime","value": "2020-02-24 09:00:53","prev": "2020-02-24 00:00:00"}

解释：json对象中“effectiveTime”字段，在old_url响应中为"2020-02-24 00:00:00"，在new_url响应中为："2020-02-24 09:00:53"

add	表示 exists in new_url的字段 && does not exist in old_url的字段	
样例：{ "add": "/shelfSnapIds/1","value": 47574184,"details": "array-item"}

解释：json对象中“shelfSnapIds”字段为list，它第一个元素的值在new_url响应中存在，在old_url响应中不存在

remove	 表示 exists in old_url的字段 && does not exist in new_url的字段	
样例：{ "remove": "/shelfSnapIds/1","prev": 47574180,"details": "array-item"}

解释：json对象中“shelfSnapIds”字段为list，它第一个元素的值在old_url响应中存在，在new_url响应中不存在



## 4注意事项与补充说明
### 1、http响应值content-type必须为Json对象格式，可以使用公司统一的模板进行封装

### 2、如果接口响应返回状态码为500，可以登录机器【1-b-display-qa-python-http-automated-diff-0】查看堆栈信息，目录为/home/w/www/display_qa_python_http_automated_diff/diffOptools/logs/sys.logs

### 3、若接口无请求参数可不填写，但如果填写一定要注意格式，必须为Json数据格式



## 5后续规划
目前在测试中还未上线的功能如下：

case持久化存储。可以帮您维护一些经常使用的case到数据库
线上日志流量拉取。通过脚本拉取线上流量落到数据库
批量diff。从上面维护的case中批量捞取用例执行diff


## 6意见与反馈
如果您在使用本工具过程中，遇到任何疑问，或不理解的报错，请蜂语联系hang.yu06，会第一时间支持您解决问题
本工具是在店务智能陈列业务部系统重构时进行开发的，为RD和QA在接口自动化回归上节省很多人力，同时提升了回归case的覆盖率。但本工具存在许多不足，如果您发现任何地方实现的不够合理，或者有更好的建议，欢迎随时与我们联系！




