from PIL import Image
import threading
import time

img = Image.open('img1.jpg')
pix = img.load()
print(pix[0,1])
def reverse_image_job(img, start, end):
    for y in range(start, end):
        for x in range(img.size[0]):
            r = 255-pix[x,y][0]
            g = 255-pix[x,y][1]
            b = 255-pix[x,y][2]
            pix[x,y] = (r, g, b)

def thread_managing(img, thread_num):
    threads = []
    for i in range(thread_num):
        start = i * img.size[1] // thread_num
        end = min((i + 1) * img.size[1] // thread_num,img.size[1])
        thread = threading.Thread(target=reverse_image_job, args=(img, start, end))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    img.save('reverse_img_'+str(thread_num)+'_thread.jpg')

start = time.time()
thread_managing(img,4)
end = time.time()
print('execution time:', end-start)
#I start with 1 thread and after I increased the number of threads I didn't notice a decresing in the time,
#so after googling it I found that the GIL is the reason for that. 



#pseudo code:
'''
get the img
split the img into 4 part (for 4 processes)
create 4 processes
each process will reverse the color of a part of the img
start the processes
wait for the processes to finish
combine the parts of the img
save the img


This approach is better than the threading one because the GIL doesn't affect the processes,
I got it after that I have been stuck over 45-minutes with error in normal multiprocessing approach.


for this I will use :
-cv2 library to manipulate the image
-multiprocessing library to create the processes
-time library to calculate the execution time

'''

