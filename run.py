import os
import subprocess

#with open("/model/run.sh", 'w') as f:
#    f.write("cd /model\n")
#    f.write("python3 setup.py develop\n")

os.system("chmod -R 0777 /results")
#os.system("/model/run.sh")

videos = os.listdir("/dataset")
for video in videos:
    subprocess.run(["mkdir", f"/results/{video}"])
subprocess.run(["python3", "/model/inference_and_eval.py", "--checkpoint_path=/tmp/model.ckpt", 
        f"--input_lr_dir=/dataset", f"--output_dir=/results"])
#   subprocess.run(["python3", "/model/.py", "-n", "RealESRGAN_x4plus", "--input", f"/dataset/{video}", "--face_enhance", "--tile", "1024", "--output", f"/results/{video}"])
