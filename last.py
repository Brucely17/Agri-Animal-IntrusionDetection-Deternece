
import os
from inference_sdk import InferenceHTTPClient

def last_n_recent_files(directory, n=4):
    # Get list of files in the directory
    files = os.listdir(directory)
    
    # Filter out directories, leaving only files
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    
    # Sort files by creation time
    files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)), reverse=True)
    print("files:",files[:n])
    return files[:n]

def get_final_result(directory, num_files=4):
    recent_files = last_n_recent_files(directory, num_files)
    final_result = '1'
    
    if recent_files:
        for file in recent_files:
            CLIENT = InferenceHTTPClient(
                api_url="https://detect.roboflow.com",
                api_key="API_KEY"
            )
            result = CLIENT.infer(os.path.join(directory, file), model_id="thermal-dogs-and-people/3")
            length=len(result['predictions'])
            p=0
            d=0
            pcount=p
            dcount=d
            for i in range(length):
                if result['predictions'][i]['class']=='person':
                    p+=1
                elif result['predictions'][i]['class']=='dog':
                    d+=1

            if p>d:
                print('person',p)
                
                # break
                pcount+=1
            elif p<d:
                # print('person',d)
                print('dog',d)
                dcount+=1
            elif p==0 and d==0:
                pcount+=1
                dcount+=1
                
            
                
            
            if pcount>dcount:
                final_result='1'
            elif pcount<dcount:
                final_result='1'
    


    else:
        print("No files found in the directory.")
    
    return final_result


