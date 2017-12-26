
import requests
import sys
sys.path.append("E:\\GitHub\\Python\\EricCorePy")


from EricCore.EricUtility import EricUtility


res = requests.get('https://tw.yahoo.com/')

#print(res.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

m_Util = EricUtility()

m_Util.to_file("a.html", res.text)

print("finish")