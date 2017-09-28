import pandas as pd
import os
os.chdir('F:\\homeqian\\xxtlog_20161017\\project_config\\xxt\\hdfs')
data = pd.read_csv('xxtlog_20161001DP.csv')
# print request_all.head()
# print request_all.columns
# print request_all.index
request_data = pd.DataFrame(columns=['url', 'type'])
request_data['url'] = data['basic_request_log.url']
request_data['type'] = request_data['url'].apply(lambda x: UserRequest(x))
# print(request_data)
def UserRequest(x)
request_data = request_data[request_data['type'] == 'subway']
request_data['type_subway'] = request_data['url'].apply(lambda x: UserRequest_subway(x))
request_list = []
request_count = []
request_all = pd.DataFrame(columns=['type', 'count'])
for request in request_data['type_subway'].unique():
    request_list.append(request)
    request_count.append(len(request_data[request_data['type_subway'] == request]))
request_all['type'] = request_list
request_all['count'] = request_count
request_all.to_csv('request_count_subway.csv', index=False)