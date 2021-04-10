from musicdl import musicdl
import pandas as pd
import time


def run(name):
  time.sleep(10)
  config = {'logfilepath': '/content/drive/MyDrive/Musics/musicdl.log', 'savedir': '/content/drive/MyDrive/Musics', 'search_size_per_source': 5, 'proxies': {}}
  target_srcs = ['qq', 'netease', 'migu']
  client = musicdl.musicdl(config=config)
  search_results = client.search(name, target_srcs)
  # for key, value in search_results.items():
  #     client.download(value)
  # print(search_results)
  try:
    if search_results['migu'] != None:
      for i in range(len(search_results['migu'])):
        if name in search_results['migu'][i]['songname']:
          client.download([search_results['migu'][i]])
  except:
    pass
  
  try:
    if search_results['qq'] != None:
      for i in range(len(search_results['qq'])):
        if name in search_results['qq'][i]['songname']:
          client.download([search_results['qq'][i]])
  except:
    pass

  try:
    if search_results['netease'] != None:
      for i in range(len(search_results['qq'])):
        if name in search_results['qq'][i]['songname']:
          client.download([search_results['netease'][i]])
  except:
    pass

  try:
    client.download([search_results['migu'][0]])
  except:
    pass


data_txt = pd.read_table(r'music_list.txt', sep='\t', header=None).values.tolist()
for i in data_txt:
  run(str(i[0]))