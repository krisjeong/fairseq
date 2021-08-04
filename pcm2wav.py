import subprocess
import os

root = "~"
# directory = "datasets_korean/train_data"
directory = "datasets_korean_copy/train_data"

def main():
    for dir1 in os.listdir(directory):  # KsponSpeech_01
        dir1_filepath = os.path.join(directory, dir1)
        for dir2 in os.listdir(dir1_filepath):    # KsponSpeech_0001
            dir2_filepath = os.path.join(dir1_filepath, dir2)       # dir2_filepath = full filepath we need to move to
            os.chdir(f"{dir2_filepath}")        # FileNotFoundError: [Errno 2] No such file or directory: 'datasets_korean_copy/train_data'
            print(os.getcwd())
            # subprocess.run(['sh', "/home/kris/workspace/repo/fairseq/pcm2wav.sh"])
            os.chdir("..")    # TODO: need to get back to original dir
            print(os.getcwd())
        os.chdir("..")  # TODO: need to get back to original dir
        print(os.getcwd())
if __name__ == '__main__':
    main()


# retrieve list of items to change

# for directories:

# pcm2wav.sh 실행