import win32com.client, sys, pathlib

ppt_path = "C://Users//micor//Desktop//YouTube//pptx//test.pptx"
mp4_path = "C://Users//micor//Desktop//YouTube//pptx//test.mp4"

def run(ppt_path, mp4_path):
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible = 1
    ppt.DisplayAlerts = 1
    set = ppt.Presentations.Open(ppt_path)
    mp4_exit = pathlib.Path(mp4_path)
    try:
        set.CreateVideo(mp4_path, True)
    except:
        raise SystemExit
    else:
        print("Convert Successful!")
        while(1):
            if mp4_exit.is_file():
                print("MP4 exists!")
                set.Close()
                ppt.Quit()
                exit()

if __name__ == '__main__':
    run(ppt_path, mp4_path)
