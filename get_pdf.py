from tqdm import tqdm
import os
import re
import requests

# headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}

def download_pdf(download_links_file, article_folder):
    with open(download_links_file, 'r') as f:
        article_download_link_list = f.readlines()
    article_download_link_list = [i.strip() for i in article_download_link_list if i is not '\n']
    print('共计',len(article_download_link_list), '篇文章。')
    a = input('是否立即下载？（是yes/否no）：')
    if a == 'yes':
        import os
        if not os.path.exists(article_folder):
            os.makedirs(article_folder)
        for article_download_link in tqdm(article_download_link_list):
            ad = article_download_link.split('>_<')
            article_name = ad[0]
            # 处理一下article_name，因为windows中不能用\ / : * ? " < > |作为文件名
            article_name = re.sub('[\/:*?"<>|]', '_', article_name)#去掉非法字符
            article_link = ad[1]
            r = requests.get(article_link)
            if r.text[0]!='%':
                nc.append(article_download_link)
                continue
            filename = article_folder+os.sep+'%s.pdf'%article_name
            with open(filename, 'wb+') as f:
                f.write(r.content)
            # 停一下防禁ip
            import time
            time.sleep(1.2)
    elif a == 'no':
        return
    else:
        return

download_links_file = '9178820_9185488_downloadLinks.txt'
article_folder = 'cec2020'
nc=[]
download_pdf(download_links_file, article_folder)
print(len(nc))
with open("nc.txt","w") as f:
    for i in nc:
        print(i,file=f)