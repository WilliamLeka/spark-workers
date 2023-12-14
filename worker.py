from flask import Flask
from flask import request
import requests
import os
import json
app = Flask(__name__)

## testing if api key is the issue by hard coding into code
def get_api_key():
    return 'ya29.c.c0AY_VpZjI9LTcwnHfzBd2r1sPbv37CnpsE16ARRzZByco54Hl7X16zrwGCvCPqSJrfVTVLocAIgycKhiON43H8xi_wLA0FuyD9QDcq-yYdz4NkyuK2ojV9W20NOLACl9OiOaaeQtlgnyK9fDkK-7z1Yk7FssZH9H57Wx0f75pIkn-TrkQ9hJofv7rS2Fu-xL34Kj3iM9IpvX8ugN0meLA1baeVOYZTSYV91kObi0ppuHlozE1xBV-VzT04e7e0qtQRHTseEjbb8ynHGAZme0WfRDeBDhQLidkeOAOgTSp8lIWpMBBVoh7CsBK7OMEBaoB80OhgAalCshf0HoxW2wOWdruvMCH_pPMAZLjhckz8uf6Y-qAB_Zst2i_tBQztn0SDps7cHLp5Q5e9Iy3RapR--1vKKhYSDU4jHid2gN431Kpwbx4RgYZRnOjnSYpVaRstyedwJr0uQVpoV4ebu_3Q15lMoaw5gama2OYudQ_tJp22eaWi_4caoZ1rg1nRqlUZuoykZt-Yjf5r8UtdiSOahSblI1dSs9VFqh5p5Ig6RfU6u2x9J7tuaZF3Bs531k_Rlmi7M75SR1fOmwWiQ3tZarXvS11BbmMbVlhMh5UM7iQje8pvitfwbqQ8e49UY70hFSXQWng9dgFYmhzXSM-Y_zQkbBSRwXy1_jwxZ19fkmujohR7c4dc0mcfx29c3kr5Rvkt5danXnIMZJ4MBISj8UskU-v_7wu_8m5VMw0n1UfwV0UyoOcwouzWfnn0eFxv4tjitB6JX1Y8ViqRcu57zsm4UrY9isBIcB6aZR1v06S42OIddpj4I8fSJahbx2pkhxcxYqWSM--w6p0dqjefQ7zR6hsB8emXfJeIlsp4eRyvw4tuZcVY-1nRRaQopsnsrkQJSoRfmMoZiympRo8IqlR66czsx4lIdW6dXbV91grppa-S7xoMpZ8nO0f_rOtF9XrZ2mBec39xno4hjzO021Vmqfmt_njxis7UvV6Ymyq4i3ZvX1o-Qi'
    # secret = os.environ.get("COMPUTER_API_KEY")
    # if secret:
    #     return secret
    # else:
        #local testing
       # with open('.key') as f:
            #return f.read()
      
@app.route("/")
def hello():
    return "Add workers to the Spark cluster with a POST request to add"

@app.route("/test")
def test():
    #return "Test" # testing 
    return(get_api_key())

@app.route("/add",methods=['GET','POST'])
def add():
  if request.method=='GET':
    return "Use post to add" # replace with form template
  else:
    token=get_api_key()
    ret = addWorker(token,request.form['num'])
    return ret


def addWorker(token, num):
    with open('payload.json') as p:
      tdata=json.load(p)
    tdata['name']='slave'+str(num)
    data=json.dumps(tdata)
    url='https://www.googleapis.com/compute/v1/projects/rising-analogy-400314/zones/europe-west1-b/instances'
    headers={"Authorization": "Bearer "+token}
    resp=requests.post(url,headers=headers, data=data)
    if resp.status_code==200:     
      return "Done"
    else:
      print(resp.content)
      return "Error\n"+resp.content.decode('utf-8') + '\n\n\n'+data



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
